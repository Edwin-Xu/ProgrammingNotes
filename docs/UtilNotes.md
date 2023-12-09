# Util Notes

## StopWatch

利用StopWatch监控Java代码运行时间和分析性能

```java
public static void main(String[] args) {
  Long startTime = System.currentTimeMillis();
  // 你的业务代码
  Long endTime = System.currentTimeMillis();
  Long elapsedTime = (endTime - startTime) / 1000;
  System.out.println("该段总共耗时：" + elapsedTime + "s");
}
```

我们可以利用已有的工具类中的秒表，常见的秒表工具类有 `org.springframework.util.StopWatch、org.apache.commons.lang.time.StopWatch`以及谷歌提供的guava中的秒表

### Spring

StopWatch 是位于 `org.springframework.util` 包下的一个工具类，通过它可方便的对程序部分代码进行计时(ms级别)，适用于同步单线程代码块

```java
public static void main(String[] args) throws InterruptedException {
    StopWatch stopWatch = new StopWatch();

    // 任务一模拟休眠3秒钟
    stopWatch.start("TaskOneName");
    Thread.sleep(1000 * 3);
    System.out.println("当前任务名称：" + stopWatch.currentTaskName());
    stopWatch.stop();

    // 任务一模拟休眠10秒钟
    stopWatch.start("TaskTwoName");
    Thread.sleep(1000 * 10);
    System.out.println("当前任务名称：" + stopWatch.currentTaskName());
    stopWatch.stop();

    // 任务一模拟休眠10秒钟
    stopWatch.start("TaskThreeName");
    Thread.sleep(1000 * 10);
    System.out.println("当前任务名称：" + stopWatch.currentTaskName());
    stopWatch.stop();

    // 打印出耗时
    System.out.println(stopWatch.prettyPrint());
    System.out.println(stopWatch.shortSummary());
    // stop后它的值为null
    System.out.println(stopWatch.currentTaskName()); 
    
    // 最后一个任务的相关信息
    System.out.println(stopWatch.getLastTaskName());
    System.out.println(stopWatch.getLastTaskInfo());
    
    // 任务总的耗时  如果你想获取到每个任务详情（包括它的任务名、耗时等等）可使用
    System.out.println("所有任务总耗时：" + sw.getTotalTimeMillis());
    System.out.println("任务总数：" + sw.getTaskCount());
    System.out.println("所有任务详情：" + sw.getTaskInfo());
}
```

StopWatch 不仅正确记录了上个任务的执行时间，并且在最后还可以给出精确的任务执行时间（纳秒级别）和耗时占比

- **StopWatch对象不是设计为线程安全的，并且不使用同步。**
- **一个StopWatch实例一次只能开启一个task，不能同时start多个task**
- **在该task还没stop之前不能start一个新的task，必须在该task stop之后才能开启新的task**
- **若要一次开启多个，需要new不同的StopWatch实例**

### apache

`apache commons lang3` 包下的一个任务执行时间监视器

```java
public static void main(String[] args) throws InterruptedException {
    //创建后立即start，常用
    StopWatch watch = StopWatch.createStarted();

    // StopWatch watch = new StopWatch();
    // watch.start();

    Thread.sleep(1000);
    System.out.println(watch.getTime());
    System.out.println("统计从开始到现在运行时间：" + watch.getTime() + "ms");

    Thread.sleep(1000);
    watch.split();
    System.out.println("从start到此刻为止的时间：" + watch.getTime());
    System.out.println("从开始到第一个切入点运行时间：" + watch.getSplitTime());
    Thread.sleep(1000);
    watch.split();
    System.out.println("从开始到第二个切入点运行时间：" + watch.getSplitTime());

    // 复位后, 重新计时
    watch.reset();
    watch.start();
    Thread.sleep(1000);
    System.out.println("重新开始后到当前运行时间是：" + watch.getTime());

    // 暂停 与 恢复
    watch.suspend();
    System.out.println("暂停2秒钟");
    Thread.sleep(2000);

    // 上面suspend，这里要想重新统计，需要恢复一下
    watch.resume();
    System.out.println("恢复后执行的时间是：" + watch.getTime());

    Thread.sleep(1000);
    watch.stop();

    System.out.println("花费的时间》》" + watch.getTime() + "ms");
    // 直接转成s
    System.out.println("花费的时间》》" + watch.getTime(TimeUnit.SECONDS) + "s");
}
```





## Jrebel

**激活网址列表，尽量用排序靠前的**

http://jrebel-license.jiweichengzhu.com/{GUID}

https://jrebel.qekang.com/{GUID}

**GUID可以使用[在线GUID地址](https://www.guidgen.com/)在线生成，然后替换{GUID}就行。**

















