# Redis Notes





## 简介

- 高性能
- 高可用
- 高扩展
- 类型丰富





## 基本知识

### Jedis

Redis不仅是使用命令来操作，现在基本上主流的语言都有**客户端支持**，比如java、C、C#、C++、php、Node.js、Go等。 在官方网站里列一些Java的客户端，有**Jedis**、Redisson、**Jredis**、JDBC-Redis、等其中官方推荐使用**Jedis**和**Redisson**。


Jedis API:

![image-20211119102021309](_images/RedisNotes.assets/image-20211119102021309.png)



Jedis连接池：

jedis连接资源的创建与销毁是很消耗程序性能，所以jedis为我们提供了jedis的池化技术，jedisPool在创建时初始化一些连接资源存储到连接池中，使用jedis连接资源时不需要创建，而是从连接池中获取一个资源进行redis的操作，使用完毕后，不需要销毁该jedis连接资源，而是将该资源归还给连接池，供其他请求使用。


```java
package com.itheima.utils;
 
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
 
public class JedisPoolUtils {
    被volatile修饰的变量不会被本地线程缓存，对该变量的读写都是直接操作共享内存。
    private static volatile JedisPool jedisPool;
    private JedisPoolUtils() {
    }
    //获得连接池对象
    public static JedisPool getJedisPoolInstance(){
        if(jedisPool==null){
            synchronized (JedisPoolUtils.class){
                if(jedisPool==null){
                    JedisPoolConfig config = new JedisPoolConfig();
                    config.setMaxActive(30);
                    config.setMaxIdle(10);
                    jedisPool=new JedisPool(config,"127.0.0.1",6379);
                }
            }
        }
        return jedisPool;
    }
    //归还连接
    public static void  release(JedisPool jedisPool,Jedis jedis){
        if(jedis!=null){
        jedisPool.returnResource(jedis);
        }
    }
}
```



JedisPoolConfig的配置参数
（1）maxActive：控制一个pool可分配多少个jedis实例，通过pool.getResource()来获取；如果赋值为-1，则表示不限制；如果pool已经分配了maxActive个jedis实例，则此时pool的状态为exhausted。
（2）maxIdle：控制一个pool最多有多少个状态为idle(空闲)的jedis实例；
（3）whenExhaustedAction：表示当pool中的jedis实例都被allocated完时，pool要采取的操作；默认有三种。
（4）maxWait：表示当borrow一个jedis实例时，最大的等待时间，如果超过等待时间，则直接抛JedisConnectionException；
（5）testOnBorrow：获得一个jedis实例的时候是否检查连接可用性（ping()）；如果为true，则得到的jedis实例均是可用的；
（6）testOnReturn：return 一个jedis实例给pool时，是否检查连接可用性（ping()）；
（7）testWhileIdle：如果为true，表示有一个idle object evitor线程对idle object进行扫描，如果validate失败，此object会被从pool中drop掉；这一项只有在timeBetweenEvictionRunsMillis大于0时才有意义；
（8）timeBetweenEvictionRunsMillis：表示idle object evitor两次扫描之间要sleep的毫秒数；
（9）numTestsPerEvictionRun：表示idle object evitor每次扫描的最多的对象数；
（10）minEvictableIdleTimeMillis：表示一个对象至少停留在idle状态的最短时间，然后才能被idle object evitor扫描并驱逐；这一项只有在timeBetweenEvictionRunsMillis大于0时才有意义；
（11）softMinEvictableIdleTimeMillis：在minEvictableIdleTimeMillis基础上，加入了至少minIdle个对象已经在pool里面了。如果为-1，evicted不会根据idle time驱逐任何对象。如果minEvictableIdleTimeMillis>0，则此项设置无意义，且只有在timeBetweenEvictionRunsMillis大于0时才有意义；
（12）lifo：borrowObject返回对象时，是采用DEFAULT_LIFO（last in first out，即类似cache的最频繁使用队列），如果为False，则表示FIFO队列；

### Lettuce

Spring-data-redis 现在好像默认使用 Lettuce 作为默认的客户端

Lettuce是一个高性能基于Java编写的Redis驱动框架，底层集成了Project Reactor提供天然的反应式编程，通信框架集成了Netty使用了非阻塞IO，5.x版本之后融合了JDK1.8的异步编程特性，在保证高性能的同时提供了十分丰富易用的API

`5.1`版本的新特性如下：

- 支持`Redis`的新增命令`ZPOPMIN, ZPOPMAX, BZPOPMIN, BZPOPMAX`。
- 支持通过`Brave`模块跟踪`Redis`命令执行。
- 支持`Redis Streams`。
- 支持异步的主从连接。
- 支持异步连接池。
- 新增命令最多执行一次模式（禁止自动重连）。
- 全局命令超时设置（对异步和反应式命令也有效）。

