# Computer Notes



## 存储

### 机械硬盘和固态硬盘

硬盘分为：固态硬盘SSD、机械硬盘HDD

SSD采用闪存颗粒存储

HDD采用磁性碟片存储



机械硬盘即是传统普通硬盘，主要由：盘片，磁头，盘片转轴及控制电机，磁头控制器，数据转换器，接口，缓存等几个部分组成。机械硬盘中所有的盘片都装在一个旋转轴上，每张盘片之间是平行的，在每个盘片的存储面上有一个磁头，磁头与盘片之间的距离比头发丝的直径还小，所有的磁头联在一个磁头控制器上，由磁头控制器负责各个磁头的运动。磁头可沿盘片的半径方向运动，加上盘片每分钟几千转的高速旋转，磁头就可以定位在盘片的指定位置上进行数据的读写操作。硬盘作为精密设备，尘埃是其大敌，必须完全密封。

固态硬盘（Solid State Disk或Solid State Drive），也称作电子硬盘或者固态电子盘，是由控制单元和固态存储单元（DRAM或FLASH芯片）组成的硬盘。固态硬盘的接口规范和定义、功能及使用方法上与机械硬盘的相同，在产品外形和尺寸上也与机械硬盘一致。由于固态硬盘没有机械硬盘的旋转介质，因而抗震性极佳。其芯片的工作温度范围很宽（-40~85摄氏度）。目前广泛应用于军事、车载、工控、视频监控、网络监控、网络终端、电力、医疗、航空等、导航设备等领域。目前由于成本较高，还在逐渐普及到DIY市场。

目前个人电脑上不管是台式机还是笔记本用的大多是机械硬盘，如现在流行的 500G，1TB等都是机械硬盘。一些高端或者定制的台式机等也已经开始普遍的出现固态硬盘了，但是容量都还比较小，一般是128G，240G左右。目前主要还是固态硬盘成本还是算比较高的，普及的程度目前也算是一个发力的或者过度的阶段，许多人还是选择双硬盘，SSD固态硬盘用来装系统和程序，一些大文件还是会选择使用HDD机械硬盘来存储，所以固态硬盘的全面使用可能还需要几年的时间来发展。



对比：

1、防震抗摔性：目前的机械硬盘都是磁碟型的，数据储存在磁碟扇区里。而固态硬盘是使用闪存颗粒（即目前内存、MP3、U盘等存储介质）制作而成，所以SSD固态硬盘内部不存在任何机械部件，这样即使在高速移动甚至伴随翻转倾斜的情况下也不会影响到正常使用，而且在发生碰撞和震荡时能够将数据丢失的可能性降到最小。相较机械硬盘，固硬占有绝对优势。

2、数据存储速度：从PConline评测室的评测数据来看，固态硬盘相对机械硬盘性能提升2倍多。

3、功耗：固态硬盘的功耗上也要高于机械硬盘。

4、重量：固态硬盘在重量方面更轻，与常规1.8英寸硬盘相比，重量轻20-30克。

5、噪音：由于固硬属于无机械部件及闪存芯片，所以具有了发热量小、散热快等特点，而且没有机械马达和风扇，工作噪音值为0分贝。机械硬盘就要逊色很多。

6、价格：目前市场上80G Intel固态硬盘，价格为4000元左右。而这个价钱足够买几个容量为1TB的机械硬盘了。

7、容量：固态硬盘目前最大容量仅为256G(目前IBM公司已经开始测试容量为4TB的高速固态硬盘组)，和机械硬盘最大按TB容量衡量相比差距很大。

8、使用寿命：SLC只有10万次的读写寿命，成本低廉的MLC，读写寿命仅有1万次；比起机械硬盘毫无优势可言。



### DOS vs. CMD

有所区别,你在windows操作系统里进的DOS(即输入 CMD 进命令提示符)不是纯DOS,只是为方便某些需求而建立的,而纯DOS本身就是一种操作系统.(两者的区别:比如你可以在纯DOS下删除你的windows系统,但在你所说的"命令提示符"里却不能,因为你不可能"在房子里面拆房子吧?")

dos是磁盘操作系统；命令提示符是dos系统的界面中输入dos命令的提示位置；cmd是xp系统运行其自带dos的命令。

 

1、Windows 命令提示符（cmd.exe）是 Windows NT 下的一个用于运行 Windows 控制面板程序或某些 DOS 程序的shell程序；或在 Windows CE 下只用于运行控制面板程序的外壳程序。

 

2、command.exe是 Windows NT 命令行接口，它不是一个dos窗口；而 cmd.exe 是一个16位的DOS应用程序，它用于支持老的dos应用程序，它一般运行于NTVDM中。但就用户来说，这两个命令有惊人的相似之处，这是因为用户在command.com中输入的命令有很大一部分要送到cmd.exe中运行。

 

