# Hadoop Notes

[01_尚硅谷大数据技术之大数据概论](_pdf/bigdata/hadoop/01_尚硅谷大数据技术之大数据概论.pdf)

[02_尚硅谷大数据技术之Hadoop_入门V3.3](_pdf/bigdata/hadoop/02_尚硅谷大数据技术之Hadoop_入门V3.3.pdf)

[03_尚硅谷大数据技术之Hadoop_HDFS_V3.3](_pdf/bigdata/hadoop/03_尚硅谷大数据技术之Hadoop_HDFS_V3.3.pdf)

[04_尚硅谷大数据技术之Hadoop_MapReduce_V3.3](_pdf/bigdata/hadoop/04_尚硅谷大数据技术之Hadoop_MapReduce_V3.3.pdf)

[05_尚硅谷大数据技术之Hadoop_Yarn_V3.3](_pdf/bigdata/hadoop/05_尚硅谷大数据技术之Hadoop_Yarn_V3.3.pdf)

[06_尚硅谷大数据技术之Hadoop_生产调优手册_V3.3](_pdf/bigdata/hadoop/06_尚硅谷大数据技术之Hadoop_生产调优手册_V3.3.pdf)

[07_尚硅谷大数据技术之Hadoop_源码解析_V3.3](_pdf/bigdata/hadoop/07_尚硅谷大数据技术之Hadoop_源码解析_V3.3.pdf)



## My Hadoop Notes

### MR

#### MR 原理

![image-20211109101833628](_images/HadoopNotes.assets/image-20211109101833628.png)

1. 在client启动一个作业
2. 向JOBTracker请求一个JOB ID
3. 将运行作业所需额资源文件复制到HDFS上：包括MR程序jar、配置文件、客户端计算所得的输入划分信息。这些file都存在job tracker专门为该作业创建的目录中，目录名为job id，jar文件默认有10个副本（mapred.submit.replication属性控制），输入划分信息告诉job tracker应该为这个作业启动多少个map任务等信息。
4. job tracker接收到作业后将其放在一个作业队列中，等待作业调度器调度。作业被调度时，会根据输入划分信息为每一个划分创建一个map任务，并将map任务分配给task tracker执行，对于map和reduce任务，task tracker根据主机核的数量和内存的大小，有固定的map槽和reduce槽。 注意毛不是随便分配给某个task tracker的，有个概念叫“**数据本地化DataLocal**”，意思是将毛任务分配给含有该map处理的数据块的task tracker上，同时将jar复制到该task tracker---“**运算移动，数据不移动**”，这样不需要传输数据，但是对于reduce任务，则不需要考虑数据本地化，因为map的输出不可避免地需要传输到reduce任务。
5. task tracker通过心跳机制想job tracker汇报：运行状态、进度

![image-20211109103817517](_images/HadoopNotes.assets/image-20211109103817517.png)

#### 过程

map阶段：

就是程序员编写好的map函数了，因此map函数效率相对好控制，而且一般map操作都是本地化操作也就是在数据存储节点上进行；

combiner阶段是程序员可以选择的，combiner其实也是一种reduce操作，因此我们看见WordCount类里是用reduce进行加载的。Combiner是一个本地化的reduce操作，它是map运算的后续操作，主要是在map计算出中间文件前做一个简单的合并重复key值的操作，例如我们对文件里的单词频率做统计，map计算时候如果碰到一个hadoop的单词就会记录为1，但是这篇文章里hadoop可能会出现n多次，那么map输出文件冗余就会很多，因此在reduce计算前对相同的key做一个合并操作，那么文件会变小，这样就提高了宽带的传输效率，毕竟hadoop计算力宽带资源往往是计算的瓶颈也是最为宝贵的资源，但是combiner操作是有风险的，使用它的原则是combiner的输入不会影响到reduce计算的最终输入，例如：如果计算只是求总数，最大值，最小值可以使用combiner，但是做平均值计算使用combiner的话，最终的reduce计算结果就会出错。

###### shuffle阶段：

