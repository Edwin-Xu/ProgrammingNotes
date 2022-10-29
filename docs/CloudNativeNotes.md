# Cloud Native

## Terraform

### 概述

#### 什么是Terraform

Terraform 是由 HashiCorp 创立的开源“**基础架构即代码**”工具。

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



### 教程学习

https://lonegunmanb.github.io/introduction-terraform/

#### 介绍

AWS AWSome Day中，用一段JSON代码就可以让我们用指定的镜像 id 创建一台云端虚拟机，不需要在界面上点点点。要知道在当时，我正在一家初创公司工作，同时身兼架构师、后台开发程序员、DBA 以及运维数职，要维护测试、预发布以及生产三套环境，时不时还因为要去修复因环境之间配置不一致而引发的种种错误而焦头烂额，那时的我就很期待 CloudFormation 能够给予我这种能够批量创建并管理"招之能来，来之能战，战之能胜，胜之能去"的环境的能力。

我当时并不知道在西雅图的华盛顿大学，有一个美日混血大帅哥 Mitchell Hashimoto 和他的老板 Armon Dagar 也深深沉迷于 CloudFormation 所带来的那种优雅与高效，同时他们也在头疼 CloudFormation 本身的一系列问题，最主要的就是它是 AWS 独占的。**<u>强人和我这种庸人最大的区别就是，强人有了想法直接就去做</u>**，Mitchell 和 Armon 在讨论中渐渐有了一个想法——打造一个多云(Multi-Cloud)的开源的基础设施即代码(IaC)工具，并且要超越 CloudFormation。他们组建了一家名为 **HashiCorp** 的公司来实现这个目标

在今年3月，HashiCorp 宣布成功获得 1.75 亿美元的E轮融资，投后公司估值 51 亿美元。HashiCorp 的产品线主要有 Nomad、Consul、Valut 以及 Terraform，另外还有 Vagrant 以及 Packer 两个开源工具，2020 年还推出了 Boundary 以及 Waypoint 两个新产品

HashiCorp 这家公司有一个显著特点，就是他们极其有耐心，并且极其重视“基础设施”的建设。例如，他们在思考 Terraform 配置文件该用 JSON 还是 YAML 时，对两者都不满意，所以他们宁可慢下来，花时间去设计了 HCL([HashiCorp Configuration Language](https://github.com/hashicorp/hcl))，使得他们对于声明式代码的可读性有了完全的掌控力。再比如在他们设计 Terraform 以及 Vault、Packer 时，他们使用的 go 语言因为是把引用代码下载下来后静态链接编译成单一可执行文件，所以不像 jar 或者 dll 那样有运行时动态加载插件的能力。因此他们又花时间开发了 [go-plugin](https://github.com/hashicorp/go-plugin) 这个项目，把插件编译成一个独立进程，与主进程通过 rpc 进行互操作。该项目上的投资很好地支撑了 Terraform、Vault、Packer 项目的插件机制，进而演化出如今百花齐放的 HashiCorp 开源生态。



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

Terraform使用的是HashiCorp自研的go-plugin库(https://github.com/hashicorp/go-plugin)，本质上各个Provider插件都是独立的进程，与Terraform进程之间通过rpc进行调用。Terraform引擎首先读取并分析用户编写的Terraform代码，形成一个由data与resource组成的图(Graph)，再通过rpc调用这些data与resource所对应的Provider插件；Provider插件的编写者根据Terraform所制定的插件框架来定义各种data和resource，并实现相应的CRUD方法；在实现这些CRUD方法时，可以调用目标平台提供的SDK，或是直接通过调用Http(s) API来操作目标平台。





