3、DOS是英文Disk Operating System的缩写，意思是“磁盘操作系统”。DOS是个人计算机上的一类操作系统。从1981年直到1995年的15年间，DOS在IBM PC 兼容机市场中占有举足轻重的地位。而且，若是把部分以DOS为基础的Microsoft Windows版本，如Windows 95、98和Me等都算进去的话，那么其商业寿命至少可以算到2000年。

 

4、DOS（Disk Operating System）是一个使用得十分广泛的磁盘操作系统。在 Windows 95/98（以及其后发生的 Windows 98与 Me）中，MS-DOS 核心依然存在，只是加上 Windows 当作系统的图型界面。直到纯 32 位版本的 Windows（从 NT 开始；包含了 2000、XP 、vista、win7、win8、win8.1和win10）才完全脱离了DOS的基础。



### Cmd vs. power shell

Windows 7 中开始有了一个PowerShell，实际是增强版的命令行工具。到了 Windows 10，它变成了默认的命令行工具。

 

PowerShell比之前的命令行复杂得多，当然也强悍得多，为了方便，后面我们简称之前的命令行工具还是命令行。命令行使用上和Linux终端差别很多，体验也差很多。但是PowerShell就强多了，而且命令行的命令基本可以直接在PowerShell中使用。

 

### RAID vs. JBOD

RAID是独立磁盘冗余阵列（**R**edundant **A**rray of **I**ndependent**D**isks）的简写，简称磁盘阵列。其基本思想就是把几个相对便宜的磁盘通过特定方式组合起来，使其在容量、可靠性等性能上达到甚至超过一个价格昂贵、容量巨大、可靠性高的磁盘。根据磁盘组合方式的不同可以分为RAID0 RAID1 RAID5 RAID6等

JBOD（Just a bunch of disk）严格上来说不是一种RAID，因为它只是简单将多个磁盘合并成一个大的逻辑盘，并没有任何的数据冗余。数据的存放机制就是从第一块磁盘开始依序向后存储数据。如果某个磁盘损毁，则该盘上的数据就会丢失。

相同情况下，JBOD的IO开销会更大



### IOUS 

IOPS (Input/Output Operations Per Second)，即每秒进行读写（I/O）操作的次数。



1、IOPS (Input/Output Per Second)即每秒的输入输出量(或读写次数)，是衡量磁盘性能的主要指标之一。**IOPS是指单位时间内系统能处理的I/O请求数量**，一般以每秒处理的I/O请求数量为单位，I/O请求通常为读或写数据操作请求。

2、随机读写频繁的应用，如小文件存储(图片)、OLTP数据库、邮件服务器，关注随机读写性能，IOPS是关键衡量指标。 顺序读写频繁的应用，传输大量连续数据，如电视台的视频编辑，视频点播VOD(Video On Demand)，关注连续读写性能。数据吞吐量是关键衡量指标。

3、IOPS和数据吞吐量适用于不同的场合：

读取10000个1KB文件，用时10秒 Throught(吞吐量)=1MB/s ，IOPS=1000 追求IOPS；

读取1个10MB文件，用时0.2秒 Throught(吞吐量)=50MB/s, IOPS=5 追求吞吐量；



IOPS和MB/S都是表现固态盘速度的单位，只是表现形式不同

用intel s3610，实测4K write，IOPS=13333，MB/S=52.08M换算，

就是IOPS*4再除以1024，就是MB/S，反之，MB/S乘1024，再除以4，就是IOPS。





## 计算

### CPU、processor

\# 查看物理CPU个数   （chip）

物理cpu数：主板上实际插入的cpu数量，可以数不重复的 physical id 有几个（physical id）
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

 

\# 查看每个物理CPU中core的个数   （core）

cpu核数：单块CPU上面能处理数据的芯片组的数量，如双核、四核等 （cpu cores）
cat /proc/cpuinfo| grep "cpu cores"| uniq

 

\# 查看逻辑CPU的个数   （processor）

逻辑cpu数：一般情况下，逻辑cpu=物理CPU个数×每颗核数，如果不相等的话，则表示服务器的CPU支持超线程技术（HT：简单来说，它可使处理器中的1 颗内核如2 颗内核那样在操作系统中发挥作用。这样一来，操作系统可使用的执行资源扩大了一倍，大幅提高了系统的整体性能，此时逻辑cpu=物理CPU个数×每颗核数x2）



### GPU

#### 显存 Vs. 内存

