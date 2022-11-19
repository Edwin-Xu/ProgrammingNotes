# Kubernetes Notes



## My Notes

### install

wsl安装

先在wsl2下安装docker



启动systemd支持

由于WSL2当前不支持systemd，所以systemctl命令无法使用，这会限制K8s的使用，目前有一些开源脚本可以替代。 首先安装git命令

```
sudo apt install git
复制代码
```

然后运行脚本

```bash
git clone https://github.com/DamionGans/ubuntu-wsl2-systemd-script.git
cd ubuntu-wsl2-systemd-script/
bash ubuntu-wsl2-systemd-script.sh
```

之后就可以使用systemctl了，不过目前看起来如果系统重启后，需要重新执行ubuntu-wsl2-systemd-script.sh，可以尝试加入启动项中



安装K8s

虽然Docker desktop中有建K8s的选项，但启动很慢，不建议使用，Docker总想去侵占容器编排的活儿，所以建议还是自己在Ubuntu中安装。

```arduino
sudo apt-get install -y apt-transport-https
```

需要以root用户执行

```ruby
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 

cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
```

安装kubelet、kubeadm和kubectl

- `kubelet`：在集群中的每个节点上用来启动 Pod 和容器等。
- `kubectl`：用来与集群通信的命令行工具。
- `kubeadm`：用来初始化集群的指令。

```sql
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```



使用kind快速部署K8s

