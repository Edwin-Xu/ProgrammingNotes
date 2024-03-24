# InfluxDB Notes





## MyNotes



### 概述

InfluxDB是一个用于存储和分析时间序列数据的开源数据库。



#### 特点

1. 高性能：InfluxDB具有高效的写入和查询速度，可以处理大量的时序数据。
2. 分布式架构：InfluxDB可以轻松地扩展到多个节点，以处理大规模的数据集。
3. 灵活的数据模型：InfluxDB使用测量、标签和字段的数据模型，可以灵活地存储和查询不同类型的数据。
4. SQL-like语言：InfluxDB使用类似于SQL的查询语言，使得数据查询和分析变得更加容易。
5. 多种数据格式支持：InfluxDB支持多种数据格式，包括JSON、CSV和Graphite等。
6. 可视化工具支持：InfluxDB可以与多种可视化工具集成，例如Grafana和Kibana等，使得数据可视化和监控变得更加容易。
7. 开放源代码：InfluxDB是一款开放源代码的软件，可以自由使用和修改，也有一个活跃的开发社区支持和维护。

### 基本概念

数据库

InfluxDB中的数据库类似于其他数据库系统中的数据库，它是一个存储数据的容器。在InfluxDB中，每个数据库都可以包含多个测量。

测量是InfluxDB中存储数据的基本单位。它类似于关系型数据库中的表格，但是它没有固定的列数和数据类型。每个测量包含多个数据点，每个数据点都有一个时间戳、零个或多个标签和零个或多个字段。

标签是用于标识数据点的元数据，类似于关系型数据库中的索引。标签是键值对的形式，例如“host”：“server01”，它们通常用于过滤和聚合数据。

字段是数据点的实际数据，它们可以是任意类型的。例如，一个字段可以是一个整数、浮点数、字符串或布尔值。

时间戳是数据点的时间信息，它通常是一个Unix时间戳（以秒为单位），但也可以使用其他格式。时间戳是InfluxDB中唯一必需的元素。



### 安装

https://jasper-zhang1.gitbooks.io/influxdb/content/Introduction/installation.html

helm + k8s安装

```
helm install influxdb influxdata/influxdb --set service.main.ports.http.port=9096

set 修改host端口映射
修改无效？端口8088端口不知道为什么被占用了
```

docker安装：

```
docker run -d -p 8086:9096 --name influxdb infulxdb:1.8.10-alpine
```





```
D:\Users\taoxu.xu>kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)             AGE
influxdb     ClusterIP   10.98.205.23   <none>        8086/TCP,8088/TCP   108s
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP             6d2h
```



官方自从 1.3 版本开始把 web 界面取消了

- TCP端口`8086`用作InfluxDB的客户端和服务端的http api通信
- TCP端口`8088`给备份和恢复数据的RPC服务使用

InfluxDB使用服务器本地时间给数据加时间戳，而且是UTC时区的。并使用NTP来同步服务器之间的时间，如果服务器的时钟没有通过NTP同步，那么写入InfluxDB的数据的时间戳就可能不准确。

### 入门指南

`influx`这个命令行工具，这个工具包含在InfluxDB的安装包里，是一个操作数据库的轻量级工具。它直接通过InfluxDB的HTTP接口(如果没有修改，默认是8086)来和InfluxDB通信。

说明：也可以直接发送裸的HTTP请求来操作数据库，例如`curl`



`_internal`数据库是用来存储InfluxDB内部的实时监控数据的



InfluxDB里存储的数据被称为`时间序列数据`，其包含一个数值，就像CPU的load值或是温度值类似的。时序数据有零个或多个数据点，每一个都是一个指标值。数据点包括`time`(一个时间戳)，`measurement`(例如cpu_load)，至少一个k-v格式的`field`(也即指标的数值例如 “value=0.64”或者“temperature=21.2”)，零个或多个`tag`，其一般是对于这个指标值的元数据(例如“host=server01”, “region=EMEA”, “dc=Frankfurt)。

可以将`measurement`类比于SQL里面的table，其主键索引总是时间戳。`tag`和`field`是在table里的其他列，`tag`是被索引起来的，`field`没有。不同之处在于，在InfluxDB里，你可以有几百万的measurements，你不用事先定义数据的scheme，并且null值不会被存储。



#### 写入

将数据点写入InfluxDB，只需要遵守如下的行协议：

```
<measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]
```

下面是数据写入InfluxDB的格式示例：

```
cpu,host=serverA,region=us_west value=0.64
payment,device=mobile,product=Notepad,method=credit billed=33,licenses=3i 1434067467100293230
stock,symbol=AAPL bid=127.46,ask=127.48
temperature,machine=unit42,type=assembly external=25,internal=37 1434067467000000000
```

插入单条的时间序列数据:

```
INSERT cpu,host=serverA,region=us_west value=0.64

insert stock,type=sh open=1,close=2 1623288483000000000
type: tag
openclose: field value
ts
```

这样一个measurement为`cpu`，tag是`host`和`region`，`value`值为`0.64`的数据点被写入了InfluxDB中

我们在写入的时候没有包含时间戳，当没有带时间戳的时候，InfluxDB会自动添加本地的当前时间作为它的时间戳。



导入文本文件



```
TXT格式：measurement,tag1=value1,tag2=value2 field1=value1,field2=value2 timestamp


influx -import -path=/path/to/your/datafile.lp -precision=ns -host=http://localhost:8086 -database=your_database
```

- `-import`: 标识这是一个导入操作。
- `-path`: 指定要导入的文件的路径。
- `-precision`: 指定导入数据的时间精度（例如，`ns`代表纳秒）。
- `-host`: 指定InfluxDB服务器的地址。
- `-database`: 指定要导入数据的数据库名称。





influx -import -path=/home/stock_data/stock.txt -precision=ns -host=http://localhost:8086 -database=stock



influx -import -path=/home/stock_data/stock.txt -precision=ns -host=https://localhost:8086 -database=stock

influx -import -path=/home/stock_data/stock.txt -precision=ns -database=stock