显存和内存有什么区别？两者有工作对象、存储
速度和容量的区别。工作对象方面，显存只为GPU
暂存资料，而内存则是为CPU和系统缓存资料空
间；存储速度方面，GDDR6显存速度最高可达
72GB/5,而DDR4内存速度在25.6GB/s。容量方
面，显存受制于显卡厂商设计，内存则可以根据用户
需要自行增减。具体介绍如下：
1、工作对象方面，显存只要是为GPU暂存资
料，而内存则是为CPU和系统缓存资料空间，如果
您使用的是集成显卡，那么系统没有单独的显存，显
存空间是在内存空间中划分出来的；
2、存储速度，以目前最新的GDDR6显存为
例，速度最高可达72GB/5,这是为了满足显卡大量
的图像素材读取的需要，而DDR4内存的速度是
25.6GB/s;
3、容量方面，显存容量是固定的，显卡厂商配
置的容量就是上限，消费者无法自行添加，消费级电
脑的内存是以DDR插槽为标准，您可以根据需求和
主板的插槽数量增减内存容量。



#### VGPU

vGPU提供在云服务器上搭载虚拟GPU的能力

虚拟化技术



#### GPU型号

NVIDIA常见的三大产品线如下
**Quadro类型**: Quadro系列显卡一般用于特定行业，比如设计、建筑等，图像处理专业显卡，比如CAD、Maya等软件。
**GeForce类型**: 这个系列显卡官方定位是消费级，常用来打游戏。但是它在深度学习上的表现也非常不错，很多人用来做推理、训练，单张卡的性能跟深度学习专业卡Tesla系列比起来其实差不太多，但是性价比却高很多。
**Tesla类型**: Tesla系列显卡定位并行计算，一般用于数据中心，具体点，比如用于深度学习，做训练、推理等。Tesla系列显卡针对GPU集群做了优化，像那种4卡、8卡、甚至16卡服务器，Tesla多块显卡合起来的性能不会受>很大影响，但是Geforce这种游戏卡性能损失严重，这也是Tesla主推并行计算的优势之一。

Quadro类型分为如下几个常见系列
**NVIDIA RTX Series系列**: RTX A2000、RTX A4000、RTX A4500、RTX A5000、RTX A6000
**Quadro RTX Series系列**: RTX 3000、RTX 4000、RTX 5000、RTX 6000、RTX 8000

GeForce类型分为如下几个常见系列
**Geforce 10系列**: GTX 1050、GTX 1050Ti、GTX 1060、GTX 1070、GTX 1070Ti、GTX 1080、GTX 1080Ti
**Geforce 16系列**：GTX 1650、GTX 1650 Super、GTX 1660、GTX 1660 Super、GTX 1660Ti
**Geforce 20系列**：RTX 2060、RTX 2060 Super、RTX 2070、RTX 2070 Super、RTX 2080、RTX 2080 Super、RTX 2080Ti
**Geforce 30系列**: RTX 3050、RTX 3060、RTX 3060Ti、RTX 3070、RTX 3070Ti、RTX 3080、RTX 3080Ti、RTX 3090 RTX 3090Ti

Tesla类型分为如下几个常见系列
**A-Series系列**: A10、A16、A30、A40、**<u>A100</u>**
**T-Series系列**: T4
**V-Series系列**: **<u>V100</u>**
**P-Series系列**: P4、P6、P40、**<u>P100</u>**
**K-Series系列**: K8、K10、K20c、K20s、K20m、K20Xm、K40t、K40st、K40s、K40m、K40c、K520、**<u>K80</u>**



## 显示

### 显卡

![image-20221012133336542](_images/ComputerNotes.asserts/image-20221012133336542.png)

显示适配器

就是显卡

### 多显示器

配置时发现外接的两个显示器可以显示，但是内容完全一样。

经过查询，发现需要**分线器**，把HDMI一分为二，分别作用于两个显示器。





## 术语

### IDC

互联网数据中心（Internet Data Center）简称IDC，就是电信部门利用已有的互联网[通信线路](https://baike.baidu.com/item/通信线路/1527630?fromModule=lemma_inlink)、带宽资源，建立标准化的电信专业级机房环境，为企业、政府提供服务器托管、租用以及相关增值等方面的全方位服务。

IDC主要是指互联网数据中心（InternetDataCenter，简称IDC）是指一种拥有完善的设备（包括高速互联网接入带宽、高性能局域网络、安全可靠的机房环境等）、专业化的管理、完善的应用的服务平台。

在这个平台基础上，IDC服务商为客户提供互联网基础平台服务（[服务器](https://cloud.tencent.com/product/cvm?from=20065&from_column=20065)托管、虚拟主机、邮件缓存、虚拟邮件等）以及各种增值服务（场地的租用服务、域名系统服务、负载均衡系统、数据库系统、数据备份服务等）。







