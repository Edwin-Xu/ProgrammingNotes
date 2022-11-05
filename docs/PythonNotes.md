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

### os

#### os.walk()

os.walk()主要用来扫描某个指定目录下所包含的子目录和文件。

```python
for curDir, dirs, files in os.walk("test"):
    print("====================")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(dirs))
    print("该目录下包含的文件：" + str(files))
```

上面的代码在扫描子目录和文件的时候，是采用自顶向下的方式进行扫描。如果想要自底向上地扫描子目录和文件，可以添加上topdown=False参数

我们还可以利用os.walk输出test文件夹下所有的文件

```
for curDir, dirs, files in os.walk("test"):
    for file in files:
        print(os.path.join(curDir, file))
```

也可以利用os.walk输出test文件夹下所有的子目录



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



#### windows

FileNotFoundError: [WinError 2] 系统找不到指定的文件。

0x02 原因：

`dir` 命令是`cmd.exe` 或者`powershell.exe`才能理解的命令。在**Windows**环境下`subprocess.Popen`默认是不会调用`cmd.exe`的。所以需要指定。

> subprocess.Popen(["cmd", "/c", "dir", "c:\\Users"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)



如果是 其他命令中使用到了 popen，则没办法使用了，比如conda中虚拟环境中的执行pip





## jupyter

### 虚拟环境

既然有虚拟环境（Virtual Environment），那么有必要先解释一下，什么是环境。
这里的环境，指的就是 Python 代码的运行环境。它应该包含以下信息：（第 1 个是最主要的，后面 2 个基本是围绕它确定的）

- Python 解释器，用哪个解释器来执行代码？
- Python 库的位置，该去哪里 import 所需要的模块呢？
- 可执行程序的位置，比如说安装了 pip，那么 pip 命令是在哪里呢？

如果看了对安装后的文件夹的说明，应该很清楚了，就是：

1. python.exe
2. Lib 文件夹，包括其中的 site-packages
3. Scripts 文件夹



虚拟环境就是 Python 环境的一个副本。
虚拟环境是一个虚拟化、从电脑独立开辟出来的环境。通俗的来讲，虚拟环境就是借助虚拟机docker来把一部分内容独立出来，我们把这部分独立出来的东西称作“容器”，在这个容器中，我们可以只安装我们需要的依赖包，各个容器之间互相隔离，互不影响。
譬如，本次学习需要用到Django，我们可以做一个Django的虚拟环境，里面只需要安装Django相关包就可以了。



Anaconda创建、激活、退出、删除虚拟环境

```pyhton
#在原始控制台输入：，检测anaconda环境是否安装成功。输出conda版本为成功
conda --version
#查看当前存在哪些虚拟环境：
conda env list 或 conda info -e
#在未创建自己的虚拟环境之前，查看到的将是anaconda自带的base环境


#创建虚拟环境。使用管理员身份运行Anaconda Prompt，创建一个叫做“env_name”的python3.6的虚拟环境，在界面输入
conda create --name env_name python=3.6


#创建完成后，激活虚拟环境：
conda activate env_name
#如果显示例如：(env_name) C:\Users\ 代表已经进入虚拟环境，在这个状态下就可以安装你所需要的包了
#下一次进入虚拟环境依旧是从Anaconda Prompt进入，直接activate env_name激活即可。（如果忘记了名称我们可以先用conda env list查看一下）
#如果直接输入命令activate，如果后面什么参数都不加那么会进入anaconda自带的base环境


#在虚拟环境中，安装第三方包：
conda install package_name 或者 pip install package_name
#一次安装多个第三方包：
conda install package_name_1 package_name_2
#指定所安装的第三方包的版本：
conda install package_name=X.X
#更新package_name包：
conda update package_name
#在虚拟环境中，卸载第三方包：
conda remove package_name 或者 pip uninstall package_name
#要查看当前环境中所有安装了的包可以用
conda list

#在激活的虚拟环境内，可以打开python解释器：
python
#验证第三方包package_name是否安装成功：
import package_name
#退出python解释器：
exit()


#退出虚拟环境
conda deactivate
#切回root环境
activate root


#删除虚拟环境及下属所有包
conda remove --name env_name --all
#删除虚拟环境中的包：
conda remove --name env_name package_name


#分享环境，一个方法是给ta一个你环境的.yml文件。首先activate env_name激活要分享的环境，然后输入：将包信息存入yml文件中.
conda env export > environment.yml
#在当前工作目录下会生成一个environment.yml文件，小伙伴拿到environment.yml文件后，将该文件放在工作目录下，可以通过以下命令从该文件创建环境
conda env create -f environment.yml
```

### kernel

kernel在Jupyter中提供编程语言支持。（说白了，kernel就是编译器）
IPython是默认内核，支持Python编程语言。IPython是参考的Jupyter内核，提供了一个强大的**Python交互式计算环境**。
还有其他内核包括R、Julia等。所以除了Python之外，还可以在Jupyter中使用许多其他语言。

```
查看虚拟环境
conda env list

查看jupyter kernel
jupyter kernelspec list
```















































## project

### requirements.txt

很多 Python 项目中经常会包含一个 **requirements.txt** 文件，里面内容是项目的依赖包及其对应版本号的信息列表，即项目依赖关系清单，其作用是用来重新构建项目所需要的运行环境依赖，比如你从 GitHub 上 clone 了一个 Python 项目，通常你会先找到 requirements.txt 文件，然后运行命令 `pip install -r requirements.txt` 来安装该项目所依赖的包。

同样，你也可以在你的项目目录下运行命令 `pip freeze > requirements.txt` 来生成 requirements.txt 文件，以便他人重新安装项目所依赖的包。





## conda

https://zhuanlan.zhihu.com/p/350353990

```python
conda --create py36 python=3.6
conda env list
conada activate

```





python setup.py install





换源：

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```





## Problems

### SSL3_GET_SERVER_CERTIFICATE

SSL3_GET_SERVER_CERTIFICATE:certificate verify failed'),)) - skipping



pip --trusted-host pypi.tuna.tsinghua.edu.cn install requests



### OSError: [Errno 99]

OSError: [Errno 99] Cannot assign requested address

对于 Docker 容器，您需要运行它们`network_mode: host`以使用主机的网络 systemd，或者您需要绑定到容器的 IP 地址。您不能从容器绑定到主机的 IP 地址，除非使用 `network_mode: host`! 但是您可以从主机转发端口，绑定到特定的 IP 地址。









