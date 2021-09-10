# Linux

## 命令学习

- du df
- ln
- which(在path中搜索可执行文件) vs. whereis(搜索程序、二进制)
- chown
- chmod
- chgrp
- su vs sudo: 推荐sudo?
- curl: mock http
- wget: 下载文件，是curl的子集
- ping:Packet Internet Groper
- host
- nc: tcp udp发包
- netstat
- telnet:查看网络连接
- tcpdump 网络抓包工具
- 
- ssh  远程登录
- scp 远程拷贝
- ps
- free 内存使用
- top  CPU使用率 内存信息 进程信息等
- kill ： ctrl+c即信号2
- 



## 进程管理

### pstree

打印进程树

| -a   | 显示启动每个进程对应的完整指令，包括启动进程的路径、参数等。 |
| ---- | ------------------------------------------------------------ |
| -c   | 不使用精简法显示进程信息，即显示的进程中包含子进程和父进程。 |
| -n   | 根据进程 PID 号来排序输出，默认是以程序名排序输出的。        |
| -p   | 显示进程的 PID。                                             |
| -u   | 显示进程对应的用户名称。                                     |

需要注意的是，在使用 pstree 命令时，如果不指定进程的 PID 号，也不指定用户名称，则会以 init 进程为根进程，显示系统中所有程序和进程的信息；反之，若指定 PID 号或用户名，则将以 PID 或指定命令为根进程，显示 PID 或用户对应的所有程序和进程。

**init 进程是系统启动的第一个进程，进程的 PID 是 1**，也是系统中所有进程的父进程。





## shell

```
定义数组：arr =(v1 v2)
读取数组： ${ar[0]}
@或*可以获取数组中所有的元素


```



参数

$N : 

- 0：文件名
- 1：第一个参数，依次类推
- $# : 参数个数
- $*:以一个单字符串显示所有的参数
- $@: 同上* , 不过使用时需要添加引号，并在引号中返回每个参数 



流程控制：

- if
- for
- while
- until
- case esac
- break continue
- 



函数

```
[function] funcname[(param)]

{

 action

}
```





- xargs:

将参数列表转换为小块分段传递给其他命令

command | xargs

- alias
- crontab
- rsync
- iostat
- vmstat
- atnodes
- tonodes
- 

## 环境变量

Linux是一个多用户多任务的操作系统，可以在Linux中为不同的用户设置不同的运行环境，具体做法是设置不同用户的环境变量。

### 分类

一、按照**生命周期**来分，Linux环境变量可以分为两类：
 1、**永久的**：需要用户修改相关的配置文件，变量永久生效。
 2、**临时的**：用户利用**export**命令，**在当前终端下声明环境变量，关闭Shell终端失效。**

二、按照**作用域**来分，Linux环境变量可以分为：
 1、**系统环境变量**：系统环境变量**对该系统中所有用户**都有效。
 2、**用户环境变量**：顾名思义，这种类型的环境变量**只对特定的用户有效**。

### Linux设置环境变量

#### 系统环境变量

在`/etc/profile`文件中添加变量 **对所有用户生效（永久的）**

```bash
 export CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jre/lib
```

修改文件后要想马上生效还要运行`source /etc/profile`不然只能在下次重进此用户时生效。

#### 用户环境变量

在用户目录下的.bash_profile文件中增加变量 **对单一用户生效（永久的）**

```bash
vim ~/.bash.profile
export CLASSPATH=./JAVA_HOME/lib;$JAVA_HOME/jre/lib
```

修改文件后要想马上生效还要运行$ source ~/.bash_profile不然只能在下次重进此用户时生效。

#### 临时环境变量

直接运行export命令定义变量 **【只对当前shell（BASH）有效（临时的）】**

### Linux环境变量的使用

#### 常见环境变量

- PATH：**指定命令的搜索路径**

  ```bash
  PATH=$PAHT:<PATH 1>:<PATH 2>:<PATH 3>:--------:< PATH n >
  export PATH
  ```

  中间用冒号隔开。环境变量更改后，在用户下次登陆时生效。

  `echo $PATH` 查看

- HOME：指定用户的主工作目录（即用户登陆到Linux系统中时，默认的目录）。

- HISTSIZE：指保存历史命令记录的条数。

- LOGNAME：指当前用户的登录名。

- HOSTNAME：指主机的名称，许多应用程序如果要用到主机名的话，通常是从这个环境变量中来取得的

- SHELL：指当前用户用的是哪种Shell。

- LANG/LANGUGE：和语言相关的环境变量，使用多种语言的用户可以修改此环境变量。

