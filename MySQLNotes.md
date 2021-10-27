# MySQL Notes

## SQL

### DML

**数据操纵语言**（Data Manipulation Language, DML）

select

insert

update: update tb set a =b

delete： delete from table where

### DDL

Data Definition Language 数据定义语言

- create 
- drop
- truncate: 清空数据，保存结构，比delete from性能高
- rename: rename table a to b
- alter
  - add: alter table a add column city varchar
  - modify/change: 
  - drop



### DCL

控制语言

DBA的职责

### 显示建表语句

>  show create table book\G

```sql
show create table book\G
***************************[ 1. row ]***************************
Table        | book
Create Table | CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `book_name` varchar(128) COLLATE utf8_bin NOT NULL,
  `pages` int(11) NOT NULL,
  `price` int(11) NOT NULL DEFAULT '0',
  `press` varchar(256) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `book_id_UNIQUE` (`book_id`),
  KEY `book_index` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin
```

### delete vs. truncate

delete

### upsert

- upsert(update or insert), 即更新或写入。
- MySQL中实现upsert操作方式：
  思路：通过判断插入的记录里是否存在主键索引或唯一索引冲突，来决定是插入还是更新。当出现主键索引或唯一索引冲突时则进行update操作，否则进行insert操作。
  实现：使用 ON DUPLICATE KEY UPDATE

```sql
insert into demo(a,b,c,d,e,f) values(1,1,1,2,2,2) ON DUPLICATE KEY UPDATE a=2,b=2,c=3,d=4,e=5,f=6;
-- 因为已经存在由abc三列组成唯一索引数据：1，1，1，本次又写入demo(a,b,c,d,e,f) values(1,1,1,2,2,2)，会造成唯一索引冲突。因此，会触发ON DUPLICATE KEY 后面的 UPDATE a=2,b=2,c=3,d=4,e=5,f=6操作。
```





## 主键 外键



### 外键

> 以前对外键的理解有误，外键是一种约束，需要通过语句添加

由于一个班级可以有多个学生，在关系模型中，这两个表的关系可以称为“一对多”，即一个`classes`的记录可以对应多个`students`表的记录。

为了表达这种一对多的关系，我们需要在`students`表中加入一列`class_id`，让它的值与`classes`表的某条记录相对应：

这样，我们就可以根据`class_id`这个列直接定位出一个`students`表的记录应该对应到`classes`的哪条记录。

在`students`表中，通过`class_id`的字段，可以把数据与另一张表关联起来，这种列称为`外键`。



**外键并不是通过列名实现的，而是通过定义外键约束实现的**：

```sql
ALTER TABLE students
ADD CONSTRAINT fk_class_id
FOREIGN KEY (class_id)
REFERENCES classes (id);
```

其中，外键约束的名称`fk_class_id`可以任意，`FOREIGN KEY (class_id)`指定了`class_id`作为外键，`REFERENCES classes (id)`指定了这个外键将关联到`classes`表的`id`列（即`classes`表的主键）。

**通过定义外键约束，关系数据库可以保证无法插入无效的数据。即如果`classes`表不存在`id=99`的记录，`students`表就无法插入`class_id=99`的记录。**

由于外键约束会降低数据库的性能，大部分互联网应用程序为了追求速度，并不设置外键约束，而是仅靠应用程序自身来保证逻辑的正确性。这种情况下，`class_id`仅仅是一个普通的列，只是它起到了外键的作用而已。

要删除一个外键约束，也是通过`ALTER TABLE`实现的：

```sql
ALTER TABLE students
DROP FOREIGN KEY fk_class_id;

# 注意：删除外键约束并没有删除外键这一列。删除列是通过DROP COLUMN ...实现的。
```

## 索引

- 主键索引(聚簇索引)
- 唯一索引 非唯一索引
- 单列索引  组合索引
- 全文索引

### 索引选择性

索引的选择性，指的是不重复的索引值（基数）和表记录数的比值。选择性是索引筛选能力的一个指标。索引的取值范围是 0—1 ，当选择性越大，索引价值也就越大。

