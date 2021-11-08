# Hadoop Notes

# Notes From Video

https://ke.qq.com/course/3030492?taid=10164911987375580

## 大数据概况及Hadoop

### 大数据

大数据是一个描述大量告诉复杂和可变数据的术语，需要先进的技术来实现信息的获取、存储、分发、管理和分析

![image-20210901180316313](HadoopNotes.assets/image-20210901180316313.png)

- volume 体量大
- velocity 处理速度快
- variety：种类繁多：结构化 半结构化 非结构化
- value：价值密度低

![image-20210901181450607](HadoopNotes.assets/image-20210901181450607.png)

### Hadoop概述

![image-20210901181600509](HadoopNotes.assets/image-20210901181600509.png)

http://hadoop.apache.org/

![image-20210901182253475](HadoopNotes.assets/image-20210901182253475.png)

![image-20210901182308609](HadoopNotes.assets/image-20210901182308609.png)



## Hadoop

### 架构

- common 公共模块

- HDFS 数据存储，分布式

- MapReduce：处理数据的核心框架

- yarn：资源管理器，资源调度，协调管理，2.x是Tez

- ecosystem：生态圈

  ![image-20210901183122534](HadoopNotes.assets/image-20210901183122534.png)

![image-20210901182946090](HadoopNotes.assets/image-20210901182946090.png)

java语言实现的

### install

- 配置jdk
- Hadoop配置
- 



### HDFS role

![image-20210902122626391](HadoopNotes.assets/image-20210902122626391.png)

![image-20210902123424458](HadoopNotes.assets/image-20210902123424458.png)

#### NameNode

NameNode存储元数据，保存数据分为多少块，每一块存放在那些节点上

数据都是存在DataNode节点

https://ke.qq.com/course/3030492?taid=10164942052146652

#### DataNode

![image-20210902123253507](HadoopNotes.assets/image-20210902123253507.png)

### 组件

![image-20210902123531875](HadoopNotes.assets/image-20210902123531875.png)

2.x版本每一个块默认是128MB

避免在HDFS中存储小文件

每个块默认保存三份，用以备份

![image-20210902173248589](HadoopNotes.assets/image-20210902173248589.png)

### MapReduce Engine

![image-20210902173421222](HadoopNotes.assets/image-20210902173421222.png)

![image-20210902173441988](HadoopNotes.assets/image-20210902173441988.png)

## HDFS 读写

![image-20210902173641638](HadoopNotes.assets/image-20210902173641638.png)

![image-20210902174229009](HadoopNotes.assets/image-20210902174229009.png)

### HDFS CLI

![image-20210902182148964](HadoopNotes.assets/image-20210902182148964.png)

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

![image-20210910123833624](HadoopNotes.assets/image-20210910123833624.png)

![image-20210910124308008](HadoopNotes.assets/image-20210910124308008.png)

![image-20210910140709087](HadoopNotes.assets/image-20210910140709087.png)

shuffle

![image-20210910140843379](HadoopNotes.assets/image-20210910140843379.png)

![image-20210910141015158](HadoopNotes.assets/image-20210910141015158.png)

![image-20210910141444557](HadoopNotes.assets/image-20210910141444557.png)

![image-20210910143346888](HadoopNotes.assets/image-20210910143346888.png)

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

![image-20211024225414290](HadoopNotes.assets/image-20211024225414290.png)

![image-20211024225558557](HadoopNotes.assets/image-20211024225558557.png)

hive将结构化数据映射为一张表

优势：

- 编码简单：HQL
- hive支持不同的运算框架：如spark等



![image-20211024230009791](HadoopNotes.assets/image-20211024230009791.png)



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

![image-20210827180501034](HadoopNotes.assets/image-20210827180501034.png)

RDBMS适用于关系型数据库，而MR适合非结构化半结构化数据

##### 1.3.2 网格计算

High Performance Computing/HPC高性能计算和网格计算，做大规模数据处理，他们使用消息传递接口MPI/message passing interface这样的api

##### 1.3.3 志愿计算



#### 1.4 Hadoop发展简史

![image-20210827181721446](HadoopNotes.assets/image-20210827181721446.png)

![image-20210827182106815](HadoopNotes.assets/image-20210827182106815.png)



#### 1.5 Apache Hadoop

虽然Hadoop最出名的是MapReduce以及其分布式文件系统HDFS，但是其还有很多其他子项目：

![image-20210827182216364](HadoopNotes.assets/image-20210827182216364.png)

![image-20210827182418957](HadoopNotes.assets/image-20210827182418957.png)

![image-20210827182442454](HadoopNotes.assets/image-20210827182442454.png)

### 2.MapReduce

![image-20210827183321170](HadoopNotes.assets/image-20210827183321170.png)

![image-20210827183608925](HadoopNotes.assets/image-20210827183608925.png)

#### 2.4 分布化

**MR JOB是执行的单位：包含输入数据、MR程序和配置信息**

**Hadoop通过把作业分成若干个小任务Task来工作：包括map和reduce**

**有两种类型的节点控制着作业执行过程：JOBTracker和多个TaskTracker**

**job tracker通过调度任务在task tracker上执行，来协调所有运行在系统上的作业，task tracker在运行的同时想jobtracker汇报进度**

**jobtracker记录每个任务的执行情况，如果有任务失败则调用其他task执行**

hadoop将数据分片发送给MR，MR为每一个分片创建一个map任务

一个分片往往是一个HDFS块的大小

![image-20211108203210035](HadoopNotes.assets/image-20211108203210035.png)

![image-20211108203349056](HadoopNotes.assets/image-20211108203349056.png)

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

![image-20211108211557058](HadoopNotes.assets/image-20211108211557058.png)

hdfs://host/path/*

FSDataInputStream

FileSystemDoubleCat



目录：

Filestatus



#### 3.6.数据流

![image-20211108212151198](HadoopNotes.assets/image-20211108212151198.png)

节点间通过RPC通信

![image-20211108212342696](HadoopNotes.assets/image-20211108212342696.png)



副本的存放：

![image-20211108213433726](HadoopNotes.assets/image-20211108213433726.png)



#### 归档

Hadoop Archives

### Hadoop IO

数据完整性校验

压缩

![image-20211108214217922](HadoopNotes.assets/image-20211108214217922.png)

编码解码



序列化：

Hadoop使用自己的序列化工具Writables



##### Writeable

![image-20211108215017497](HadoopNotes.assets/image-20211108215017497.png)













TODO

Combiner



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



























