[kind](https://link.juejin.cn?target=https%3A%2F%2Fkind.sigs.k8s.io%2F) 即 Kubernetes In Docker，顾名思义，就是将 K8s 所需要的所有组件，全部部署在一个docker容器中，是一套开箱即用的 K8s 环境搭建方案。使用 kind 搭建的集群无法在生产中使用，但是如果你只是想在本地简单的玩玩 K8s，不想占用太多的资源，那么使用 kind 是你不错的选择。同样，kind 还可以很方便的帮你本地的 k8s 源代码打成对应的镜像，方便测试。 kind只是一个二进制的文件，直接下载下来就可以使用。

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /bin/
```

查看安装情况

```
kind version 
```

最简单的情况，我们使用一条命令就能创建出一个单节点的 K8s 环境

```lua
kind create cluster 

```

至此，整个环境部署就已经完成

### kind

kind即 Kubernetes In Docker，将 k8s 所需要的所有组件，全部部署在了一个docker容器中，是一套开箱即用的 k8s 环境搭建方案，可以让我们快速的搭建k8s测试平台。它将每个容器模拟成一个k8s节点，可以轻松地在单节点上部署"多节点"集群，甚至"高可用集群"，而且还可以部署和管理多个版本集群。在搭建个人学习平台时，如果要搭建一个多控多计算的集群，个人电脑很难有这么高的资源配置，使用kind来部署集群就很有必要了。



### SpringCloud vs. K8s

Spring Cloud 和 Kubernetes 都声称自己是开发和运行微服务的最佳环境，但它们在本质上有很大的不同，解决的问题也不同。在本文中，我们将看看每个平台是如何交付基于微服务架构(MSA)的？它们擅长哪些领域？以及如何充分利用这两个领域在微服务的旅程中取得成功。



https://cloud.tencent.com/developer/article/1776313










## 官方文档学习

> https://www.kubernetes.org.cn/k8s

### 概述

[**Kubernetes**](https://www.kubernetes.org.cn/)是一个开源的，**用于管理云平台中多个主机上的容器化的应用**，Kubernetes的**目标是让部署容器化的应用简单并且高效**（powerful）,Kubernetes提供了应用部署，规划，更新，维护的一种机制。

Kubernetes一个核心的特点就是能够自主的管理容器来保证云平台中的容器按照用户的期望状态运行着（比如用户想让apache一直运行，用户不需要关心怎么去做，Kubernetes会自动去监控，然后去重启，新建，总之，让apache一直提供服务），管理员可以加载一个微型服务，让规划器来找到合适的位置，同时，Kubernetes也系统提升工具以及人性化方面，让用户能够方便的部署自己的应用（就像canary deployments）。

在Kubenetes中，所有的容器均在[**Pod**](https://www.kubernetes.org.cn/tags/pod)中运行,一个Pod可以承载一个或者多个相关的容器，在后边的案例中，同一个Pod中的容器会部署在同一个物理机器上并且能够共享资源。一个Pod也可以包含O个或者多个磁盘卷组（volumes）,这些卷组将会以目录的形式提供给一个容器，或者被所有Pod中的容器共享，对于用户创建的每个Pod,系统会自动选择那个健康并且有足够容量的机器，然后创建类似容器的容器,当容器创建失败的时候，容器会被node agent自动的重启,这个node agent叫kubelet,但是，如果是Pod失败或者机器，它不会自动的转移并且启动，除非用户定义了 replication controller。



用户可以自己创建并管理Pod,Kubernetes将这些操作简化为两个操作：基于相同的Pod配置文件部署多个Pod复制品；

Kubernetes支持一种特殊的网络模型，Kubernetes创建了一个地址空间，并且不动态的分配端口，它可以允许用户选择任何想使用的端口，为了实现这个功能，它为每个Pod分配IP地址。

所有Kubernetes中的资源，比如Pod,都通过一个叫URI的东西来区分，这个URI有一个UID,URI的重要组成部分是：对象的类型（比如pod），对象的名字，对象的命名空间，对于特殊的对象类型，在同一个命名空间内，所有的名字都是不同的，在对象只提供名称，不提供命名空间的情况下，这种情况是假定是默认的命名空间。UID是时间和空间上的唯一。



#### 起源

**大规模容器集群管理工具，从Borg到Kubernetes**

在Docker 作为高级容器引擎快速发展的同时，Google也开始将自身在容器技术及集群方面的积累贡献出来。在Google内部，容器技术已经应用了很多年，Borg系统运行管理着成千上万的容器应用，在它的支持下，无论是谷歌搜索、Gmail还是谷歌地图，可以轻而易举地从庞大的数据中心中获取技术资源来支撑服务运行。

Borg提供了3大好处:

1. 隐藏资源管理和错误处理，用户仅需要关注应用的开发。

2) 服务高可用、高可靠。

3) 可将负载运行在由成千上万的机器联合而成的集群中。

作为Google的竞争技术优势，Borg理所当然的被视为商业秘密隐藏起来，但当Tiwtter的工程师精心打造出属于自己的Borg系统（Mesos）时， Google也审时度势地推出了来源于自身技术理论的新的开源工具

2014年6月，谷歌云计算专家埃里克·布鲁尔（Eric Brewer）在旧金山的发布会为这款新的开源工具揭牌，它的名字Kubernetes在希腊语中意思是船长或领航员，这也恰好与它在容器集群管理中的作用吻合，即作为装载了集装箱（Container）的众多货船的指挥者，负担着全局调度和运行监控的职责。

Kubernetes作为容器集群管理工具，于2015年7月22日迭代到 v 1.0并正式对外公布，这意味着这个开源容器编排系统可以正式在生产环境使用。与此同时，谷歌联合Linux基金会及其他合作伙伴共同成立了CNCF基金会( Cloud Native Computing Foundation)，并将Kuberentes 作为首个编入CNCF管理体系的开源项目，助力容器技术生态的发展进步。Kubernetes项目凝结了Google过去十年间在生产环境的经验和教训，从Borg的多任务Alloc资源块到Kubernetes的多副本Pod，从Borg的Cell集群管理，到Kubernetes设计理念中的联邦集群，在Docker等高级引擎带动容器技术兴起和大众化的同时，为容器集群管理提供独了到见解和新思路。

### 设计架构

#### 节点

Kubernetes集群包含有**节点代理kubelet和Master组件**(APIs, scheduler, etc)，一切都基于分布式的存储系统。

![image-20220814202951753](_images/K8sNotes.asserts/image-20220814202951753.png)

在这张系统架构图中，我们把服务分为**运行在工作节点上的服务和组成集群级别控制板的服务。**

Kubernetes主要由以下几个核心组件组成：

- **etcd保存了整个集群的状态；**
- **apiserver提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制；**
- **controller manager负责维护集群的状态，比如故障检测、自动扩展、滚动更新等；**
- **scheduler负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上；**
- **kubelet负责维护容器的生命周期，同时也负责Volume（CVI）和网络（CNI）的管理；**
- **Container runtime负责镜像管理以及Pod和容器的真正运行（CRI）；**
- **kube-proxy负责为Service提供cluster内部的服务发现和负载均衡；**

除了核心组件，还有一些推荐的Add-ons：

- kube-dns负责为整个集群提供DNS服务
- Ingress Controller为服务提供外网入口
- Heapster提供资源监控
- Dashboard提供GUI
- Federation提供跨可用区的集群
- Fluentd-elasticsearch提供集群日志采集、存储与查询

![image-20220814203917162](_images/K8sNotes.asserts/image-20220814203917162.png)

![image-20220814203940929](_images/K8sNotes.asserts/image-20220814203940929.png)

### 分层架构

Kubernetes设计理念和功能其实就是一个类似Linux的分层架构

![image-20220814204127988](_images/K8sNotes.asserts/image-20220814204127988.png)

- **核心**层：Kubernetes最核心的功能，对外提供API构建高层的应用，对内提供插件式应用执行环境
- **应用**层：部署（无状态应用、有状态应用、批处理任务、集群应用等）和路由（服务发现、DNS解析等）
- 管理层：系统度量（如基础设施、容器和网络的度量），自动化（如自动扩展、动态Provision等）以及策略管理（RBAC、Quota、PSP、NetworkPolicy等）
- 接口层：kubectl命令行工具、客户端SDK以及集群联邦
- 生态系统：在接口层之上的庞大容器集群管理调度的生态系统，可以划分为两个范畴
  - Kubernetes外部：日志、监控、配置管理、CI、CD、Workflow、FaaS、OTS应用、ChatOps等
  - Kubernetes内部：CRI、CNI、CVI、镜像仓库、Cloud Provider、集群自身的配置和管理等



kubelet:

kubelet负责管理[pods](https://www.kubernetes.org.cn/kubernetes-pod)和它们上面的容器，images镜像、volumes、etc。



kube-proxy

**每一个节点也运行一个简单的网络代理和负载均衡**（详见[services FAQ](https://github.com/kubernetes/kubernetes/wiki/Services-FAQ) )（PS:官方 英文）。 正如Kubernetes API里面定义的这些服务（详见[the services doc](https://github.com/kubernetes/kubernetes/blob/release-1.2/docs/user-guide/services.md)）（PS:官方 英文）也可以在各种终端中以轮询的方式做一些简单的TCP和UDP传输。

服务端点目前是通过DNS或者环境变量( Docker-links-compatible 和 Kubernetes{FOO}_SERVICE_HOST 及 {FOO}_SERVICE_PORT 变量都支持)。这些变量由服务代理所管理的端口来解析。



Kubernetes控制面板可以分为多个部分。目前它们都运行在一个*master* 节点，然而为了达到高可用性，这需要改变。不同部分一起协作提供一个统一的关于集群的视图。



etcd

所有master的持续状态都存在etcd的一个实例中。这可以很好地存储配置数据。因为有watch(观察者)的支持，各部件协调中的改变可以很快被察觉。



Kubernetes API Server

API服务提供[Kubernetes API](https://github.com/kubernetes/kubernetes/blob/release-1.2/docs/api.md) （PS:官方 英文）的服务。这个服务试图通过把所有或者大部分的业务逻辑放到不两只的部件中从而使其具有CRUD特性。它主要处理REST操作，在etcd中验证更新这些对象（并最终存储）。



Scheduler

调度器把未调度的pod通过binding api绑定到节点上。调度器是可插拔的，并且我们期待支持多集群的调度，未来甚至希望可以支持用户自定义的调度器。



Kubernetes控制管理服务器

所有其它的集群级别的功能目前都是由控制管理器所负责。例如，端点对象是被端点控制器来创建和更新。这些最终可以被分隔成不同的部件来让它们独自的可插拔。

[replicationcont](https://github.com/kubernetes/kubernetes/blob/release-1.2/docs/user-guide/replication-controller.md)[roller](https://github.com/kubernetes/kubernetes/blob/release-1.2/docs/user-guide/replication-controller.md)（PS:官方 英文）是一种建立于简单的 [pod](https://www.kubernetes.org.cn/kubernetes-pod) API之上的一种机制。一旦实现，我们最终计划把这变成一种通用的插件机制。

### 设计理念



### 创建k8s集群











































































