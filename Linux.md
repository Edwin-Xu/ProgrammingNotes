# Linux

## 命令学习

- du df
- ln
- which
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

[function] funcname[(param)]

{

 action

}



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

