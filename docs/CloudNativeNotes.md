# Cloud Native

## 基础知识

### 基础概念

#### ECS

云服务器**ECS（Elastic Compute Service）**是阿里云提供的性能卓越、稳定可靠、弹性扩展的**IaaS**（Infrastructure as a Service）级别云计算服务。云服务器ECS免去了您采购IT硬件的前期准备，让您像使用水、电



#### IaC

基础设施即代码（IaC）是通过代码而非手动流程来管理和置备基础设施的方法。

Infrastructure as Code（IaC）是一种基于编程的技术，可以用于创建和管理计算机网络的基础设施，这些基础设施包括计算机、应用程序、存储和网络等。IaC可以帮助组织更快地部署和管理基础设施，并且更容易管理和实施更改

利用 IaC 我们可以创建包含基础设施规范的配置文件，从而便于编辑和分发配置。此外，它还可确保每次置备的环境都完全相同。通过对配置规范进行整理和记录，IaC 有助于实现[配置管理](https://www.redhat.com/zh/topics/automation/what-is-configuration-management)，并避免发生未记录的临时配置更改。

版本控制是 IaC 的一个重要组成部分，就像其他任何软件源代码文件一样，配置文件也应该在源代码控制之下。以基础设施即代码方式部署还意味着您可以将基础架构划分为若干模块化组件，它们可通过自动化以不同的方式进行组合。



避免手动配置以强制实施一致性

*幂等性*是给定操作始终产生相同结果的能力，是一个重要的 IaC 原则。 无论环境的启动状态如何，部署命令始终将目标环境设置为相同的配置。 通过自动配置现有目标或放弃现有目标并重新创建新环境来实现幂等性。





## Terraform

### 概述

#### 什么是Terraform

Terraform 是由 HashiCorp 创立的开源“**基础架构即代码**”工具。

[Terraform](https://www.terraform.io/)是一个开源的IT基础设施编排管理工具，Terraform支持使用配置文件描述单个应用或整个数据中心。



Terraform 是一种*声明式*编码工具，可以让开发人员用 HCL（HashiCorp 配置语言）高级配置语言来描述用于运行应用程序的“最终状态”云或本地基础架构。 它随后会生成用于达到该最终状态的计划，并执行该计划以供应基础架构。

由于 Terraform 使用的语法很简单，能够跨多个云和本地[数据中心](https://www.ibm.com/cn-zh/cloud/learn/data-centers)供应基础架构，并且能够安全高效地重新供应基础架构以响应配置更改，因此它是目前最受欢迎的基础架构自动化工具之一。 如果贵组织计划部署[混合云](https://www.ibm.com/cn-zh/cloud/learn/hybrid-cloud)或[多云](https://www.ibm.com/cloud/learn/multicloud)环境，那么您很可能想要或需要了解 Terraform。



阿里云与 Terraform 集成，可以使用Terraform来创建、修改、删除ECS、VPC、RDS、SLB等多种资源。

#### 基础架构即代码IaC

IaC 允许开发人员以让**供应自动化、更快速和可重现的方式来整理基础架构**。 它是 Agile 和 [DevOps](https://www.ibm.com/cn-zh/cloud/learn/devops-a-complete-guide) 实践的关键组件，这些实践包括版本控制、[持续集成](https://www.ibm.com/cn-zh/cloud/learn/continuous-integration)和[持续部署](https://www.ibm.com/cn-zh/cloud/learn/continuous-deployment)等。

IaC优点：

- **提高速度：**在需要部署和/或连接资源时，自动化比手动浏览界面更快。
- **提高可靠性：**如果基础架构庞大，那么很容易错误配置资源或以错误顺序供应服务。 借助 IaC，资源始终完全**按声明**进行供应和配置。
- **防止配置偏离：**当用于供应环境的配置不再与实际环境匹配时，便会出现配置偏离。（请参阅下面的“不可变基础架构”。）
- **支持实验、测试和优化：**因为使用“基础架构即代码”可以更快更轻松地供应新基础架构，因此可在不投入大量时间和资源的情况下进行和测试实验性更改；如果得到有利的结果，便可以快速扩展新的基础架构以投入生产。



基础设施即代码（IaC）是**通过代码而非手动流程来管理和置备**基础设施的方法。



Terraform是 IAC的一种，

#### Terraform优势

- 基础设施即代码
- **<u>基础设施可以使用高级配置语法进行描述，</u><u>使得基础设施能够被代码化、版本化，从而可以进行共享和重复利用</u>**
- 执行计划：Terraform有一个 "计划 "步骤，在这个步骤中，它会生成一个执行计划。执行计划显示了当你调用apply时，Terraform会做什么，这让你在Terraform操作基础设施时避免任何意外。
- 依赖图：Terraform建立了一个所有资源的图，**并行创建和修改任何非依赖性资源**。从而使得Terraform可以尽可能高效地构建基础设施，操作人员可以深入了解基础设施中的依赖性。
- 变更自动化：复杂的变更集可以应用于您的基础设施，而只需最少的人工干预。有了前面提到的执行计划和资源图，您就可以准确地知道Terraform将改变什么，以及改变的顺序，从而避免了许多可能的人为错误



#### 声明式方法与命令式方法

aC 有两种实施方法：声明式或命令式。 

声明式方法定义了系统的预期状态，包括所需的资源以及它们应具有的属性，随后 IaC 工具会为您进行相关配置。 

声明式方法还将保留系统对象的当前状态列表，因此在移除基础架构时会更便于管理。

另一方面，命令式方法则定义了实现预期配置所需的特定命令，最后需要以正确的顺序执行这些命令。 

许多 IaC 工具都使用声明式方法，并会自动置备所需的基础架构。如果您更改了预期状态，则声明式 IaC 工具会为您应用这些更改。命令式工具则需要您确定该如何应用这些更改。



#### 与 Kubernetes

有时候，很容易混淆 Terraform 与 Kubernetes 以及它们的实际用途。 事实上，这二者并非竞争关系，而是可以高效地协同工作。

[Kubernetes](https://www.ibm.com/cn-zh/cloud/learn/kubernetes) 是开源的[容器编排系统](https://www.ibm.com/cloud/blog/container-orchestration-explained)，允许开发人员在计算集群的节点上安排部署，并主动管理[容器化](https://www.ibm.com/cloud/learn/containerization)工作负载以确保其状态符合用户期望。

另一方面，Terraform 是一款基础架构即代码工具，覆盖范围更广，让开发人员可以自动完成跨越多个公有云和私有云的基础架构。

Terraform 可以自动化和管理[基础架构即服务 (IaaS)](https://www.ibm.com/cloud/learn/iaas)、[平台即服务 (PaaS)](https://www.ibm.com/cn-zh/cloud/learn/paas)，甚至[软件即服务 (SaaS)](https://www.ibm.com/cn-zh/cloud/learn/iaas-paas-saas) 级别的功能，并在所有提供商之间并行构建所有此类资源。 您可以使用 Terraform 来自动供应 Kubernetes，特别是云平台上管理的 [Kubernetes 集群](https://www.ibm.com/cloud/blog/kubernetes-clusters-architecture-for-rapid-controlled-cloud-app-delivery)，并自动将应用程序部署到集群中。

#### 与 Ansible

**Terraform 和 Ansible 都是“基础架构即代码”工具**，但两者之间存在几处明显差异. **Terraform 纯粹是一种声明式工具**（见上文），而 **Ansible 则将声明式和*程序式*配置结合**。 在程序式配置中，您可以指定步骤或精确方式，以用于供应基础架构来使其达到期望的状态。 程序式配置的工作量 更大，但控制能力更强。







### 教程学习

https://lonegunmanb.github.io/introduction-terraform/

#### 介绍

多年以前参加过一次 AWS AWSome Day，那是一种 AWS 在全球各大城市巡回举办的免费的技术研讨会，时长一天，为初次接触AWS大会的开发人员、IT 技术人员以及企业技术领域的决策者提供入门级的 AWS 产品介绍。在那次 AWSome Day 中，我第一次接触到了现在公有云里那些耳熟能详的概念，比如 Region、Availability Zone、Auto Scaling Group、RDS 这些经典产品。

最让我觉得惊奇的是，培训师现场演示了一种名为 CloudFormation 的产品，用培训师的话说就是“撒豆成兵”，**<u>通过编写一些 JSON 就可以批量反复创建一批云端资源</u>**

AWS AWSome Day中，<u>用一段JSON代码就可以让我们用指定的镜像 id 创建一台云端虚拟机，不需要在界面上点点点。要知道在当时，我正在一家初创公司工作，同时身兼架构师、后台开发程序员、DBA 以及运维数职，要维护测试、预发布以及生产三套环境</u>，时不时还因为要去修复因环境之间配置不一致而引发的种种错误而焦头烂额，那时的我就很期待 CloudFormation 能够给予我这种能够批量创建并管理"招之能来，来之能战，战之能胜，胜之能去"的环境的能力。

我当时并不知道在西雅图的华盛顿大学，有一个美日混血大帅哥 Mitchell Hashimoto 和他的老板 Armon Dagar 也深深沉迷于 CloudFormation 所带来的那种优雅与高效，同时他们也在头疼 CloudFormation 本身的一系列问题，最主要的就是它是 AWS 独占的。**<u>强人和我这种庸人最大的区别就是，强人有了想法直接就去做</u>**，Mitchell 和 Armon 在讨论中渐渐有了一个想法——打造一个多云(Multi-Cloud)的开源的基础设施即代码(IaC)工具，并且要超越 CloudFormation。他们组建了一家名为 **HashiCorp** 的公司来实现这个目标

在今年3月，HashiCorp 宣布成功获得 1.75 亿美元的E轮融资，投后公司估值 51 亿美元。HashiCorp 的产品线主要有 Nomad、Consul、Valut 以及 Terraform，另外还有 Vagrant 以及 Packer 两个开源工具，2020 年还推出了 Boundary 以及 Waypoint 两个新产品

HashiCorp 这家公司有一个显著特点，就是他们极其有耐心，并且极其重视“基础设施”的建设。例如，他们在思考 Terraform 配置文件该用 JSON 还是 YAML 时，对两者都不满意，所以他们宁可慢下来，花时间去设计了 HCL([HashiCorp Configuration Language](https://github.com/hashicorp/hcl))，使得他们对于声明式代码的可读性有了完全的掌控力。再比如在他们设计 Terraform 以及 Vault、Packer 时，他们使用的 go 语言因为是把引用代码下载下来后静态链接编译成单一可执行文件，所以不像 jar 或者 dll 那样有运行时动态加载插件的能力。因此他们又花时间开发了 [go-plugin](https://github.com/hashicorp/go-plugin) 这个项目，把插件编译成一个独立进程，与主进程通过 rpc 进行互操作。该项目上的投资很好地支撑了 Terraform、Vault、Packer 项目的插件机制，进而演化出如今百花齐放的 HashiCorp 开源生态。



Terraform 的生态环境到了今天，已经发展为三个分支，分别是：

- 开源版
- Terraform Cloud 云服务版
- Terraform 企业版









#### 初体验

安装：

```bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository -y "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install -y terraform
```





```bash
# 验证
terraform version
terraform -help

```



例子：

创建一个干净的空文件夹，在里面创建一个main.tf文件(tf就是Terraform，Terraform代码大部分是.tf文件，语法是HCL，当然目前也支持JSON格式的Terraform代码，但我们暂时只以tf为例)：

```sql
# 声明了这段代码所需要的Terraform版本以及UCloud插件版本
terraform {
  required_version = "~>0.13.5"
  required_providers {
    ucloud = {
      source  = "ucloud/ucloud"
      version = "~>1.22.0"
    }
  }
}

provider "ucloud" {
  public_key  = "JInqRnkSY8eAmxKFRxW9kVANYThg1pcvjD2Aw5f5p"
  private_key = "IlJn6GlmanYI1iDVEtrPyt5R9noAGz41B8q5TML7abqD8e4YjVdylwaKWdY61J5TcA"
  project_id  = "org-tgqbvi"
  region      = "cn-bj2"
}

# 真正定义云端基础设施的代码就是后面的部分，分为三部分，data、resource和output。

# data代表利用UCloud插件定义的data模型对UCloud进行查询，例如我们在代码中利用data查询cn-bj2-04机房UCloud官方提供的CentOS 6.5 x64主机镜像的id，以及官方提供的默认Web服务器适用的安全组(可以理解成防火墙)的id，这样我们就不需要人工在界面上去查询相关id，再硬编码到代码中。
data "ucloud_security_groups" "default" {
  type = "recommend_web"
}

data "ucloud_images" "default" {
  availability_zone = "cn-bj2-04"
  name_regex        = "^CentOS 6.5 64"
  image_type        = "base"
}

# resource代表我们需要在云端创建的资源，在例子里我们创建了三个资源，分别是主机、弹性公网ip，以及主机和公网ip的绑定。

resource "ucloud_instance" "web" {
  availability_zone = "cn-bj2-04"
  image_id          = data.ucloud_images.default.images[0].id
  instance_type     = "n-basic-2"
  root_password     = "supersecret1234"
  name              = "tf-example-instance"
  tag               = "tf-example"
  boot_disk_type    = "cloud_ssd"

  security_group = data.ucloud_security_groups.default.security_groups[0].id

  delete_disks_with_instance = true

  user_data = <<EOF
#!/bin/bash
yum install -y nginx
service nginx start
EOF
}
# 我们在定义主机时给定了主机的尺寸、系统盘类型等关键信息，并且通过user_data定义了第一次开机时所要执行的初始化脚本，在脚本中我们在这台CentOS服务器上安装了nginx服务并启动之。
resource "ucloud_eip" "web-eip" {
  internet_type = "bgp"
  charge_mode   = "bandwidth"
  charge_type   = "dynamic"
  name          = "web-eip"
}

resource "ucloud_eip_association" "web-eip-association" {
  eip_id      = ucloud_eip.web-eip.id
  resource_id = ucloud_instance.web.id
}

output "eip" {
  value = ucloud_eip.web-eip.public_ip
}
```



```shell
 terraform init
 # 初始化操作，通过官方插件仓库下载对应操作系统的UCloud插件
 
 terraform plan
 # 预览一下代码即将产生的变更
 
 $ terraform apply
 # 运行， Terraform会首先重新计算一下变更计划，并且像刚才执行plan命令那样把变更计划打印给我们，要求我们人工确认。让我们输入yes
 
 terraform destroy
 # 清理
```















#### 基础概念

##### provider

Terraform被设计成一个多云基础设施编排工具，不像CloudFormation那样绑定AWS平台，Terraform可以同时编排各种云平台或是其他基础设施的资源。Terraform实现多云编排的方法就**是Provider插件机制**。

Terraform使用的是HashiCorp自研的go-plugin库(https://github.com/hashicorp/go-plugin)，本质上各个Provider插件都是独立的进程，与Terraform进程之间通过rpc进行调用。Terraform引擎首先读取并分析用户编写的Terraform代码，**形成一个由data与resource组成的图(Graph)**，再通过rpc调用这些data与resource所对应的Provider插件；Provider插件的编写者根据Terraform所制定的插件框架来定义各种data和resource，并实现相应的CRUD方法；在实现这些CRUD方法时，可以调用目标平台提供的SDK，或是直接通过调用Http(s) API来操作目标平台。

##### 状态管理

我们在第一章的末尾提过，当我们成功地执行了一次`terraform apply`，创建了期望的基础设施以后，我们如果再次执行`terraform apply`，生成的新的执行计划将不会包含任何变更，Terraform会记住当前基础设施的状态，并将之与代码所描述的期望状态进行比对。第二次apply时，因为当前状态已经与代码描述的状态一致了，所以会生成一个空的执行计划。

Terraform引入了一个独特的概念——状态管理，这是Ansible等配置管理工具或是自研工具调用SDK操作基础设施的方案所没有的。简单来说，Terraform将每次执行基础设施变更操作时的状态信息保存在一个状态文件中，默认情况下会保存在当前工作目录下的`terraform.tfstate`文件里

极其重要的安全警示——tfstate是明文的





Consul是HashiCorp推出的一个开源工具，主要用来解决服务发现、配置中心以及Service Mesh等问题；Consul本身也提供了类似ZooKeeper、Etcd这样的分布式键值存储服务，具有基于Gossip协议的最终一致性，所以可以被用来充当Terraform Backend存储。







#### terraform编程

Terraform早期仅支持使用HCL(Hashicorp Configuration Language)语法的.tf文件，近些年来也开始支持JSON。HashiCorp甚至修改了他们的json解析器，使得他们的json可以支持注释，但HCL相比起JSON来说有着更好的可读性

##### 类型

原始类型分三类：`string`、`number`、`bool`。

- `string` 代表一组 Unicode 字符串，例如：`"hello"`。
- `number` 代表数字，可以为整数，也可以为小数。
- `bool` 代表布尔值，要么为 `true`，要么为 `false`。`bool` 值可以被用做逻辑判断。

`number` 和 `bool` 都可以和 `string` 进行隐式转换，当我们把 `number` 或 `bool` 类型的值赋给 `string` 类型的值，或是反过来时，Terraform 会自动替我们转换类型，其中：

- `true` 值会被转换为`"true"`，反之亦然
- `false` 值会被转换为`"false"`，反之亦然
- `15` 会被转换为 `"15"`，`3.1415` 会被转换为 `"3.1415"`，反之亦然

复杂类型是一组值所组成的符合类型，有两类复杂类型。

一种是集合类型。一个集合包含了一组同一类型的值。集合内元素的类型成为元素类型。一个集合变量在构造时必须确定集合类型。集合内所有元素的类型必须相同。

Terraform 支持三种集合：

- `list(...)`：列表是一组值的连续集合，可以用下标访问内部元素，下标从 `0` 开始。例如名为 `l` 的 `list`，`l[0]` 就是第一个元素。`list` 类型的声明可以是 `list(number)`、`list(string)`、`list(bool)`等，括号中的类型即为元素类型。
- `map(...)`：字典类型(或者叫映射类型)，代表一组键唯一的键值对，键类型必须是 `string`，值类型任意。`map(number)` 代表键为 `string` 类型而值为 `number` 类型，其余类推。`map` 值有两种声明方式，一种是类似 `{"foo": "bar", "bar": "baz"}`，另一种是 `{foo="bar", bar="baz"}`。键可以不用双引号，但如果键是以数字开头则例外。多对键值对之间要用逗号分隔，也可以用换行符分隔。推荐使用 `=` 号(Terraform 代码规范中规定按等号对齐，使用等号会使得代码在格式化后更加美观)
- `set(...)`：集合类型，代表一组不重复的值。

第二种复杂类型是结构化类型。一个结构化类型允许多个不同类型的值组成一个类型。结构化类型需要提供一个 `schema` 结构信息作为参数来指明元素的结构。



`any` 是 Terraform 中非常特殊的一种类型约束，它本身并非一个类型，而只是一个占位符。每当一个值被赋予一个由 `any` 约束的复杂类型时，Terraform 会尝试计算出一个最精确的类型来取代 `any`。



存在一种特殊值是无类型的，那就是 `null`。`null` 代表数据缺失。如果我们把一个参数设置为 `null`，Terraform 会认为你忘记为它赋值。如果该参数有默认值，那么 Terraform 会使用默认值；如果没有又恰巧该参数是必填字短，Terraform 会报错。`null` 在条件表达式中非常有用，你可以在某项条件不满足时跳过对某参数的赋值。

##### 资源

资源通过resource块来定义，一个resource可以定义一个或多个基础设施资源对象，例如VPC、虚拟机，或是DNS记录、Consul的键值对数据等。



语法：

resource块定义单个资源对象：

```tex
resource "aws_instance" "web" {
  ami           = "ami-a1b2c3d4"
  instance_type = "t2.micro"
}
```

紧跟resource关键字的是资源类型，在上面的例子里就是`aws_instance`。后面是资源的Local Name，例子里就是`web`。Local Name可以在同一模块内的代码里被用来引用该资源，但类型加Local Name的组合在当前模块内必须是唯一的，不同类型的两个资源Local Name可以相同。随后的花括号内的内容就是块体，创建资源所用到的各种参数的值就在块体内定义。例子中我们定义了虚拟机所使用的镜像id以及虚拟机的尺寸。



不同资源定义了不同的可赋值的属性，官方文档将之称为参数(Argument)，有些参数是必填的，有些参数是可选的。使用某项资源前可以通过阅读相关文档了解参数列表以及他们的含义、赋值的约束条件。

参数值可以是简单的字面量，也可以是一个复杂的表达式。



每一个Terraform Provider都有自己的文档，用以描述它所支持的资源类型种类，以及每种资源类型所支持的属性列表。

大部分公共的Provider都是通过[Terraform Registry](https://registry.terraform.io/browse/providers)连带文档一起发布的。当我们在Terraform Registry站点上浏览一个Provider的页面时，我们可以点击"Documentation"链接来浏览相关文档。Provider的文档都是版本化的，我们可以选择特定版本的Provider文档。





资源行为：

一个resource块声明了作者想要创建的一个确切的基础设施对象，并且设定了各项属性的值。如果我们正在编写一个新的Terraform代码文件，那么代码所定义的资源仅仅只在代码中存在，并没有与之对应的实际的基础设施资源存在。

对一组Terraform代码执行terraform apply可以创建、更新或者销毁实际的基础设施对象，Terraform会制定并执行变更计划，以使得实际的基础设施符合代码的定义。



##### 数据源

数据源允许查询或计算一些数据以供其他地方使用。使用数据源可以使得Terraform代码使用在Terraform管理范围之外的一些信息，或者是读取其他Terraform代码保存的状态。

数据源通过一种特殊的资源访问：data资源。数据源通过data块声明：

```hcl
data "aws_ami" "example" {
  most_recent = true

  owners = ["self"]
  tags = {
    Name   = "app-server"
    Tested = "true"
  }
}
```



#### 模块

简单来讲模块就是包含一组Terraform代码的文件夹

Terraform模块是编写高质量Terraform代码，提升代码复用性的重要手段，可以说，一个成熟的生产环境应该是由数个可信成熟的模块组装而成的

实际上所有包含Terraform代码文件的文件夹都是一个Terraform模块。我们如果直接在一个文件夹内执行`terraform apply`或者`terraform plan`命令，那么当前所在的文件夹就被称为根模块(root module)。我们也可以在执行Terraform命令时通过命令行参数指定根模块的路径。

一个最小化模块推荐的结构是这样的：

```bash
$ tree minimal-module/
.
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
```





在 Terraform 代码中引用一个模块，使用的是 `module` 块。

每当在代码中新增、删除或者修改一个 `module` 块之后，都要执行 `terraform init` 或是 `terraform get` 命令来获取模块代码并安装到本地磁盘上





#### 命令行

Terraform是用Go语言编写的，所以它的交付物只有一个可执行命令行文件：terraform。在Terraform执行发生错误时，terraform进程会返回一个非零值，所以在脚本代码中我们可以轻松判断执行是否成功。





