将map的输出作为reduce的输入的过程就是shuffle了，这个是mapreduce优化的重点地方。这里我不讲怎么优化shuffle阶段，讲讲shuffle阶段的原理，因为大部分的书籍里都没讲清楚shuffle阶段。Shuffle一开始就是map阶段做输出操作，一般mapreduce计算的都是海量数据，map输出时候不可能把所有文件都放到内存操作，因此map写入磁盘的过程十分的复杂，更何况map输出时候要对结果进行排序，内存开销是很大的，map在做输出时候会在内存里开启一个环形内存缓冲区，这个缓冲区专门用来输出的，默认大小是100mb，并且在配置文件里为这个缓冲区设定了一个阀值，默认是0.80（这个大小和阀值都是可以在配置文件里进行配置的），同时map还会为输出操作启动一个守护线程，如果缓冲区的内存达到了阀值的80%时候，这个守护线程就会把内容写到磁盘上，这个过程叫spill，另外的20%内存可以继续写入要写进磁盘的数据，写入磁盘和写入内存操作是互不干扰的，如果缓存区被撑满了，那么map就会阻塞写入内存的操作，让写入磁盘操作完成后再继续执行写入内存操作，前面我讲到写入磁盘前会有个排序操作，这个是在写入磁盘操作时候进行，不是在写入内存时候进行的，如果我们定义了combiner函数，那么排序前还会执行combiner操作。每次spill操作也就是写入磁盘操作时候就会写一个溢出文件，也就是说在做map输出有几次spill就会产生多少个溢出文件，等map输出全部做完后，map会合并这些输出文件。这个过程里还会有一个Partitioner操作，对于这个操作很多人都很迷糊，其实Partitioner操作和map阶段的输入分片（Input split）很像，一个Partitioner对应一个reduce作业，如果我们mapreduce操作只有一个reduce操作，那么Partitioner就只有一个，如果我们有多个reduce操作，那么Partitioner对应的就会有多个，Partitioner因此就是reduce的输入分片，这个程序员可以编程控制，主要是根据实际key和value的值，根据实际业务类型或者为了更好的reduce负载均衡要求进行，这是提高reduce效率的一个关键所在。到了reduce阶段就是合并map输出文件了，Partitioner会找到对应的map输出文件，然后进行复制操作，复制操作时reduce会开启几个复制线程，这些线程默认个数是5个，程序员也可以在配置文件更改复制线程的个数，这个复制过程和map写入磁盘过程类似，也有阀值和内存大小，阀值一样可以在配置文件里配置，而内存大小是直接使用reduce的tasktracker的内存大小，复制时候reduce还会进行排序操作和合并文件操作，这些操作完了就会进行reduce计算了。

###### reduce阶段：

和map函数一样也是程序员编写的，最终结果是存储在hdfs上的。

输入 --> map --> shuffle --> reduce -->输出



**Partitioner:数据分组 决定了Map task输出的每条数据交给哪个Reduce Task处理。默认实现：hash(key) mod R R是Reduce Task数目，允许用户自定义，很多情况下需要自定义Partitioner ，比如“hash(hostname(URL)) mod R”确保相同域名的网页交给同一个Reduce Task处理 属于（map）阶段。**

Combiner：可以看做local reduce  合并相同的key对应的value，通常与reducer逻辑一样 ，好处是减少map task输出 数量（磁盘IO），减少Reduce-map网络传输数据量(网络IO) 结果叠加属于（map）阶段。

Shuffle：Shuffle描述着数据从map task输出到reduce task输入的这段过程 (完整地从map task端拉取数据到reduce 端。
 在跨节点拉取数据时，尽可能地减少对带宽的不必要消耗。减少磁盘IO对task执行的影响。) 属于(reduce)阶段。

















# Notes From Video

https://ke.qq.com/course/3030492?taid=10164911987375580

## 大数据概况及Hadoop

### 大数据

大数据是一个描述大量告诉复杂和可变数据的术语，需要先进的技术来实现信息的获取、存储、分发、管理和分析

![image-20210901180316313](_images/HadoopNotes.assets/image-20210901180316313.png)