举例说明：假如有一张表格，总共有一万行的记录，其中有一个性别列sex，这个列的包含选项就两个：男/女。那么，这个时候，这一列创建索引的话，索引的选择性为万分之二，这时候，在性别这一列创建索引是没有啥意义的。假设个极端情况，列内的数据都是女，那么索引的选择性为万分之一，其效率还不如直接进行全表扫描。如果是主键索引的话，那么选择性为1，索引价值比较大。可以直接根据索引定位到数据。

索引选择性 = 基数 / 总行数 

　　举例：有个学校表 school ,学校名称 school_nick 的索引选择性为： 

```SELECT COUNT(DISTINCT(school_nick))/COUNT(id) AS Selectivity FROM school; ```

### 覆盖索引

覆盖索引是select的数据列只用从索引中就能够取得，不必读取数据行，换句话说查询列要被所建的索引覆盖。



覆盖索引必须要存储索引列的值，而哈希索引、空间索引和全文索引不存储索引列的值，所以mysql只能用B-tree索引做覆盖索引。



### 索引原理

B+Tree

![image-20210722190626182](MySQLNotes.assets/image-20210722190626182.png)

### 索引类型

- 聚簇索引
- 非聚簇索引/辅助索引， 二级索引---**回表**



- 单列索引

  ![image-20210722190852035](MySQLNotes.assets/image-20210722190852035.png)

- 联合索引

  ![image-20210722190910783](MySQLNotes.assets/image-20210722190910783.png)

- 覆盖索引

- 

### 索引失效

![image-20210722191607383](MySQLNotes.assets/image-20210722191607383.png)

注意： 

- join字段/字符集不一致
- 扫描全表20%（非确定值）
- 聚合函数
- like

### 不同数据类型的索引性能差别

索引的性能好坏，主要是由建立索引字段的数据的分散程度决定，与字段类型无关。如果是完全相同的数据内容，int理论上性能略好，但是实际差异不可能体现出来。

？？？

这是错的吧，int索引应该在性能上好









## 数据类型

![image-20210722180005728](MySQLNotes.assets/image-20210722180005728.png)

![image-20210722180750671](MySQLNotes.assets/image-20210722180750671.png)



### char

如何存储的？



### varchar

当长度<=255时，使用一个字节来记录长度，超过255后使用两个字节来记录



如何存储的？



char vs varchar



### Text

长字符串

以字节为单位，注意 和varchar/char不同的。

- `TEXT`：65,535 bytes，64kb；
- `MEDIUMTEXT`：16,777,215bytes，16Mb；
- `LONGTEXT`：4,294,967,295 bytes，4Gb；

#### VARCHAR和TEXT

- VARCHAR中的VAR表示您可以将最大大小设置为1到65,535之间的任何值。 TEXT字段的最大固定大小为65,535个字符。
- VARCHAR可以是索引的一部分，而TEXT字段要求您指定前缀长度，该长度可以是索引的一部分。
- VARCHAR与表内联存储（至少对于MyISAM存储引擎而言），因此在大小合理时可能会更快。当然，快得多少取决于您的数据和硬件。同时，**TEXT存储在表外，该表具有指向实际存储位置的指针。**
- 排序使用TEXT列将需要使用基于磁盘的临时表作为MEMORY（HEAP）存储引擎。



### Blob

二进制

可以存储文件等



### 字符字节

不同的编码下，每个字符最多占多少字节

#### uft8

占2个字节的：带有附加符号的拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文及它拿字母则需要二个字节编码

占3个字节的：基本等同于GBK，含21000多个汉字

最多三字节？？？

#### utf8mb4 

是utf-8的超集，一个字符最多4字节



### 时间日期

![image-20210722181041562](MySQLNotes.assets/image-20210722181041562.png)

#### DATETIME VS. TIMESTAMP

