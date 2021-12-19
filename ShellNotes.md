# Shell Notes

## BASIC NOTES



数字大小比较**不能用**=  !=  <  >等,要用-eq -ne -lt -gt等.



**set -u （检查脚本内的变量，如果有变量未被定义将终止脚本）（脚本的自检测功能）**





bc   数值计算

在计算和if判断上花了不少时间

string使用 == 等比较

整数使用 -eq -ne等比较

小数无法直接比较使用expr 表达式

或者使用bc计算







### 异常自动退出

如果出现异常，退出shell，不继续执行

set -e

你写的每一个脚本的开始都应该包含set -e。这告诉bash一但有任何一个语句返回非真的值，则退出bash。

使用-e的好处是避免错误滚雪球般的变成严重错误，能尽早的捕获错误。更加可读的版本：set -o errexit 

使用-e把你从检查错误中解放出来。如果你忘记了检查，bash会替你做这件事。

不过你也没有办法使用$? 来获取命令执行状态了，因为bash无法获得任何非0的返回值。



command:
command ||  （echo "command failed"; exit 1） ; 



### 基本语法

#### if

双方括号[[ ]]：表示高级字符串处理函数

```shell
dt='PARTITIONED BY ( `dt`'
createTbl01='str'

isTbl01PartitionedByDt=false
if [[ ${createTbl01} == *${dt}* ]]
then
	isTbl01PartitionedByDt=false
fi
```