- volume 体量大
- velocity 处理速度快
- variety：种类繁多：结构化 半结构化 非结构化
- value：价值密度低

![image-20210901181450607](_images/HadoopNotes.assets/image-20210901181450607.png)

### Hadoop概述

![image-20210901181600509](_images/HadoopNotes.assets/image-20210901181600509.png)

http://hadoop.apache.org/

![image-20210901182253475](_images/HadoopNotes.assets/image-20210901182253475.png)

![image-20210901182308609](_images/HadoopNotes.assets/image-20210901182308609.png)



## Hadoop

```text
一、Hadoop入门
	1、常用端口号
	hadoop3.x 
		HDFS NameNode 内部通常端口：8020/9000/9820
		HDFS NameNode 对用户的查询端口：9870
		Yarn查看任务运行情况的：8088
		历史服务器：19888
	hadoop2.x 
		HDFS NameNode 内部通常端口：8020/9000
		HDFS NameNode 对用户的查询端口：50070
		Yarn查看任务运行情况的：8088
		历史服务器：19888
	2、常用的配置文件
	3.x core-site.xml  hdfs-site.xml  yarn-site.xml  mapred-site.xml workers
	2.x core-site.xml  hdfs-site.xml  yarn-site.xml  mapred-site.xml slaves
	
二、HDFS
	1、HDFS文件块大小（面试重点）
		硬盘读写速度
		在企业中  一般128m（中小公司）   256m （大公司）
	2、HDFS的Shell操作（开发重点）
	3、HDFS的读写流程（面试重点）
三、Map Reduce
	1、InputFormat
		1）默认的是TextInputformat  kv  key偏移量，v :一行内容
		2）处理小文件CombineTextInputFormat 把多个文件合并到一起统一切片
	2、Mapper 
		setup()初始化；  map()用户的业务逻辑； clearup() 关闭资源；
	3、分区
		默认分区HashPartitioner ，默认按照key的hash值%numreducetask个数
		自定义分区
	4、排序
		1）部分排序  每个输出的文件内部有序。
		2）全排序：  一个reduce ,对所有数据大排序。
		3）二次排序：  自定义排序范畴， 实现 writableCompare接口， 重写compareTo方法
			总流量倒序  按照上行流量 正序
	5、Combiner 
		前提：不影响最终的业务逻辑（求和 没问题   求平均值）
		提前聚合map  => 解决数据倾斜的一个方法
	6、Reducer
		用户的业务逻辑；
		setup()初始化；reduce()用户的业务逻辑； clearup() 关闭资源；
	7、OutputFormat
		1）默认TextOutputFormat  按行输出到文件
		2）自定义
四、Yarn
	1、Yarn的工作机制（面试题）
		
	2、Yarn的调度器
		1）FIFO/容量/公平
		2）apache 默认调度器  容量； CDH默认调度器 公平
		3）公平/容量默认一个default ，需要创建多队列
		4）中小企业：hive  spark flink  mr  
		5）中大企业：业务模块：登录/注册/购物车/营销
		6）好处：解耦  降低风险  11.11  6.18  降级使用
		7）每个调度器特点：
			相同点：支持多队列，可以借资源，支持多用户
			不同点：容量调度器：优先满足先进来的任务执行
					公平调度器，在队列里面的任务公平享有队列资源
		8）生产环境怎么选：
			中小企业，对并发度要求不高，选择容量
			中大企业，对并发度要求比较高，选择公平。
	3、开发需要重点掌握：
		1）队列运行原理	
		2）Yarn常用命令
		3）核心参数配置
		4）配置容量调度器和公平调度器。
		5）tool接口使用。
```



### 架构

- common 公共模块

- HDFS 数据存储，分布式

- MapReduce：处理数据的核心框架

- yarn：资源管理器，资源调度，协调管理，2.x是Tez

- ecosystem：生态圈

  ![image-20210901183122534](_images/HadoopNotes.assets/image-20210901183122534.png)

![image-20210901182946090](_images/HadoopNotes.assets/image-20210901182946090.png)

