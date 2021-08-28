# Hadoop Notes

## Notes From Video





















































## Hadoop权威指南

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



































































