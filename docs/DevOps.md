# DevOps Notes





## Ansible

自动化运维工具

### Ansible Notes

#### What's Ansible

ansible是新出现的自动化运维工具，基于Python开发，集合了众多运维工具（puppet、chef、func、fabric）的优点，实现了批量系统配置、批量程序部署、批量运行命令等功能。

ansible是基于 paramiko 开发的,并且基于模块化工作，本身没有批量部署的能力。**真正具有批量部署的是ansible所运行的模块，ansible只是提供一种框架**。ansible**不需要在远程主机上安装client/agents，因为它们是基于ssh来和远**
**程主机通讯的**。ansible目前已经已经被红帽官方收购，是自动化运维工具中大家认可度最高的，并且上手容易，学习简单。是每位运维工程师必须掌握的技能之一。

#### 特点

1. 部署**简单**，只需在主控端部署Ansible环境，被控端无需做任何操作；
2. 默认使用**SSH**协议对设备进行管理；
3. 有**大量常规运维操作模块**，可实现日常绝大部分操作；
4. 配置简单、功能强大、扩展性强；
5. 支持API及自定义模块，可通过Python轻松扩展；
6. 通过**Playbooks**来定制强大的配置、状态管理；
7. 轻量级，无需在客户端安装agent，更新时，只需在操作机上进行一次更新即可；
8. 提供一个功能强大、操作性强的Web管理界面和REST API接口——AWX平台。

#### 架构图

![img](_images/DevOps.asserts/1204916-20171205163000628-69838828.png)

主要模块如下：

> `Ansible`：Ansible核心程序。
> `HostInventory`：记录由Ansible管理的主机信息，包括端口、密码、ip等。
> `Playbooks`：“剧本”YAML格式文件，多个任务定义在一个文件中，定义主机需要调用哪些模块来完成的功能。
> `CoreModules`：**核心模块**，主要操作是通过调用核心模块来完成管理任务。
> `CustomModules`：自定义模块，完成核心模块无法完成的功能，支持多种语言。
> `ConnectionPlugins`：连接插件，Ansible和Host通信使用





#### 安装

```shell
apt-get install ansible

# pip
pip install ansible
```





https://www.cnblogs.com/keerya/p/7987886.html





### Official Tutorial