java语言实现的

### install

- 配置jdk
- Hadoop配置
- 



### HDFS role

![image-20210902122626391](_images/HadoopNotes.assets/image-20210902122626391.png)

![image-20210902123424458](_images/HadoopNotes.assets/image-20210902123424458.png)

#### NameNode

NameNode存储元数据，保存数据分为多少块，每一块存放在那些节点上

数据都是存在DataNode节点

https://ke.qq.com/course/3030492?taid=10164942052146652

#### DataNode

![image-20210902123253507](_images/HadoopNotes.assets/image-20210902123253507.png)

### 组件

![image-20210902123531875](_images/HadoopNotes.assets/image-20210902123531875.png)

2.x版本每一个块默认是128MB

避免在HDFS中存储小文件

每个块默认保存三份，用以备份

![image-20210902173248589](_images/HadoopNotes.assets/image-20210902173248589.png)

### MapReduce Engine

![image-20210902173421222](_images/HadoopNotes.assets/image-20210902173421222.png)

![image-20210902173441988](_images/HadoopNotes.assets/image-20210902173441988.png)

## HDFS 读写

![image-20210902173641638](_images/HadoopNotes.assets/image-20210902173641638.png)

![image-20210902174229009](_images/HadoopNotes.assets/image-20210902174229009.png)

### HDFS CLI

![image-20210902182148964](_images/HadoopNotes.assets/image-20210902182148964.png)

hdfs命令有两个：

- hdfs fs：推荐
- hadoop fs: 已经过时了

```bash
# 创建目录
hdfs dfs -mkdir /dir_name 
# 查看目录
hdfs dfs -ls /dir_name
# 上传到HDFS
hdfs dfs -put a.md /dir

要从HDFS中删除文件，可以使用以下命令：

hadoop fs -rm -r -skipTrash /path_to_file/file_name
要从HDFS中删除文件夹，可以使用以下命令：

hadoop fs -rm -r -skipTrash /folder_name
hadoop fs jar MAIN_CLASS a
```

### HDFS java客户端

java 编码



## MapReduce

![image-20210910123833624](_images/HadoopNotes.assets/image-20210910123833624.png)

![image-20210910124308008](_images/HadoopNotes.assets/image-20210910124308008.png)

![image-20210910140709087](_images/HadoopNotes.assets/image-20210910140709087.png)

shuffle

![image-20210910140843379](_images/HadoopNotes.assets/image-20210910140843379.png)

![image-20210910141015158](_images/HadoopNotes.assets/image-20210910141015158.png)

![image-20210910141444557](_images/HadoopNotes.assets/image-20210910141444557.png)

![image-20210910143346888](_images/HadoopNotes.assets/image-20210910143346888.png)

并行计算框架

用户只需要关系map和reduce两个函数

Partition类

### WordCount案例

依赖：

```xml
   <dependencies>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>3.2.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-client</artifactId>
            <version>3.2.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-hdfs</artifactId>
            <version>3.2.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-common</artifactId>
            <version>3.2.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-mapreduce-client-core</artifactId>
            <version>3.2.1</version>
        </dependency>
    </dependencies>
```

mapper reduce job:

```java
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String string = value.toString();
        if (!Strings.isNullOrEmpty(string)){
            String[] strArr = string.trim().split(" +");
            for (String s : strArr) {
                context.write(new Text(s), new IntWritable(1));
            }
        }
    }
}

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        AtomicInteger cnt = new AtomicInteger();
        values.forEach(val -> {
            cnt.addAndGet(val.get());
        });
        context.write(key, new IntWritable(cnt.get()));
    }
}

public class WordCountJob {
    public void countWords(String input , String output){
        try {
            Job job = Job.getInstance();
            job.setJarByClass(WordCountJob.class);

            job.setMapperClass(WordCountMapper.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(IntWritable.class);

            job.setReducerClass(WordCountReducer.class);
            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(IntWritable.class);

            FileInputFormat.setInputPaths(job, new Path(input));
            FileOutputFormat.setOutputPath(job, new Path(output));
            boolean waitForCompletion = job.waitForCompletion(true);
            System.out.println("Count Words " + (waitForCompletion ? "SUCCEEDED." : "FAILED."));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        WordCountJob job = new WordCountJob();
        if (args.length < 2){
            System.out.println("Please input source filepath and target filepath!");
            System.exit(-1);
        }
        job.countWords(args[0], args[1]);
    }
}

```