```sql
<dependency>
    <groupId>io.lettuce</groupId>
    <artifactId>lettuce-core</artifactId>
    <version>5.1.8.RELEASE</version>
</dependency>
```



`Lettuce`主要提供三种`API`：

- 同步（`sync`）：`RedisCommands`。
- 异步（`async`）：`RedisAsyncCommands`。
- 反应式（`reactive`）：`RedisReactiveCommands`。



## 官网学习

https://redis.com.cn/

docker exec -it myredis redis-cli

### 配置

在 Redis 中，Redis 的根目录中有一个配置文件（redis.conf）。您可以通过 Redis CONFIG 命令获取和设置所有 Redis 配置。

要更新配置，可以直接编辑 redis.conf 文件，也可以通过 CONFIG set 命令更新配置。

```
config get *
CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE
```

#### redis.conf配置项说明

Redis 默认不是以守护进程的方式运行，可以通过该配置项修改，使用 yes 启用守护进程

```
config get daemonize
1) "daemonize"
2) "no"
```

当 Redis 以守护进程方式运行时，Redis 默认会把 pid 写入 /var/run/redis.pid 文件，可以通过 pidfile 指定:**pidfile /var/run/redis.pid**

port:指定 Redis 监听端口，默认端口为 6379，作者在自己的一篇博文中解释了为什么选用 6379 作为默认端口，因为 6379 在手机按键上 MERZ 对应的号码，而 MERZ 取自意大利歌女 Alessia Merz 的名字

bind: 绑定的主机地址

```
127.0.0.1:6379> config get bind
1) "bind"
2) "* -::*"
127.0.0.1:6379> config get port
1) "port"
2) "6379"
127.0.0.1:6379>
```

timeout: 当客户端闲置多长时间后关闭连接，如果指定为 0，表示关闭该功能

**loglevel**:指定日志记录级别，Redis 总共支持四个级别：debug、verbose、notice、warning，默认为 verbose

**logfile**:日志记录方式，默认为标准输出，如果配置 Redis 为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给 /dev/null

**databases** :置数据库的数量，默认数据库为 0，可以使用 SELECT `<dbid>` 命令在连接上指定数据库 id

```
127.0.0.1:6379> config get databases
1) "databases"
2) "16"
```

**save**:指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合

```
save <seconds> <changes>
Redis 默认配置文件中提供了三个条件：
save 900 1
save 300 10
save 60 10000
分别表示 90 0 秒（15 分钟）内有 1 个更改，300 秒（5 分钟）内有 10 个更改以及 60 秒内有 10000 个更改。
```

**rdbcompression**:指定存储至本地数据库时是否压缩数据，默认为 yes，Redis 采用 LZF 压缩，如果为了节省 CPU 时间，可以关闭该选项，但会导致数据库文件变的巨大

**dbfilename** :指定本地数据库文件名，默认值为 dump.rdb

**dir**:指定本地数据库存放目录

**slaveof** :设置当本机为 slave 服务时，设置 master 服务的 IP 地址及端口，在 Redis 启动时，它会自动从 master 进行数据同步

**masterauth**:当 master 服务设置了密码保护时，slave 服务连接 master 的密码

**requirepass** :设置 Redis 连接密码，如果配置了连接密码，客户端在连接 Redis 时需要通过 AUTH `<password>`命令提供密码，默认关闭

**maxclients** :设置同一时间最大客户端连接数，默认无限制，Redis 可以同时打开的客户端连接数为 Redis 进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis 会关闭新的连接并向客户端返回 max number of clients reached 错误信息

**maxmemory**:指定 Redis 最大内存限制，Redis 在启动时会把数据加载到内存中，达到最大内存后，Redis 会先尝试清除已到期或即将到期的 Key，当此方法处理后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis 新的 vm 机制，会把 Key 存放内存，Value 会存放在 swap 区

**appendonly** :指定是否在每次更新操作后进行日志记录，Redis 在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis 本身同步数据文件是按上面 save 条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为 no

**appendfilename**:指定更新日志文件名，默认为 appendonly.aof

**appendfsync** :

指定更新日志条件，共有 3 个可选值：  

**no**：表示等操作系统进行数据缓存同步到磁盘（快）  

**always**：表示每次更新操作后手动调用 fsync() 将数据写到磁盘（慢，安全） 

**everysec**：表示每秒同步一次（折衷，默认值）