- 区别1：存储方式不一样

  **对于TIMESTAMP，它把客户端插入的时间从当前时区转化为UTC（世界标准时间）进行存储。查询时，将其又转化为客户端当前时区进行返回。**

  **而对于DATETIME，不做任何改变，基本上是原样输入和输出。**

  

  所以说DATETIME数据，插入和获取不会有任何区别。

  但是对于TIMESTAMP，如果插入后更改了时区，那么select后将会转化为当前时区，和原来insert的时间有差别，差别就是两个时区的时差。

- 区别2：存储的时间范围不一样

  timestamp所能存储的时间范围为：'1970-01-01 00:00:01.000000' 到 '2038-01-19 03:14:07.999999'。 **2038年，快了**

  datetime所能存储的时间范围为：'1000-01-01 00:00:00.000000' 到 '9999-12-31 23:59:59.999999'。

- 区别3： 存储大小不同

  TIMESTAMP只需要4字节，而DATETIME需要8字节
  
  





### 编码

在mysql中存在着各种utf8编码格式，如下(**新建数据库时一般选用utf8_general_ci就可以**)：
utf8_bin:将字符串中的**每一个字符用二进制数据存储**，区分大小写(在二进制中 ,小写字母 和大写字母 不相等.即 a !=A)。
**utf8_genera_ci:不区分大小写，ci为case insensitive的缩写**（insensitive ; 中文解释: adj. 感觉迟钝的，对…没有感觉的），即大小写不敏感。
utf8_general_cs:区分大小写，cs为case sensitive的缩写（sensitive 中文解释:敏感事件;大小写敏感;注重大小写;全字拼写须符合），即大小写敏感
utf8_unicode_ci:不能完全支持组合的记号。











## 存储引擎

![image-20210722175130741](MySQLNotes.assets/image-20210722175130741.png)

MySQL是**单进程多线程**模式

<img src="MySQLNotes.assets/image-20210722175300978.png" alt="image-20210722175300978" style="zoom:150%;" />



```sql
show engines
```

![image-20210722175604844](MySQLNotes.assets/image-20210722175604844.png)

### InnoDB



### MyISAM





## 权限管理

![image-20210722182511072](MySQLNotes.assets/image-20210722182511072.png)

![image-20210722182559332](MySQLNotes.assets/image-20210722182559332.png)

![image-20210722182623472](MySQLNotes.assets/image-20210722182623472.png)

![image-20210722182722519](MySQLNotes.assets/image-20210722182722519.png)

![image-20210722182747687](MySQLNotes.assets/image-20210722182747687.png)

![image-20210722182901769](MySQLNotes.assets/image-20210722182901769.png)



## 系统命令

![image-20210722183146171](MySQLNotes.assets/image-20210722183146171.png)

\G :按列显示



```sql
# 查看表
show tables like '%s%'
# 查看表定义
show create table tb
# 查看数据库定义
show create database db
# 查看表数据、索引所占空间、平均行长、行数等
show table status like 'xxx'\G
# 查看索引
show index from tb\G

# 查看列信息
show columns from tb

```



#### set

![image-20210722183939045](MySQLNotes.assets/image-20210722183939045.png)



## 高可用

### Master-Slave

 ![image-20210722184449153](MySQLNotes.assets/image-20210722184449153.png)

异步复制出现了

### Binlog   & Relay Log

![image-20210722184532691](MySQLNotes.assets/image-20210722184532691.png)

![image-20210722184601468](MySQLNotes.assets/image-20210722184601468.png)

提交顺序



GTID

![image-20210722184722516](MySQLNotes.assets/image-20210722184722516.png)



### 3M架构

MMM

**Master-Master Replication** for mysql

MySQL主主复制管理器

**是一套双主 故障切换 和 双主日常管理 的脚本程序**

MMM使用Perl开发，主要用来管理MySQL master-master双主复制。(虽然叫双主，但是业务上同一时刻只允许一个Master进行写入，另一台备选主提供部分读服务，以加速在主主切换是备选主的预热)



应用场景：

