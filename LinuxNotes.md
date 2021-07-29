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



## 目录结构

- usr: Not user的缩写，Unix Software Resource的缩写
- /home：普通用户的主目录



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

















