# Jdbc Notes

## 

## Basic Notes

### 参数

属性名	描述	默认值
driverClassName	用户名	-
url	密码	-
username	建立连接的url	-
password	数据库驱动的完整类名	-
initialSize	连接器启动时创建的初始连接数	10
maxActive	最大连接数，通常为常规访问的最大数据库并发数，建议根据后期jmx监控逐渐调优	100
maxIdle	最大空闲连接数，比较难把握的一个参数，许多连接池也已经移除了此属性(如Druid)，访问峰值比较集中的系统如考勤可以设置小一点节省大部分时段的连接资源，过小也可能导致连接频繁创建关闭也会影响性能，建议一般系统不低于maxActive的50%	100
minIdle	最小连接数,一般与initialSize一致即可	10
maxWait	连接池中连接用完时，新的请求的等待时间，超时返回异常，单位毫秒	默认30000
testWhileIdle	连接进入空闲状态时是否经过空闲对象驱逐进程同时进行校验，推荐的校验方法，依赖validationQuery	false
validationQuery	在连接返回给调用者前用于校验连接是否有效的SQL语句，必须为一个SELECT语句，且至少有一行结果	-
validationQueryTimeout	连接验证的超时时间，单位秒，注：池本身并不会让查询超时，完全是依靠JDBC驱动来强制查询超时	-
validationInterval	TomcatJDBC特有属性，检查连接可用性的时间间隔，防止testOnBorrow和testOnReturn为true时检查过于频繁，单位毫秒	30000
timeBetweenEvictionRunsMillis	空闲对象驱逐检查时间间隔，单位毫秒	5000
minEvictableIdleTimeMillis	连接被空闲对象驱逐进程驱逐前在池中保持空闲状态的最小时间，单位毫秒	60000
defaultAutoCommit	连接池所创建的连接默认自动提交状态（JDBC缺省值意思是默认不会调用setAutoCommit方法）	JDBC缺省值
jmxEnabled	是否利用 JMX 注册连接池	true
jdbcInterceptors	TomcatJDBC特有属性， QueryTimeoutInterceptor（查询超时拦截器，属性queryTimeout，单位秒，默认1秒），SlowQueryReport（慢查询记录，属性threshold超时纪录阈值单位毫秒，默认1000），多个用拦截器用;分隔，示例：QueryTimeoutInterceptor(queryTimeout=5);SlowQueryReport(threshold=3000)注：当新语句创建时，自动调用Statement.setQueryTimeout(seconds)。池本身并不会让查询超时，完全是依靠JDBC驱动来强制查询超时，更详细的信息请查看官方文档	-
testOnBorrow	连接被调用时是否校验，依赖validationQuery，对性能有一定影响，不推荐使用	false
testOnReturn	连接返回到池中是时是否校验,依赖validationQuery，对性能有一定影响，不推荐使用	false
removeAbandoned	是否清除已经超过 removeAbandonedTimeout 设置的连接，可用于排查一些事务未提交的问题(正式环境谨慎使用,对性能有一定影响),不推荐使用，可用QueryTimeOut拦截器替代	false
removeAbandonedTimeout	清除无效连接的时间，单位秒 与removeAbandoned联合使用	60
defaultReadOnly	连接池创建的连接是否是否为只读，需要说明的是设置了true只是告诉数据库连接是只读，便于数据库做一些优化(例如不安排数据库锁)，并非不能执行更新操作，只是对数据的一致性的保护并不强而已（这跟spring的只读事务类似）	JDBC缺省

https://blog.csdn.net/QQ736238785/article/details/106850145





### 连接池连接数

在配置tomcat数据库连接池时候，对配置的具体数值总是懵逼。这里给出具体建议。

首先上公式：
数据库**连接池连接数 = ((核心数 * 2) + 有效磁盘数)**
核心数如何得到？

linux 查看物理cpu的个数

> cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
>
> 查看每个物理CPU中core的个数(即核数)

> cat /proc/cpuinfo| grep "cpu cores"| uniq两数相乘即得到核心数。
> 

## Problems

### PoolExhaustedException

```java
PoolExhaustedException:Unable to fetch a connection in 4 seconds, none available[size:100; busy:100; idle:0; lastwait:4000]
```

连接池中没有连接了，等待了maxWait时间，没有则抛异常