MMM提供了自动和手动两种方式移除一组服务器中复制延迟较高的服务器的虚拟ip，同时它还可以备份数据，实现两节点之间的数据同步等。由于MMM无法完全保证数据的一致性，所以MMM适用于对数据的一致性要求不是很高的，但是又想最大程度地保证业务可用性的场景。对于那些对数据的一致性要求很高的业务，非常不建议采用MMM这种高可用架构。

![image-20211022151708201](MySQLNotes.assets/image-20211022151708201.png)



mysql-mmm的组成以及原理

三个脚本：
mmm_mond:
 监控进程，负责所有的监控工作，决定和处理所有节点角色活动。此脚本需要在监管机上运行。
mmm_agentd:
 运行在每个mysql服务器上的代理进程，完成监控的探针工作，执行简单的远端服务设置，此脚本需要在被监管机器上运行。
mmm_control:
 提供管理mmm_mond进程的命令。



### 3M,QMHA,PXC架构的mysql









## 规范

### QUNAR规范

主键没有业务意义，是unsigned的

每个列必须有注释

使用utf8mb4



![image-20210722184914325](MySQLNotes.assets/image-20210722184914325.png)

![image-20210722184946174](MySQLNotes.assets/image-20210722184946174.png)

![image-20210722185011528](MySQLNotes.assets/image-20210722185011528.png)



![image-20210722185053263](MySQLNotes.assets/image-20210722185053263.png)



![image-20210722185157402](MySQLNotes.assets/image-20210722185157402.png)

![image-20210722185218120](MySQLNotes.assets/image-20210722185218120.png)

![image-20210722185353899](MySQLNotes.assets/image-20210722185353899.png)

![image-20210722185444711](MySQLNotes.assets/image-20210722185444711.png)

![image-20210722185639030](MySQLNotes.assets/image-20210722185639030.png)

![image-20210722185743143](MySQLNotes.assets/image-20210722185743143.png)







## 数据库设计

### 数据库表字段设计

![image-20210722190012648](MySQLNotes.assets/image-20210722190012648.png)

![image-20210722190026274](MySQLNotes.assets/image-20210722190026274.png)



![image-20210722190147349](MySQLNotes.assets/image-20210722190147349.png)



![image-20210722190219506](MySQLNotes.assets/image-20210722190219506.png)

Timestamp是从1960年开始？datetime从1000



禁止：

![image-20210722190335468](MySQLNotes.assets/image-20210722190335468.png)



### 范式

- 1NF：列的原子性
- 2NF：在1NF基础上，非码属性必须完全依赖于候选码（在1NF基础上消除非主属性对主码的部分函数依赖）
- 3NF：在2NF的基础上，任何的非主属性不依赖于其他非主属性 （在第二范式基础上消除传递依赖）

## SQL 优化

### explain执行计划

![image-20210722192334704](MySQLNotes.assets/image-20210722192334704.png)

![image-20210722192311898](MySQLNotes.assets/image-20210722192311898.png)

![image-20210722192511872](MySQLNotes.assets/image-20210722192511872.png)

![image-20210722192638277](MySQLNotes.assets/image-20210722192638277.png)

![image-20210722192756930](MySQLNotes.assets/image-20210722192756930.png)

![image-20210722193046210](MySQLNotes.assets/image-20210722193046210.png)











### 正确使用索引：

![image-20210722193148494](MySQLNotes.assets/image-20210722193148494.png)

join两边都加

![image-20210722193254221](MySQLNotes.assets/image-20210722193254221.png)

![image-20210722193340798](MySQLNotes.assets/image-20210722193340798.png)

![image-20210722193457423](MySQLNotes.assets/image-20210722193457423.png)

![image-20210722193600003](MySQLNotes.assets/image-20210722193600003.png)

尽量利用覆盖索引



### 避免Bad SQL

![image-20210722193813981](MySQLNotes.assets/image-20210722193813981.png)

![image-20210722193850346](MySQLNotes.assets/image-20210722193850346.png)

![image-20210722193930750](MySQLNotes.assets/image-20210722193930750.png)



## 性能优化