```
127.0.0.1:6379> config get appendonly
1) "appendonly"
2) "yes"
127.0.0.1:6379> config get appendfilename
1) "appendfilename"
2) "appendonly.aof"
127.0.0.1:6379> config get appendfsync
1) "appendfsync"
2) "everysec"
```

 **vm-enabled**:指定是否启用虚拟内存机制，默认值为 no，简单的介绍一下，VM 机制将数据分页存放，由 Redis 将访问量较少的页即冷数据 swap 到磁盘上，访问多的页面由磁盘自动换出到内存中

**vm-max-memory**:

将所有大于 vm-max-memory 的数据存入虚拟内存,无论 vm-max-memory 设置多小,所有索引数据都是内存存储的( Redis 的索引数据就是 keys ),也就是说,当 vm-max-memory 设置为 0 的时候,其实是所有 value 都存在于磁盘。默认值为 0

**vm-page-size**:Redis swap 文件分成了很多的 page，一个对象可以保存在多个 page 上面，但一个 page 上不能被多个对象共享，vm-page-size 是要根据存储的数据大小来设定的，作者建议如果存储很多小对象，page 大小最好设置为 32 或者 64 bytes；如果存储很大大对象，则可以使用更大的 page，如果不确定，就使用默认值

**vm-pages** :设置 swap 文件中的 page 数量，由于页表（一种表示页面空闲或使用的 bitmap）是在放在内存中的，在磁盘上每 8 个 pages 将消耗 1byte 的内存。

**vm-max-threads**:置访问 swap 文件的线程数,最好不要超过机器的核数

**glueoutputbuf** :设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启

### 数据类型

五种类型

#### 字符串String

String 是一组字节。在 Redis 数据库中，字符串是二进制安全的。这意味着它们具有已知长度，并且不受任何特殊终止字符的影响。可以在一个字符串中存储最多 512 兆字节的内容。





### 命令

#### key

```shell
# del
del key1 key2

# dump 序列化key
127.0.0.1:6379> dump a
"\x00\xc0{\n\x00H\xe2S\xe1\x00zg\xb9"
127.0.0.1:6379>

# exists 存在性
127.0.0.1:6379> exists a b
(integer) 1
127.0.0.1:6379> exists a
(integer) 1


# expire
设置 key 的过期时间（seconds）。 设置的时间过期后，key 会被自动删除。带有超时时间的 key 通常被称为易失的(volatile)。
超时时间只能使用删除 key 或者覆盖 key 的命令清除，包括 DEL, SET, GETSET 和所有的 *STORE 命令。 对于修改 key 中存储的值，而不是用新值替换旧值的命令，不会修改超时时间。例如，自增 key 中存储的值的 INCR , 向list中新增一个值 LPUSH, 或者修改 hash 域的值 HSET ，这些都不会修改 key 的过期时间。

通过使用 PERSIST 命令把 key 改回持久的(persistent) key，这样 key 的过期时间也可以被清除。

key使用 RENAME 改名后，过期时间被转移到新 key 上。
已存在的旧 key 使用 RENAME 改名，那么新 key 会继承所有旧 key 的属性。例如，一个名为 KeyA 的 key 使用命令 RENAME Key_B Key_A 改名，新的 KeyA 会继承包括超时时间在内的所有 Key_B 的属性。

特别注意，使用负值调用 EXPIRE/PEXPIRE 或使用过去的时间调用 EXPIREAT/PEXPIREAT ，那么 key 会被删除 deleted 而不是过期。 (因为, 触发的key event 将是 del, 而不是 expired).
已经设置过期的key，可以调用 EXPIRE 重新设置。在这种情况下 key 的生存时间被更新为新值。

key 的过期时间以绝对 Unix 时间戳的方式存储。这意味无论 Redis 是否运行，过期时间都会流逝。

服务器的时间必须稳定准确，这样过期时间才能更准确。如果在两个时间相差较多的机器之间移动 RDB 文件，那么可能会出现所有的 key 在加载的时候都过期了。

运行的 Redis 也会不停的检查服务器的时间，如果你设置一个带有 1000 秒过期时间的key，然后你把服务器的时间向前调了 2000 秒，那么这个 key 会立刻过期，不是等 1000 秒后过期。


# EXPIREAT
EXPIREAT 与 EXPIRE 有相同的作用和语义, 不同的是 EXPIREAT 使用绝对 Unix 时间戳 (自1970年1月1日以来的秒数)代替表示过期时间的秒数。使用过去的时间戳将会立即删除该 key。
EXPIREAT 引入的目的是为了把 AOF 持久化模式的相对时间转换为绝对时间。当然，也可以直接指明某个 key 在未来某个时间过期。

# keys

```







## Jredis

## Redisson

## Luc...



























