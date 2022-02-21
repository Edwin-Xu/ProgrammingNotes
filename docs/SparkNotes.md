# Spark Notes



## Spark Notes

### Spark概述

#### Spark是什么

Apache Spark 是基于内存的快速、通用、可扩展的大数据分析流程。

#### spark and hadoop

Hadoop

 ⚫ 2006 年 1 月，Doug Cutting 加入 Yahoo，领导 Hadoop 的开发

 ⚫ 2008 年 1 月，Hadoop 成为 Apache 顶级项目

 ⚫ 2011 年 1.0 正式发布

 ⚫ 2012 年 3 月稳定版发布

 ⚫ 2013 年 10 月发布 2.X (Yarn)版本

Spark

 ⚫ 2009 年，Spark 诞生于伯克利大学的 AMPLab 实验室

 ⚫ 2010 年，伯克利大学正式开源了 Spark 项目

 ⚫ 2013 年 6 月，Spark 成为了 Apache 基金会下的项目

 ⚫ 2014 年 2 月，Spark 以飞快的速度成为了 Apache 的顶级项目

 ⚫ 2015 年至今，Spark 变得愈发火爆，大量的国内公司开始重点部署或者使用 Spark



从功能上：

Hadoop：

- java编写
- 作为hadoop分布式文件系统，源于Google的TheGoogleFileSystem这篇论文
- MR
- HBASE是Google的Bigtable的开源实现，但是和bigtable有许多不同之处。HBASE是一个基于HDFS的分布式数据库，擅长实时读/写超大规模的数据集，是hadoop非常重要的组件

Spark：

- Spark是一种由Scala开发的 通用快速可扩展的 大数据分析引擎
- Spark Core提供最基础的功能
- Spark SQL是用来操作结构化数据的组件。用户可以通过SQL或者HQL来查询数据
- Spark Streaming是Spark平台上针对实时数据进行流式计算的组件，提供了丰富的处理数据流的API

Spark一直被认为是hadoop的升级版



hadoop比较慢，但是可以处理非常大的数据量

spark很快，但是处理的数据量有限

#### Spark OR Hadoop

MR和Spark都是处理数据的框架，该如何选择？

MR不满足数据的迭代循环计算，在一些数据可复用场景中不适用。

Spark则是可以重复利用数据计算

Spark就是在传统的MR计算框架基础上，利用其计算过程的优化，从而大大加快了数据分析、挖掘和读写速度

并将计算单元缩小到了更适合并行运算和重复使用的RDD计算模型

Spark**是一个分布式数据快速分析项目**，它的核心计算使 **弹性分布式数据集 Resilient Distributed Datasets**，提供比MR更加丰富的模型，可以在内存中对数据集进行多次的的迭代，来支持复杂的数据挖掘算法和图形计算算法。

Spark和hadoop的根本差异是多个作业之间的数据通信问题，spark是基于内存，而hadoop是基于磁盘

spark task启动时间快，spark采用fork线程的方式，而hadoop采用创建新的进程的方式。

#### Spark核心模块

![image-20211107224118124](_images/SparkNotes.assets/image-20211107224118124.png)

Spark Core 中提供了 Spark 最基础与最核心的功能

Spark SQL 是 Spark 用来操作结构化数据的组件。

Spark Streaming 是 Spark 平台上针对实时数据进行流式计算的组件

MLlib 是 Spark 提供的一个机器学习算法库。MLlib 不仅提供了模型评估、数据导入等 额外的功能，还提供了一些更底层的机器学习原语。

GraphX 是 Spark 面向图计算提供的框架与算法库。



弹性分布式数据集

Resilient Distributed Datasets





### 快速上手

#### HelloWorld

```scala
object WordCount {
  def main(args: Array[String]): Unit = {
    val path:String = "D:\\tmp\\log.txt"

    // 创建运行配置
    val sparkConf = new SparkConf()
      .setMaster("local[*]")
      .setAppName("WordCount")
    // 创建上下文环境对象
    val sc:SparkContext = new SparkContext(sparkConf);
    // 读取文件数据
    val fileRDD:RDD[String] = sc.textFile(path);
    // 分词
    val wordRDD :RDD[String] = fileRDD.flatMap(_.split(" "))
    // 转map
    val word2OneRDD:RDD[(String, Int)] = wordRDD.map((_,1))
    // 分组聚合
    val word2CountRDD:RDD[(String, Int)] = word2OneRDD.reduceByKey(_+_);
    // 将数据聚合结果采集到内存中
    val word2Count:Array[(String, Int)] = word2CountRDD.collect()
    // 打印
    word2Count.foreach(println)
    // 关闭spark连接
    sc.stop()
  }
}
```