- 参数优化
  - 内存相关
    - innode_buffer_pool_size
    - innode_log_buffer_size
    - sort_buffer_size
  - io相关
    - sync_binlog
- SQL优化
  - SQL优化
    - 选取最少的满足需求的数据
    - 执行之前explain查看执行计划，扫描行数尽可能少
    - 利用好索引
    - 避免出现索引失效：隐式转换，最左前缀，聚合函数，20%(MySQL不确定，非确值)
  - SQL改写
- 其他优化
  - in
    - 控制in后面只能接常量，长度一般不超过200
    - **in后面不能接子查询**
  - 不等于： not in ,  !=, <>
  - 前缀模糊查询
  - 尽可能使用count(*)： **count( *) 不同于列，有特殊机制**
  - limit



## 日常操作数据库要求

![image-20210722194149641](MySQLNotes.assets/image-20210722194149641.png)

![image-20210722194209053](MySQLNotes.assets/image-20210722194209053.png)





![image-20210722194319202](MySQLNotes.assets/image-20210722194319202.png)





QUNAR操作没看完







## 原理分析篇

### 数据库的存储

查看数据表的存储目录：

```sql
show variables like '%datadir%';
Variable_name | datadir
Value         | /var/lib/mysql/
```

```bash
root@VM-16-11-ubuntu:/var/lib/mysql# ll
total 188488
drwx------  8 mysql mysql     4096 Jul 22 10:53 ./
drwxr-xr-x 51 root  root      4096 Apr 25 22:03 ../
-rw-r-----  1 mysql mysql       56 Mar  9 17:00 auto.cnf
-rw-------  1 mysql mysql     1676 Mar  9 17:00 ca-key.pem
-rw-r--r--  1 mysql mysql     1112 Mar  9 17:00 ca.pem
-rw-r--r--  1 mysql mysql     1112 Mar  9 17:00 client-cert.pem
-rw-------  1 mysql mysql     1676 Mar  9 17:00 client-key.pem
-rw-r--r--  1 root  root         0 Mar  9 17:00 debian-5.7.flag
-rw-r-----  1 mysql mysql     2474 Mar 24 22:29 ib_buffer_pool
-rw-r-----  1 mysql mysql 79691776 Jul 22 16:43 ibdata1
-rw-r-----  1 mysql mysql 50331648 Jul 22 16:43 ib_logfile0
-rw-r-----  1 mysql mysql 50331648 Mar  9 17:00 ib_logfile1
-rw-r-----  1 mysql mysql 12582912 Jul 23 10:13 ibtmp1
drwxr-x---  2 mysql mysql     4096 Jul 23 10:01 mysql/
drwxr-x---  2 mysql mysql     4096 Jul 22 16:42 MySQL/
drwxr-x---  2 mysql mysql     4096 May 24 15:59 oauth2_server/
drwxr-x---  2 mysql mysql     4096 Mar  9 17:00 performance_schema/
-rw-------  1 mysql mysql     1680 Mar  9 17:00 private_key.pem
-rw-r--r--  1 mysql mysql      452 Mar  9 17:00 public_key.pem
drwxr-x---  2 mysql mysql     4096 May 19 23:05 readme/
-rw-r--r--  1 mysql mysql     1112 Mar  9 17:00 server-cert.pem
-rw-------  1 mysql mysql     1676 Mar  9 17:00 server-key.pem
drwxr-x---  2 mysql mysql     4096 May 31 00:38 world/
```

建一个数据库test01，并使用不同引擎建表

