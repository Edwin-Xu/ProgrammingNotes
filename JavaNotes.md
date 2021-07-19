# Java Notes

## sneakyThrows

lombok的功能

`@SneakyThrows`注解的用途得从java的异常设计体系说起。
 java中我们常见的2类异常。
 1.普通`Exception`类,也就是我们常说的受检异常或者Checked Exception。
 2.`RuntimeException`类，既运行时异常。
 前者会强制要求抛出它的方法声明throws，调用者必须显示的去处理这个异常。设计的目的是为了提醒开发者处理一些场景中必然可能存在的异常情况。比如网络异常造成IOException。

但是现实，往往事与愿违。大部分情况下的异常，我们都是一路往外抛了事。（强制处理我也处理不了啊！臣妾做不到）所以渐渐的java程序员处理Exception的常见手段就是外面包一层RuntimeException，接着往上丢。这种解决思想尤其在Spring中到处出现。

```php
try{
}catch(Exception e){
	throw new RuntimeException(e);
}
```

Lombok的@SneakyThrows就是为了消除这样的模板代码。
使用注解后不需要担心Exception的处理

```dart
 import lombok.SneakyThrows;

public class SneakyThrowsExample implements Runnable {
  @SneakyThrows(UnsupportedEncodingException.class)
  public String utf8ToString(byte[] bytes) {
    return new String(bytes, "UTF-8");
  }
  
  @SneakyThrows
  public void run() {
    throw new Throwable();
  }
}
```

真正生成的代码

```java
import lombok.Lombok;

public class SneakyThrowsExample implements Runnable {
  public String utf8ToString(byte[] bytes) {
    try {
      return new String(bytes, "UTF-8");
    } catch (UnsupportedEncodingException e) {
      throw Lombok.sneakyThrow(e);
    }
  }
  
  public void run() {
    try {
      throw new Throwable();
    } catch (Throwable t) {
      throw Lombok.sneakyThrow(t);
    }
  }
}
```

Lombok.sneakyThrow():

```java
    public static RuntimeException sneakyThrow(Throwable t) {
        if (t == null) throw new NullPointerException("t");
        return Lombok.<RuntimeException>sneakyThrow0(t);
    }

    private static <T extends Throwable> T sneakyThrow0(Throwable t) throws T {
        throw (T)t;
    }
    
```

利用泛型将我们传入的**Throwable强转为RuntimeException**。虽然事实上我们不是RuntimeException。但是没关系。因为**JVM并不关心这个。泛型最后存储为字节码时并没有泛型的信息**。这样写只是为了**骗过javac编译器**。



```java
Example usage:
public void run() {
	 throw sneakyThrow(new IOException("You don't need to catch me!"));
}
```



## Thread

### deamon

```
# 将一个线程设置为守护线程
thread.setDaemon(true);
```

**当运行的线程都是守护进程线程时，Java虚拟机会退出。**

setDaemon()必须在start之前得到调用



### join

```
public final synchronized void join(long millis) throws InterruptedException
```

Waits at most millis milliseconds for this thread to die

**主线程等待该线程millis毫秒，等待millis毫秒后主线程会继续执行，如果子线程运行不需要millis毫秒，则主线程在子线程结束后就会执行**

> 注意: join应该在start之后调佣，子线程启动后才会有等待一说



### interrupt() interruptted



### ThreadFactory





## JUC 

juc(Doug Lea贡献)下可以分为4类：

- 并发任务的提交
- 线程安全集合类
- CAS
- 线程协调类：如Semaphore



### ReadWriteLock



### ReentrantLock



### Semaphore

信号量，用来控制访问特定资源的线程数量