- MAIL：指当前用户的邮件存放目录。

#### 查看和修改命令

- echo         显示某个环境变量值 echo $PATH

- export   设置一个新的环境变量 export HELLO="hello" (可以无引号)

- env      显示所有环境变量

- set      显示本地定义的shell变量

- unset        清除环境变量 unset HELLO

- readonly     设置只读环境变量 readonly HELLO







## 目录结构

- usr: Not user的缩写，Unix Software Resource的缩写
- /home：普通用户的主目录

在shell的命令行下直接使用`export 变量名=变量值`
 定义变量，该变量只在当前的shell（BASH）或其子shell（BASH）下是有效的，shell关闭了，变量也就失效了，再打开新shell时就没有这个变量，需要使用的话还需要重新定义。



### 文件权限

Linux的权限不是很细致，只有RWX三种
r(Read，读取)：对文件而言，具有读取文件内容的权限；对目录来说，具有浏览目录的权限。
w(Write,写入)：对文件而言，具有新增,修改,删除文件内容的权限；对目录来说，具有新建，删除，修改，移动目录内文件的权限。
x(eXecute，执行)：对文件而言，具有执行文件的权限；**对目录了来说该用户具有进入目录的权限**（**当前用户无执行权限时不能cd到该目录**）。
1、目录的只读访问不允许使用cd进入目录，必须要有执行的权限才能进入。
2、只有执行权限只能进入目录，不能看到目录下的内容，要想看到目录下的文件名和目录名，需要可读权限。
3、一个文件能不能被删除，主要看该文件所在的目录对用户是否具有写权限，如果目录对用户没有写权限，则该目录下的所有文件都不能被删除，文件所有者除外
4、目录的w位不设置，即使你拥有目录种某文件的w权限也不能写该文件

特殊文件权限：

- setuid
- setgid
- sticky粘滞位：只能文件创建者和root可以删除，对目录有效文件无效，只限删除操作

## 包管理

### apt-get

**apt-get命令**是**Debian** Linux发行版中的APT软件包管理工具。所有基于Debian的发行都使用这个包管理系统。deb包可以把一个应用的文件包在一起，大体就如同Windows上的安装文件。

```bash
apt-get(选项)(参数)
```

使用apt-get命令的第一步就是引入必需的软件库，Debian的软件库也就是所有Debian软件包的集合，它们存在互联网上的一些公共站点上。把它们的地址加入，apt-get就能搜索到我们想要的软件。**/etc/apt/sources.list**是存放这些地址列表的配置文件

```bash
apt-get update # 在修改/etc/apt/sources.list或者/etc/apt/preferences之后运行该命令。此外您需要定期运行这一命令以确保您的软件包列表是最新的
apt-get install packagename
apt-get remove packagename # 卸载一个已安装的软件包（保留配置文件）
apt-get –purge remove packagename # 卸载一个已安装的软件包（删除配置文件）
apt-get autoclean apt # 会把已装或已卸的软件都备份在硬盘上，所以如果需要空间的话，可以让这个命令来删除你已经删掉的软件
apt-get clean # 更新所有已安装的软件包
apt-get upgrade # 更新所有已安装的软件包
apt-get dist-upgrade # 将系统升级到新版本
apt-get autoclean # 定期运行这个命令来清除那些已经卸载的软件包的.deb文件。通过这种方式，您可以释放大量的磁盘空间。如果您的需求十分迫切，可以使用apt-get clean以释放更多空间。这个命令会将已安装软件包裹的.deb文件一并删除。大多数情况下您不会再用到这些.debs文件
```





## 打包与压缩

tar: 打包，没有压缩

tar.gz; 打包，gzip压缩



```bash
tar -cvf a.tar a # 压缩
tar -xvf a.tar # 打包
```



## shell

- bin/sh:  bourne shell
- bin/bash: bbourne again shell
- /usr/bin/sh: C shell
- /usr/bin/ksh: K shell
- /sbin/sh: shell for root



$()\$  和反引号` 都可以将命令执行结果赋值给变量



unset 删除变量

readonly 只读变量



### 注释

当行注释：#

多行注释1： 

```bash
: '  comments '
# :后面有一个space
```





### 字符串操作

```bash
$(str:0:4)
可以截取、匹配、返回长度等
$(str#*//)

```

## 传参

-$# 参数个数





## ENV

临时环境变量：使用export声明即可

```bash
export qunar=val
```

永久ENV

/ect/profile中使用export声明，对所有用户生效

~/.bash_profile只对自己生效

```bash
export PATH=$JAVA_HOME$/bin
```

