```sql
create DATABASE test01
# datadir中新出现了一个目录test01，表明一个数据库对应一个目录

# 创建一个innodb作为引擎的表
CREATE TABLE `innodb_tb01` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `book_name` varchar(128) COLLATE utf8_bin NOT NULL,
  `pages` int(11) NOT NULL,
  `price` int(11) NOT NULL DEFAULT '0',
  `press` varchar(256) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `book_id_UNIQUE` (`book_id`),
  KEY `book_index` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin
# 然后test01下出现几个文件
-rw-r----- 1 mysql mysql     65 Jul 23 10:31 db.opt
-rw-r----- 1 mysql mysql   8728 Jul 23 10:34 innodb_tb01.frm
-rw-r----- 1 mysql mysql 131072 Jul 23 10:34 innodb_tb01.ibd
# 删除表，还剩下db.opt
cat db.opt
default-character-set=latin1
default-collation=latin1_swedish_ci
# 表明db.opt是配置文件


### 在建一个MyISAM表
CREATE TABLE `myisam_tb01` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `book_name` varchar(128) COLLATE utf8_bin NOT NULL,
  `pages` int(11) NOT NULL,
  `price` int(11) NOT NULL DEFAULT '0',
  `press` varchar(256) COLLATE utf8_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `book_id_UNIQUE` (`book_id`),
  KEY `book_index` (`book_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin
# 新出现三个文件：.frm .MYD .MYI
-rw-r----- 1 mysql mysql   8728 Jul 23 10:43 myisam_tb01.frm
-rw-r----- 1 mysql mysql      0 Jul 23 10:43 myisam_tb01.MYD
-rw-r----- 1 mysql mysql   1024 Jul 23 10:43 myisam_tb01.MYI

# 两种数据引擎都有 .frm文件
```

- **在MyISAM引擎下：**
  - **.frm: 表结构文件，描述表定义**
  - **.MYD: 表数据文件**
  - **.MYI: 表索引文件**

- **在InnoDB引擎下：**
  - **.frm：同样是表结构文件**
  - **.idb: 表数据和索引文件。该表的索引(B+树)的每个非叶子节点存储索引，叶子节点存储索引和索引对应的数据。**





## 常见错误

### 字段类型隐式转换



### NULL值的问题

不使用 == <>

使用is , is not







## 一些问题

### 版本区别

mysql5.6 mysql5.7 mysql8.0 是大家目前使用最多的版本

- 在mysql 5.7之后，mysql group by的默认使用增加了限制，一些在mysql5.6可以执行的group by，在5.7 之后会报错
- JDBC驱动：高版本的默认jdbc驱动类从 com.mysql.jdbc.Driver 改成 com.mysql.cj.jdbc.Driver

### count(*) vs. count(field) vs.count(1)

如果field是主键

三者是一样的，都是利用主键做全表扫描。

需要注意的是*还需要解析，这是一点额外的消耗

```sql
mysql root@localhost:oauth2_server> explain select COUNT(*) from login_history_entity\G
***************************[ 1. row ]***************************
id            | 1
select_type   | SIMPLE
table         | login_history_entity
partitions    | None
type          | index
possible_keys | None
key           | index_username
key_len       | 122
ref           | None
rows          | 185
filtered      | 100.00
Extra         | Using index

1 row in set
Time: 0.003s
mysql root@localhost:oauth2_server> explain select COUNT(id) from login_history_entity\G
***************************[ 1. row ]***************************
id            | 1
select_type   | SIMPLE
table         | login_history_entity
partitions    | None
type          | index
possible_keys | None
key           | index_username
key_len       | 122
ref           | None
rows          | 185
filtered      | 100.00
Extra         | Using index

1 row in set
Time: 0.003s
mysql root@localhost:oauth2_server> explain select COUNT(1) from login_history_entity\G
***************************[ 1. row ]***************************
id            | 1
select_type   | SIMPLE
table         | login_history_entity
partitions    | None
type          | index
possible_keys | None
key           | index_username
key_len       | 122
ref           | None
rows          | 185
filtered      | 100.00
Extra         | Using index
```

Filed为非主键是则是直接全表扫描, 效率要差

```sql
mysql root@localhost:oauth2_server> explain select COUNT(device) from login_history_entity\G
***************************[ 1. row ]***************************
id            | 1
select_type   | SIMPLE
table         | login_history_entity
partitions    | None
type          | ALL
possible_keys | None
key           | None
key_len       | None
ref           | None
rows          | 185
filtered      | 100.00
Extra         | None
```







limit 2 offset 100

偏移100后的2两条

注意不是2行后的100条