```java
acquire()  
获取一个令牌，在获取到令牌、或者被其他线程调用中断之前线程一直处于阻塞状态。

acquire(int permits)  
获取一个令牌，在获取到令牌、或者被其他线程调用中断、或超时之前线程一直处于阻塞状态。
    
acquireUninterruptibly() 
获取一个令牌，在获取到令牌之前线程一直处于阻塞状态（忽略中断）。
    
tryAcquire()
尝试获得令牌，返回获取令牌成功或失败，不阻塞线程。

tryAcquire(long timeout, TimeUnit unit)
尝试获得令牌，在超时时间内循环尝试获取，直到尝试获取成功或超时返回，不阻塞线程。

release()
释放一个令牌，唤醒一个获取令牌不成功的阻塞线程。

hasQueuedThreads()
等待队列里是否还存在等待线程。

getQueueLength()
获取等待队列里阻塞的线程数。

drainPermits()
清空令牌把可用令牌数置为0，返回清空令牌的数量。

availablePermits()
返回可用的令牌数量。
```



原理：利用AQS

### CountDownLatch



### Future

```java
public class FutureTest01 {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService executorService = Executors.newFixedThreadPool(10);
        // submit的任务，只会执行一次，get第一次调用时运行，并得到运行结果
        Future<Integer> submit = executorService.submit(() -> {
            System.out.println("begin");
            Thread.sleep(2000);
            System.out.println("end");
            return (int) (Math.random() * 100);
        });
        Integer integer = null;
        try {
            integer = submit.get(1000, TimeUnit.MILLISECONDS);
            System.out.println(integer);
        } catch (InterruptedException | TimeoutException | ExecutionException e) {
            System.out.println(e.getMessage());
        }

        try {
            integer = submit.get(3000, TimeUnit.MILLISECONDS);
            System.out.println(integer);
        } catch (InterruptedException | TimeoutException | ExecutionException e) {
            System.out.println(e.getMessage());
        }

        System.out.println(submit.get());
        System.out.println(submit.get());
        /*
        * output：
        * begin
            null
            end
            33
            33
            33
        * */
    }
}
```



Future 的重要方法：

- get(): 获取任务执行的返回值，可以传入时间，时间到之前阻塞线程，直到返回

- ```
  boolean cancel(boolean mayInterruptIfRunning);
  可以取消未执行/执行中的任务
  如果取消后再次get, 则会抛出CancellationException
  
  ```



### RunnableFuture

```
public interface RunnableFuture<V> extends Runnable, Future<V> {
    /**
     * Sets this Future to the result of its computation
     * unless it has been cancelled.
     */
    void run();
}
```

RunnableFuture是可以运行的Future，它还允许访问执行结果





## 日志

#### SLF4j

SLF4J仿佛就是一个日志接口，Log4J更像是一个底层的实现，其中SLF4J提供了绝大部分的日志实现，在它下面可以包括更多的日志实现框架，比如Logback等等



SLF4J，即简单日志门面（Simple Logging Facade for Java），不是具体的日志解决方案，它只服务于各种各样的日志系统。按照官方的说法，SLF4J是一个用于日志系统的简单Facade，允许最终用户在部署其应用时使用其所希望的日志系统。

(SLF4J是一个抽象，相当于接口，可以适配到任何实现，他也有自己的多个具体实现)

```
 Logger logger = LoggerFactory.getLogger(PlaceHolders.class);
```

```
<!-- slf4j依赖 -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>1.7.12</version>
		</dependency>
		<!-- log4j依赖 -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-log4j12</artifactId>
			<version>1.7.12</version>
		</dependency>
		<dependency>
			<groupId>log4j</groupId>
			<artifactId>log4j</artifactId>
			<version>1.2.17</version>
		</dependency>
		<!-- logback依赖 -->
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.1.2</version>
		</dependency>
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
			<version>1.1.2</version>
		</dependency>
		<!-- slf4j自带的简单日志 -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-simple</artifactId>
			<version>1.7.12</version>
		</dependency>
		<!-- jdk自带的日志 -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-jdk14</artifactId>
			<version>1.7.12</version>
		</dependency>
		<!-- common-logging日志框架 -->
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-jcl</artifactId>
			<version>1.7.12</version>
		</dependency>
		<dependency>
			<groupId>commons-logging</groupId>
			<artifactId>commons-logging</artifactId>
			<version>1.2</version>
		</dependency>

```