打包

启动hadoop

上传输入文件

```shell
./hadoop fs -put /home/edwinxu/Desktop/EdwinXu/workspace/hadoop/jars/wordcount/input.txt /wordcount
```



运行jar：

```shell
./hadoop jar /home/edwinxu/Desktop/EdwinXu/workspace/hadoop/jars/wordcount/wordcount.jar cn.edw.bigdata.hadoop.WordCountJob /wordcount/input.txt /wordcount
```





先跳到Hive：

https://ke.qq.com/webcourse/3030492/103148093#taid=10171332963483100&vid=5285890808495683641

## Hive

### 数据仓库

大量的数据汇集到一起

![image-20211024225414290](_images/HadoopNotes.assets/image-20211024225414290.png)

![image-20211024225558557](_images/HadoopNotes.assets/image-20211024225558557.png)

hive将结构化数据映射为一张表

优势：

- 编码简单：HQL
- hive支持不同的运算框架：如spark等



![image-20211024230009791](_images/HadoopNotes.assets/image-20211024230009791.png)



**HQL会翻译成MR然后执行**

Hive实现WordCount：







































# Hadoop官方教程

http://hadoop.apache.org/docs/r1.0.4/cn/index.html

## Hadoop快速入门

编辑 conf/hadoop-env.sh文件，至少需要将JAVA_HOME设置为Java安装根路径。



可以用以下三种支持的模式中的一种启动Hadoop集群：

- 单机模式

- 伪分布式模式

  每一个Hadoop守护进程都作为一个独立的Java进程运行。

  

- 完全分布式模式

# Hadoop权威指南

Tom White著

### 0.序

Google帝国基石？MapReduce算法？

Hadoop起源于Nutch, 后来Tom White成为开发负责人

国内Hadoop人才：邵铮



Internet数据爆炸性增长，传统的技术架构不适合海量数据处理的要求，Hadoop在这样的环境下出现的，Hadoop的出现代表着互联网发展的两个方向：

第一：海量数据处理的广泛应用

第二：开源软件的蓬勃发展



### 1.初始Hadoop

#### 1.1 data

纽约证券交易所每天产生1TB的交易数据

#### 1.2 数据存储和分析

硬盘容量快速增长，访问速度却难以与时俱进

读取速度的问题：从多个磁盘读取数据

硬盘故障问题：复制备份

#### 1.3 相较于其他系统

##### 1.3.1 RDBMS

![image-20210827180501034](_images/HadoopNotes.assets/image-20210827180501034.png)

RDBMS适用于关系型数据库，而MR适合非结构化半结构化数据

##### 1.3.2 网格计算

High Performance Computing/HPC高性能计算和网格计算，做大规模数据处理，他们使用消息传递接口MPI/message passing interface这样的api

##### 1.3.3 志愿计算



#### 1.4 Hadoop发展简史

![image-20210827181721446](_images/HadoopNotes.assets/image-20210827181721446.png)

![image-20210827182106815](_images/HadoopNotes.assets/image-20210827182106815.png)



#### 1.5 Apache Hadoop

虽然Hadoop最出名的是MapReduce以及其分布式文件系统HDFS，但是其还有很多其他子项目：

![image-20210827182216364](_images/HadoopNotes.assets/image-20210827182216364.png)

![image-20210827182418957](_images/HadoopNotes.assets/image-20210827182418957.png)

![image-20210827182442454](_images/HadoopNotes.assets/image-20210827182442454.png)

### 2.MapReduce

![image-20210827183321170](_images/HadoopNotes.assets/image-20210827183321170.png)

![image-20210827183608925](_images/HadoopNotes.assets/image-20210827183608925.png)

