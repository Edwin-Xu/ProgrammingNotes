# Architecture Notes

> Learn architecture knowledge

## My Notes



## 凤凰架构

### 前言

这是一部以“**如何构建一套可靠的分布式大型软件系统**”为叙事主线的开源文档，是一幅帮助开发人员整理现代软件架构各条分支中繁多知识点的技能地图

“Phoenix”这个词东方人不常用，但在西方的软件工程读物——尤其是关于 Agile、DevOps 话题的作品中时常出现。软件工程小说《[The Phoenix Project](https://book.douban.com/subject/20644908/)》讲述了徘徊在死亡边缘的 Phoenix 项目在精益方法下浴火重生的故事；马丁·福勒（Martin Fowler）对《[Continuous Delivery](https://book.douban.com/subject/4327796/)》的诠释里，曾多次提到“[Phoenix Server](https://martinfowler.com/bliki/PhoenixServer.html)”（取其能够“涅槃重生”之意）与“[Snowflake Server](https://martinfowler.com/bliki/SnowflakeServer.html)”（取其“世界上没有相同的两片雪花”之意）的优劣比对。也许是东西方的文化的差异，尽管有“失败是成功之母”这样的谚语，但我们东方人的骨子里更注重的还是一次把事做对做好，尽量别出乱子；而西方人则要“更看得开”一些，把出错看做正常甚至是必须的发展过程，只要出了问题能够兜底使其重回正轨便好。

在软件工程里，任何产品的研发，只要时间尺度足够长，人就总会疏忽犯错，代码就总会携有缺陷，电脑就总会宕机崩溃，网络就总会堵塞中断……如果一项工程需要大量的人员，共同去研发某个大规模的软件产品，并使其分布在网络中大量的服务器节点中同时运行，随着项目规模的增大、运作时间变长，其必然会受到墨菲定律的无情打击。

> 墨菲定律（Murphy's Law）
>
> Anything that can go wrong will go wrong.
> 如果事情可能出错就总会出错。



软件架构风格从大型机（Mainframe），到[原始分布式](https://icyfenix.cn/architecture/architect-history/primitive-distribution.html)（Distributed），到[大型单体](https://icyfenix.cn/architecture/architect-history/monolithic.html)（Monolithic），到[面向服务](https://icyfenix.cn/architecture/architect-history/soa.html)（Service-Oriented），到[微服务](https://icyfenix.cn/architecture/architect-history/microservices.html)（Microservices），到[服务网格](https://icyfenix.cn/architecture/architect-history/post-microservices.html)（Service Mesh），到[无服务](https://icyfenix.cn/architecture/architect-history/serverless.html)（Serverless）

### 服务架构演进

#### 原始分布式时代

> UNIX 的分布式设计哲学
>
> Simplicity of both the interface and the implementation are more important than any other attributes of the system — including correctness, consistency, and completeness
>
> 保持接口与实现的简单性，比系统的任何其他属性，包括准确性、一致性和完整性，都来得更加重要。

可能与绝大多数人心中的认知会有差异，“**使用多个独立的分布式服务共同构建一个更大型系统**”的设想与实际尝试，反而要**比今天大家所了解的大型单体系统出现的时间更早**

#### 单体系统

> 单体架构（Monolithic）
>
> “单体”只是表明系统中主要的过程调用都是进程内调用，不会发生进程间通信，仅此而已。

“单体架构”在整个软件架构演进的历史进程里，是出现时间最早、应用范围最广、使用人数最多、统治历史最长的一种架构风格，但“单体”这个名称，却是在微服务开始流行之后才“事后追认”所形成的概念。此前，并没有多少人将“单体”视作一种架构来看待

从纵向角度来看，笔者从未见过实际生产环境里有哪个大型的现代信息系统是完全不分层的。分层架构（Layered Architecture）已是现在几乎所有信息系统建设中都普遍认可、采用的软件设计方法，无论是单体还是微服务，抑或是其他架构风格，都会对代码进行纵向层次划分，收到的外部请求在各层之间以不同形式的数据结构进行流转传递，触及最末端的数据库后按相反的顺序回馈响应

![img](_images/ArchitectureNotes.asserts/layed-arch.8e054a47.png)



**从横向角度来看，单体架构也可以支持按照技术、功能、职责等维度，将软件拆分为各种模块，以便重用和管理代码**。**<u>单体系统并不意味着只能有一个整体的程序封装形式</u>**，如果需要，它完全可以由多个 JAR、WAR、DLL、Assembly 或者其他模块格式来构成。即使是**以横向扩展（Scale Horizontally）的角度来衡量，在负载均衡器之后同时部署若干个相同的单体系统副本，以达到分摊流量压力的效果，也是非常常见的需求**。

#### SOA时代

> SOA 架构（Service-Oriented Architecture）
>
> 面向服务的架构是一次具体地、系统性地成功解决分布式服务主要问题的架构模式。

为了**对大型的单体系统进行拆分，让每一个子系统都能独立地部署、运行、更新**，开发者们曾经尝试过多种方案，这里列举以下三种较有代表性的架构模式:

- [烟囱式架构](https://en.wikipedia.org/wiki/Information_silo)（Information Silo Architecture）：信息烟囱又名信息孤岛（Information Island），使用这种架构的系统也被称为孤岛式信息系统或者烟囱式信息系统。它指的是一种完全不与其他相关信息系统进行互操作或者协调工作的设计模式。这样的系统其实并没有什么“架构设计”可言. 

- [微内核架构](https://en.wikipedia.org/wiki/Microkernel)（Microkernel Architecture）：微内核架构也被称为插件式架构（Plug-in Architecture）。既然在烟囱式架构中，没有业务往来关系的系统也可能需要共享人员、组织、权限等一些的公共的主数据，那不妨就将这些主数据，连同其他可能被各子系统使用到的公共服务、数据、资源集中到一块，成为一个被所有业务系统共同依赖的核心（Kernel，也称为 Core System），具体的业务系统以插件模块（Plug-in Modules）的形式存在，这样也可提供可扩展的、灵活的、天然隔离的功能特性，即微内核架构

  ![img](_images/ArchitectureNotes.asserts/coresystem.f46f7c00.png)

- [事件驱动架构](https://en.wikipedia.org/wiki/Event-driven_architecture)（Event-Driven Architecture）：为了能让子系统互相通信，一种可行的方案是在子系统之间建立一套事件队列管道（Event Queues），来自系统外部的消息将以事件的形式发送至管道中，各个子系统从管道里获取自己感兴趣、能够处理的事件消息，也可以为事件新增或者修改其中的附加信息，甚至可以自己发布一些新的事件到管道队列中去，如此，每一个消息的处理者都是独立的，高度解耦的，但又能与其他处理者（如果存在该消息处理者的话）通过事件管道进行互动

  ![img](_images/ArchitectureNotes.asserts/eventbus.a0c12890.png)

- 

软件架构来到 SOA 时代，许多概念、思想都已经能在今天微服务中找到对应的身影了，譬如**服务之间的松散耦合、注册、发现、治理，隔离、编排，**等等。这些在今天微服务中耳熟能详的名词概念，大多数也是在分布式服务刚被提出时就已经可以预见的困难点。SOA 针对这些问题，甚至是针对“软件开发”这件事情本身，都进行了更加系统性、更加具体的探索。

#### 微服务

> 微服务架构（Microservices）
>
> 微服务是一种通过多个小型服务组合来构建单个应用的架构风格，这些服务围绕业务能力而非特定的技术标准来构建。各个服务可以采用不同的编程语言，不同的数据存储技术，运行在不同的进程之中。服务采取轻量级的通信机制和自动化的部署机制实现通信与运维。

微服务”这个技术名词最早在 2005 年就已经被提出，它是由 Peter Rodgers 博士在 2005 年度的云计算博览会（Web Services Edge 2005）上首次使用，当时的说法是“Micro-Web-Service”，指的是一种专注于单一职责的、语言无关的、细粒度 Web 服务（Granular Web Services）。“微服务”一词并不是 Peter Rodgers 直接凭空创造出来的概念，最初的微服务可以说是 SOA 发展时催生的产物，就如同 EJB 推广过程中催生了 Spring 和 Hibernate 那样，这一阶段的微服务是作为一种 SOA 的轻量化的补救方案而被提出的。时至今日，在英文版的维基百科上，仍然将微服务定义为一种 SOA 的变种形式，所以微服务在最初阶段与 SOA、Web Service 这些概念有所牵扯也完全可以理解

微服务真正的崛起是在 2014 年，相信阅读此文的大多数读者，也是从 Martin Fowler 与 James Lewis 合写的文章《[Microservices: A Definition of This New Architectural Term](https://martinfowler.com/articles/microservices.html)》中首次了解到微服务的

微服务的九个核心的业务与技术特征:

- **围绕业务能力构建**（Organized around Business Capability）
- **分散治理**（Decentralized Governance）。
- **通过服务来实现独立自治的组件**（Componentization via Services）
- **产品化思维**（Products not Projects）
- **数据去中心化**（Decentralized Data Management）
- **强终端弱管道**（Smart Endpoint and Dumb Pipe）
- **容错性设计**（Design for Failure）
- **演进式设计**（Evolutionary Design）
- **基础设施自动化**（Infrastructure Automation）

### 架构师的视觉



































