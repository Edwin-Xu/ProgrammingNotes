# Qunar TC DEV

公共组件

- pom
- 
- common
- Qconfig
- qSchedyle
- qmq
- Qtrance
- Qmonitor
- mysql、Redis

### TCDev POM

公共父pom

### 公共应用中心

portal

### Common基础库



- common-rpc
- common-sentinel: 阿里的sentinel， 从流量控制、熔断降级、系统负载保护等多个纬度保护系统的稳定性

### QConfig

配置中心，类似apllo

@QConfig,注册到Spring的context中

### QMQ

可靠性作为设计考量



newQMQ, 新的MQ，目前往其迁移，开源



QMQ不能保证 消息 有序

### QSchedule

调度

Cron表达式



### bistoury

集成阿里Archas



### MySQL和Redis数据源

三种MySQL HA方案

HA： High Availability高可用解决方案



DBA集群方案



### QMonitor

作用：

- 观察系统状态：线程数量、GC情况
- 观察业务状态：订单量、处理耗时
- 报警，发现异常，及时修复

监控指标：

- 时间
- 次数，如QPS、瞬时值、分钟总数



### 其他

QTalk咨询热线：

tcevrexian