#### log4j

Log4j是Apache的一个开源项目，通过使用Log4j，我们可以控制日志信息输送的目的地是控制台、文件、GUI组件，甚至是套接口服务器、NT的事件记录器、UNIX Syslog守护进程等；我们也可以控制每一条日志的输出格式；通过定义每一条日志信息的级别，我们能够更加细致地控制日志的生成过程。最令人感兴趣的就是，这些可以通过一个配置文件来灵活地进行配置，而不需要修改应用的代码。

```
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.12</version>
</dependency>
```

```
static final Logger logger = Logger.getLogger(Log4jTest.class);
```

config:

```bash
# Global logging configuration
# 设置日志输出级别以及输出目的地，可以设置多个输出目的地，开发环境下，日志级别要设置成DEBUG或者ERROR
# 前面写日志级别，逗号后面写输出目的地：我自己下面设置的目的地相对应，以逗号分开
# log4j.rootLogger = [level],appenderName1,appenderName2,…
log4j.rootLogger=DEBUG,CONSOLE,LOGFILE

#### 控制台输出 ####
log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
# 输出到控制台
log4j.appender.CONSOLE.Target = System.out
# 指定控制台输出日志级别
log4j.appender.CONSOLE.Threshold = DEBUG
# 默认值是 true, 表示是否立即输出
log4j.appender.CONSOLE.ImmediateFlush = true
# 设置编码方式
log4j.appender.CONSOLE.Encoding = UTF-8
# 日志输出布局
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
# 如果日志输出布局为PatternLayout 自定义级别，需要使用ConversionPattern指定输出格式
log4j.appender.CONSOLE.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %5p (%c:%L) - %m%n



#### 输出错误信息到文件 ####
log4j.appender.LOGFILE=org.apache.log4j.FileAppender
# 指定输出文件路径
#log4j.appender.LOGFILE.File =F://Intellij idea/logs/error.log 
log4j.appender.LOGFILE.File =./logs/error.log 

#日志输出到文件，默认为true
log4j.appender.LOGFILE.Append = true
# 指定输出日志级别
log4j.appender.LOGFILE.Threshold = ERROR
# 是否立即输出，默认值是 true,
log4j.appender.LOGFILE.ImmediateFlush = true
# 设置编码方式
log4j.appender.LOGFILE.Encoding = UTF-8
# 日志输出布局
log4j.appender.LOGFILE.layout = org.apache.log4j.PatternLayout
# 如果日志输出布局为PatternLayout 自定义级别，需要使用ConversionPattern指定输出格式
log4j.appender.LOGFILE.layout.ConversionPattern = %-d{yyyy-MM-dd HH:mm:ss}  [ %t:%r ] - [ %p ]  %m%n
```



常用的：

```
		<dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.31</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.31</version>
        </dependency>
   
   
   
log4j.rootLogger=info,CONSOLE,FILE

log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=[%-5p] %d{yyyy-MM-dd HH:mm:ss} %C{1}@(%F:%L):%m%n

log4j.appender.FILE=org.apache.log4j.DailyRollingFileAppender
log4j.appender.FILE.File=${catalina.base}/logs/spring-web.log
log4j.appender.FILE.Encoding=utf-8
log4j.appender.FILE.DatePattern='.'yyyy-MM-dd
log4j.appender.FILE.layout=org.apache.log4j.PatternLayout
log4j.appender.FILE.layout.ConversionPattern=[%-5p] %d{yyyy-MM-dd HH\:mm\:ss} %C{1}@(%F\:%L)\:%m%n
```



### log IDEA Live Template

添加java live Template log

编辑属性，Expression设置为className()

```java
private static final Logger logger = LoggerFactory.getLogger(FutureTest02.class);
```

然后编辑器敲如log回车即可



