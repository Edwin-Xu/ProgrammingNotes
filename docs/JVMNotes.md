# JVM notes



# MyNotes



# 深入理解Java虚拟机

《深入理解Java虚拟机》JVM高级特性和最佳实践

周志明- 第三版

## C0-前言

本书一共分为五个部分：**走近Java、自动内存管理、虚拟机执行子系统、程序编译与代码优化、 高效并发**。

本书介绍的Java虚拟机并不局限于某一个特定发行商或者某一款特定虚拟机，只是由于 OracleJDK/OpenJDK在市场占有率上的绝对优势，其中的HotSpot虚拟机不可避免地成为本书主要分 析、讲解的对象

JDK从1.5版本开始，其官方的正式文档与宣传材料中的发行版本号启用了JDK 5、6、7……的新 命名方式；从2018年3月发布的JDK 10起，JDK的开发版本号（如java-version）也放弃了以前1.x的命 名形式，改为按发布的日期时间命名



## C1 走进java

第一部分：走进java

### 技术体系

从广义上讲，Kotlin、Clojure、JRuby、Groovy等运行于Java虚拟机上的编程语言及其相关的程序 都属于Java技术体系中的一员

可以把**Java程序设计语言、Java虚拟机、Java类库**这三部分统称为**JDK**（Java Development Kit），JDK是用于支持Java程序开发的最小环境

![image-20220926222430798](_images/JVMNotes.asserts/image-20220926222430798.png)

- Java ME（Micro Edition）：支持Java程序运行在移动终端（手机、PDA）上的平台，对Java API 有所精简，并加入了移动终端的针对性支持，这条产品线在JDK 6以前被称为J2ME。有一点读者请勿 混淆，现在在智能手机上非常流行的、主要使用Java语言开发程序的Android并不属于Java ME。 
- ·Java SE（Standard Edition）：支持面向桌面级应用（如Windows下的应用程序）的Java平台，提 供了完整的Java核心API，这条产品线在JDK 6以前被称为J2SE。 
- ·Java EE（Enterprise Edition）：支持使用多层架构的企业应用（如ERP、MIS、CRM应用）的 Java平台，除了提供Java SE API外，还对其做了大量有针对性的扩充[4]，并提供了相关的部署支持， 这条产品线在JDK 6以前被称为J2EE，在JDK 10以后被Oracle放弃，捐献给Eclipse基金会管理，此后被 称为Jakarta EE

### 发展史

1991年4月，由James Gosling博士领导的绿色计划（Green Project）开始启动，此计划最初的目标 是开发一种能够在各种消费性电子产品（如机顶盒、冰箱、收音机等）上运行的程序架构。这个计划 的产品就是Java语言的前身：Oak（得名于James Gosling办公室外的一棵橡树）。Oak当时在消费品市 场上并不算成功，但随着1995年互联网潮流的兴起，Oak迅速找到了最适合自己发展的市场定位并蜕 变成为Java语言。

![image-20220926234532163](_images/JVMNotes.asserts/image-20220926234532163.png)



Java没有分裂，JDK 9总算是带着 Jigsaw最终发布了，除了Jigsaw外，JDK 9还增强了若干工具（JS Shell、JLink、JHSDB等），整顿了 HotSpot各个模块各自为战的日志系统，支持HTTP 2客户单API等91个JEP。

JDK 9发布后，Oracle随即宣布Java将会以持续交付的形式和更加敏捷的研发节奏向前推进，以后 **JDK将会在每年的3月和9月各发布一个大版本**，目的就是为避免众多功能特性被集中捆绑到一个 JDK版本上而引发交付风险。这次改革确实从根源上解决了跳票问题，但也为Java的用户和发行商带 来了颇大的压力，不仅程序员感慨“Java新版本还没开始用就已经过时了”，Oracle自己对着一堆JDK版 本分支也在挠头，不知道该如何维护更新，该如何提供技术支持

Oracle的解决方案是顺理成章地终 结掉“每个JDK版本最少维护三年”的优良传统，从此以后，**每六个JDK大版本中才会被划出一个长期 支持（Long Term Support，LTS）版**，只有LTS版的JDK能够获得为期三年的支持和更新，普通版的 JDK就只有短短六个月的生命周期。**JDK 8和JDK 11会是LTS版**，再下一个就到2021年发布的**JDK 17** 了。



按常理说Java刚给Oracle赚了88亿美金，该颇为受宠才对，可Oracle是典型只谈利益不讲情怀的公 司，InfoWorld披露的一封Oracle高管邮件表明[13]，Java体系中被认为无法盈利也没有太多战略前景的 部分会逐渐被“按计划报废”（Planned Obsolescence）。这事的第一刀落下是在2018年3月，O**racle正式 宣告Java EE成为历史名词**。虽然Java SE、Java EE和Java ME三条产品线里确实只有Java SE称得上成 功，但Java EE毕竟无比辉煌过，现在其中还持有着JDBC、JMS、Servlet等使用极为广泛的基础组件， 然而Oracle仍选择把它“扫地出门”，所有权直接赠送给Eclipse基金会，唯一的条件是以后不准再使 用“Java”这个商标[14]，所以取而代之的将是Jakarta EE。



随着JDK 11发布，Oracle同时调整了JDK的授权许可证，里面包含了好几个动作。首先，**Oracle从JDK 11起把以前的商业特性[16]全部开源给OpenJDK，这样OpenJDK 11和OracleJDK 11的代码和功 能，在本质上就是完全相同的**（官方原文是Essentially Identical）[17]。然后，**Oracle宣布以后将会同时 发行两个JDK：一个是以GPLv2+CE协议下由Oracle发行的OpenJDK（本书后面章节称其为Oracle OpenJDK），另一个是在新的OTN协议下发行的传统的OracleJDK**，这两个JDK共享绝大部分源码， 在功能上是几乎一样的[18]，核心差异是前者可以免费在开发、测试或生产环境中使用，但是只有半 年时间的更新支持；后者个人依然可以免费使用，但若在生产环境中商用就必须付费，可以有三年时 间的更新支持。如果说由此能得出“Java要收费”的结论，那是纯属标题党，最多只能说Oracle在迫使商 业用户要么不断升级JDK的版本，要么就去购买商业支持



**2019年2月，在JDK 12发布前夕，Oracle果然如之前宣布那样在六个月之后就放弃了对上一个版本 OpenJDK的维护，RedHat同时从Oracle手上接过OpenJDK 8和OpenJDK 11的管理权利和维护职责** [20]。Oracle不愿意在旧版本上继续耗费资源，而RedHat或者说它背后的IBM又乐意扩大自己在Java社 区的影响力，这是一笔双赢的交易。RedHat代替Oracle成为JDK历史版本的维护者，应该有利于Java的 持续稳定，但从技术发展角度来看，这并不能为Oracle领导Java社区的局面带来根本性的改变，毕竟要 添加新的或实验性的功能，仅会针对Java的最新版本，而不会在旧版本上动手



java: sum => oracle => openjdk + oraclejdk

### java虚拟机家族



32





















































