# MacNotes



# 介绍

## 基本使用

### 包管理器 brew



/Users/txu6/Desktop/apps/ossutil/ossutilmac64 cp oss://trip-fintech-ai/upload/txu6/win2mac/ ./ -r --config-file /Users/txu6/Desktop/apps/ossutil/trip_fintech_ai_ossutilconfig

/Users/txu6/Desktop/apps/ossutil/ossutilmac64 cp oss://trip-fintech-ai/upload/txu6/st/gao/ ./ -r --config-file /Users/txu6/Desktop/apps/ossutil/trip_fintech_ai_ossutilconfig





### terminal

### Iterms2

https://blog.csdn.net/THMAIL/article/details/126571892

```
command + enter 进入与返回全屏模式
command + t 新建标签
command + w 关闭标签
command + 数字 command + 左右方向键    切换标签
command + enter 切换全屏
command + f 查找
command + d 水平分屏
command + shift + d 垂直分屏
command + option + 方向键 command + [ 或 command + ]    切换屏幕
command + ; 查看历史命令
command + shift + h 查看剪贴板历史
ctrl + u    清除当前行
ctrl + l    清屏
ctrl + a    到行首
ctrl + e    到行尾
ctrl + f/b  前进后退
ctrl + p    上一条命令
ctrl + r    搜索命令历史
```





### zsh

zsh-autosuggestions





## 命令工具

### autojump

j 跳转





# 最佳使用实践

## alias

```shell
sudo vim ~/.zshrc

alias ll='ls -la'
alias commit="git commit -m "
alias push="git push origin "
alias add="git add ."
alias fetch="git fetch origin master --depth 100"
alias time="date '+%Y-%m-%d %H:%M:%S'"
alias now="date '+%Y-%m-%d'"
alias edw="jo /Users/txu6/Desktop/edwinxu"
alias ct="jo /Users/txu6/Desktop/ctrip/projects"
alias fp="open /Users/txu6/Desktop/edwinxu/projects/edw_n/股票/复盘/每日复盘.xlsm"
alias ss="ssh txu6@jumpserver.ops.ctripcorp.com"
alias zshe="open ~/.zshrc"
alias merge="git merge origin master"

source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

[ -f /opt/homebrew/etc/profile.d/autojump.sh ] && . /opt/homebrew/etc/profile.d/autojump.sh



# git multi remove repo
source ~/.bashrc
```





