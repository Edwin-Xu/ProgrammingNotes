# Python Notes

## BASIC NOTES

### \_\_name\_\_=='\_\_main\_\_'

一般情况下，当我们写完自定义的模块之后，都会写一个测试代码，检验一些模块中各个功能是否能够成功运行。例如，创建一个 candf.py 文件，并编写如下代码：

```python
'''
摄氏度和华氏度的相互转换模块
'''
def c2f(cel):
    fah = cel * 1.8 + 32
    return fah
def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel
def test():
    print("测试数据：0 摄氏度 = %.2f 华氏度" % c2f(0))
    print("测试数据：0 华氏度 = %.2f 摄氏度" % f2c(0))
test()
```

在 candf.py 模块文件的基础上，在同目录下再创建一个 demo.py 文件，并编写如下代码：

```python
import candf
print("32 摄氏度 = %.2f 华氏度" % candf.c2f(32))
print("99 华氏度 = %.2f 摄氏度" % candf.f2c(99))
```

运行 demo.py 文件，其运行结果如下所示：

```text
测试数据：0 摄氏度 = 32.00 华氏度
测试数据：0 华氏度 = -17.78 摄氏度
32 摄氏度 = 89.60 华氏度
99 华氏度 = 37.22 摄氏度
```

解释器将模块（candf.py）中的测试代码也一块儿运行了，这并不是我们想要的结果。想要避免这种情况的关键在于，**要让 Python 解释器知道，当前要运行的程度代码，是模块文件本身，还是导入模块的其它程序。**

为了实现这一点，就需要使用 Python 内置的系统变量 __name__，它用于标识所在模块的模块名。例如，在 demo.py 程序文件中，添加如下代码：

```python
print(__name__)
print(candf.__name__)
其运行结果为：
__main__
candf
```

`if __name__ == '__main__':` 的作用是确保只有单独运行该模块时，此表达式才成立，才可以进入此判断语法，执行其中的测试代码；反之，如果只是作为模块导入到其他程序文件中，则此表达式将不成立，运行其它程序时，也就不会执行该判断语句中的测试代码。

### python -m

将库中的python模块用作脚本去运行。

```shell
python -m SimpleHTTPServer    #python2中启动一个简单的http服务器
python -m http.server    #python3中启动一个简单的http服务器
```

将模块当做脚本去启动有什么用？

1. python xxx.py
2. python -m xxx.py

这是两种加载py文件的方式:
1叫做直接运行
2相当于import,叫做当做模块来启动

 

不同的加载py文件的方式，主要是影响sys.path这个属性。sys.path相当于Linux中的PATH

### 镜像源

pip install xxx -i http://xxx



pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple



### \_pycache_

Python程序运行时不需要编译成二进制代码，而直接从源码运行程序，简单来说是，Python解释器将源码转换为字节码，然后再由解释器来执行这些字节码。

解释器的具体工作：
1、完成模块的加载和链接；
2、将源代码编译为PyCodeObject对象(即字节码)，写入内存中，供CPU读取；
3、从内存中读取并执行，结束后将PyCodeObject写回硬盘当中，也就是复制到**<u>.pyc</u>**或.pyo文件中，以保存当前目录下所有脚本的字节码文件。
**之后若再次执行该脚本，它先检查【本地是否有上述字节码文件】和【该字节码文件的修改时间是否在其源文件之后】，是就直接执行，否则重复上述步骤**

那有的小伙伴就有疑问了，__pycache__文件夹的意义何在呢？
因为第一次执行代码的时候，Python解释器已经把编译的字节码放在__pycache__文件夹中，这样以后再次运行的话，如果被调用的模块未发生改变，那就直接跳过编译这一步，直接去__pycache__文件夹中去运行相关的 *.pyc 文件，大大缩短了项目运行前的准备时间。






## 库和工具

### subprocess

从Python 2.4开始，Python引入subprocess模块来管理子进程，以取代一些旧模块的方法：如 os.system、os.spawn*、os.popen*、popen2.*、commands.*不但可以调用外部的命令作为子进程，而且可以连接到子进程的input/output/error管道，获取相关的返回信息

运行python的时候，我们都是在创建并运行一个进程。像Linux进程那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序。
 subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。



subprocess.call()

父进程等待子进程完成
返回退出信息(returncode，相当于Linux exit code)



subprocess.check_call()

父进程等待子进程完成
 返回0
 检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try…except…来检查



subprocess.check_output()

父进程等待子进程完成
 返回子进程向标准输出的输出结果
 检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try…except…来检查。

```ruby
>>> import subprocess
>>> retcode = subprocess.call(["ls", "-l"])
#和shell中命令ls -a显示结果一样
>>> print retcode
0
```

```python
>>> retcode = subprocess.call("ls -l",shell=True)
```



subprocess.Popen()

```rust
class Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
```

实际上，上面的几个函数都是基于Popen()的封装(wrapper)。这些封装的目的在于让我们容易使用子进程。当我们想要更个性化我们的需求的时候，就要转向Popen类，该类生成的对象用来代表子进程。

与上面的封装不同，Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)，







## Problems

### SSL3_GET_SERVER_CERTIFICATE

SSL3_GET_SERVER_CERTIFICATE:certificate verify failed'),)) - skipping



pip --trusted-host pypi.tuna.tsinghua.edu.cn install requests



### OSError: [Errno 99]

OSError: [Errno 99] Cannot assign requested address

对于 Docker 容器，您需要运行它们`network_mode: host`以使用主机的网络 systemd，或者您需要绑定到容器的 IP 地址。您不能从容器绑定到主机的 IP 地址，除非使用 `network_mode: host`! 但是您可以从主机转发端口，绑定到特定的 IP 地址。









