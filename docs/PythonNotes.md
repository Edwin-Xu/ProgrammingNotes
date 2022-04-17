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



## Problems

### SSL3_GET_SERVER_CERTIFICATE

SSL3_GET_SERVER_CERTIFICATE:certificate verify failed'),)) - skipping



pip --trusted-host pypi.tuna.tsinghua.edu.cn install requests

