#### 2.4 分布化

**MR JOB是执行的单位：包含输入数据、MR程序和配置信息**

**Hadoop通过把作业分成若干个小任务Task来工作：包括map和reduce**

**有两种类型的节点控制着作业执行过程：JOBTracker和多个TaskTracker**

**job tracker通过调度任务在task tracker上执行，来协调所有运行在系统上的作业，task tracker在运行的同时想jobtracker汇报进度**

**jobtracker记录每个任务的执行情况，如果有任务失败则调用其他task执行**

hadoop将数据分片发送给MR，MR为每一个分片创建一个map任务

一个分片往往是一个HDFS块的大小

![image-20211108203210035](_images/HadoopNotes.assets/image-20211108203210035.png)

![image-20211108203349056](_images/HadoopNotes.assets/image-20211108203349056.png)

也有可能是没有Reducer，Map输出后直接写到HDFS



Combiner 可以在map阶段对数据做一些简单的处理，比如求最大值，减少map的输出，提升性能

### 3.分布式文件系统

HDFS：Hadoop Distributed FileSystem

“一次写入，多次读取”思想

#### 块

磁盘有块，以块为单位操作

HDFS也是以块为单元，默认64(高版本128M)，(为什么这么大？最大化磁盘的传输效率，数据传输时间应该远大于磁盘转移时间)

注意：HDFS中没有一个块的文件实际不会占据一个块的物理空间

#### DataNode NameNode

HDFS集群中有两种节点

Namenode维护目录中所有的索引和地址，以及各种元数据

DataNode存储数据，提供定位服务

#### FS

DistributedFileSystem

#### java接口

从Hadoop URL中读取数据

![image-20211108211557058](_images/HadoopNotes.assets/image-20211108211557058.png)

hdfs://host/path/*

FSDataInputStream

FileSystemDoubleCat



目录：

Filestatus



#### 3.6.数据流

![image-20211108212151198](_images/HadoopNotes.assets/image-20211108212151198.png)

节点间通过RPC通信

![image-20211108212342696](_images/HadoopNotes.assets/image-20211108212342696.png)



副本的存放：

![image-20211108213433726](_images/HadoopNotes.assets/image-20211108213433726.png)



#### 归档

Hadoop Archives

### Hadoop IO

数据完整性校验

压缩

![image-20211108214217922](_images/HadoopNotes.assets/image-20211108214217922.png)

编码解码



序列化：

Hadoop使用自己的序列化工具Writables



##### Writeable

![image-20211108215017497](_images/HadoopNotes.assets/image-20211108215017497.png)

















# 实践

## 安装运行

下载Hadoop，解压

使用windows环境需要下载hadoop.dll和winutils.exe

配置：

```xml
# core-site.xml
<configuration>
<property>
      <name>fs.defaultFS</name>
      <value>hdfs://localhost:9000</value>
</property>
</configuration>


# hdfs-site.xml 需要创建相应的目录
<configuration>
<property>
       <name>dfs.replication</name>
       <value>1</value>
   </property>
   <property>
       <name>dfs.namenode.name.dir</name>
       <value>/home/edwinxu/Desktop/EdwinXu/workspace/hadoop/hadoop-2.7.1/data/namenode</value>
   </property>
   <property>
       <name>dfs.datanode.data.dir</name>
     <value>/home/edwinxu/Desktop/EdwinXu/workspace/hadoop/hadoop-2.7.1/data/datanode</value>
   </property>
</configuration>


# mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>


# yarn-stie.xml
<configuration>
 <property>
       <name>yarn.nodemanager.aux-services</name>
       <value>mapreduce_shuffle</value>
   </property>
   <property>
       <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
       <value>org.apache.hadoop.mapred.ShuffleHandler</value>
   </property>
   
</configuration>
```

安装java，配置环境变量

- 系统指定JAVA_HOME
- 在hadoop-env.sh中直接指定：export JAVA_HOME=/usr



验证：

jps:

```java
jps
6101 DataNode
6725 Jps
6299 SecondaryNameNode
6622 NodeManager
```



























