## My Notes

### Hive 兼容

https://zhuanlan.zhihu.com/p/149013623

UDAF

注意不是所有的Hive UDF/UDTF/UDAF在spark sql中都支持，下面是一些不支持的api：

- getRequiredJars 和 getRequiredFiles 方法用于在UDF中自动加载jar包
- initialize(StructObjectInspector) 目前暂不支持， spark目前仅适用一个已经标记为弃用的接口 initialize(ObjectInspector[])
- configure 用于初始化 MapredContext，在Spark中不支持
- close 用于释放资源，spark sql执行的时候不会调用该方法
- reset 用于在重用UDAF时，重新进行初始化；spark目前不支持udaf的重用
- getWindowingEvaluator 在聚合的时候基于固定的窗口进行优化，spark不支持

### 下划线常见用法

https://www.jianshu.com/p/0497583ec538

### spark-submit

spark-submit 用户打包 Spark 应用程序并部署到 Spark 支持的集群管理气上

```sql
spark-submit [options] <python file> [app arguments]
```

– master: 设置主节点 URL 的参数。支持：
  local： 本地机器。
  spark://host:port：远程 Spark 单机集群。
  yarn：yarn 集群
–deploy-mode：允许选择是否在本地（使用 client 选项）启动 Spark 驱动程序，或者在集群内（使用 cluster 选项）的其中一台工作机器上启动。默认值是 client。
–name：应用程序名称，也可在程序内设置。
–py-files：.py, .egg 或者 .zip 文件的逗号分隔列表，包括 Python 应用程序。这些文件将分发给每个执行节点。
–files：逗号分隔的文件列表，这些文件将分发给每个执行节点。
–conf：动态地改变应用程序的配置。
–driver-memory：指定应用程序在驱动节点上分配多少内存的参数，类似与 10000M， 2G。默认值是 1024M。
–executor-memory：指定每个执行节点上为应用程序分配的内存，默认 1G。
–num-executors：指定执行器节点数。
–help：展示帮助信息和退出。

```sql
spark-submit \
--master local \
--name sync_hive_to_doris \
--deploy-mode client  \
--num-executors 8  \
--executor-memory 5g \
--executor-cores  4  \
--conf spark.dynamicAllocation.enabled=false \
--jars mysql-connector-java-5.1.12.jar,doris-spark-1.0.0-SNAPSHOT.jar \
--conf spark.custom.doris.mysql_ip="$mysql_ip" \
--conf spark.custom.doris.mysql_port="$mysql_fe_port" \
--conf spark.custom.doris.db="$db" \
--conf spark.custom.doris.user="$user" \
--conf spark.custom.doris.password="$password" \
--conf spark.custom.target_table="$target_table" \
--conf spark.custom.doris.http_port="$mysql_be_port" \
--conf spark.custom.batchSize="$batchSize" \
--conf spark.custom.fieldSeparator="$fieldSeparator" \
--conf spark.custom.spark_sql="$spark_sql" \
--conf spark.custom.serviceTime="$datetime" \
--conf spark.custom.sql="$sql" \
--class com.qunar.fintech.doris.tools.IvToolsDataSyncDoris  \
   my.jar 
```





## Spark快速上手

IDEA安装Scala插件

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.12</artifactId>
        <version>3.0.0</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <!-- 该插件用于将 Scala 代码编译成 class 文件 -->
        <plugin>
            <groupId>net.alchim31.maven</groupId>
            <artifactId>scala-maven-plugin</artifactId>
            <version>3.2.2</version>
            <executions>
                <execution>
                    <!-- 声明绑定到 maven 的 compile 阶段 -->
                    <goals>
                        <goal>testCompile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-assembly-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <descriptorRefs>
                    <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
            </configuration>
            <executions>
                <execution>
                    <id>make-assembly</id>
                    <phase>package</phase>
                    <goals>
                        <goal>single</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```





先了解到这里

尚硅谷的笔记，地8页

















