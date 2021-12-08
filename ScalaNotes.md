# Scala Notes

[尚硅谷大数据技术之Scala](_pdf/bigdata/scala/尚硅谷大数据技术之Scala.pdf)



## 尚硅谷Scala笔记

### Scala概述

- Spark：新一代内存级大数据计算框架
- 

#### 特点

- 基于JVM：Scala源代码.scala被编译为字节码
- 多范式：OOP + 函数式编程
- 静态语言
- 强类型

### 基础语法

#### Hello World

```scala
package cn.edw.scala.basic

object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello World!")
    System.out.println("Hello World!")
  }
}
```

参数声明：类似hive/mysql等，参数名：类型

public访问修饰符：scala中没有，不声明访问权限就是公共的

static：scala中没有静态语法，没有static

void：scala中没有，使用Unit类型替代

函数声明：方法名(参数列表)：返回值类型

def : 声明方法必须使用功能def关键字

方法实现需要赋值给方法声明，所以使用 = 



Scala完全面向对象，故Scala去掉了Java中非面向对象的元素，如static关键字，void类型

为了模仿静态语法，采用伴生对象单例 的方式调用



class关键字和Java中的class关键字作用相同，用来定义一个类

#### 变量和常量

变量声明时，必须要有初始值

类型确定后，就不能修改，说明 Scala 是强数据类型语言。

声明变量时，类型可以省略，编译器自动推导，即类型推导

在声明/定义一个变量时，可以使用 var 或者 val 来修饰，var 修饰的变量可改变， val 修饰的变量不可改

```scala
object Variable {
  def main(args: Array[String]): Unit = {
    // var changeable
    var a = 10
    // declare type
    var b: Int = 20
    //val: unchangeable
    val c: Int = 30
    // c = 40  // ERR
    val d = a + b + c
  }
}
```

#### 关键字

```text
• package, import, class, object, trait, extends, with, type, for
• private, protected, abstract, sealed, final, implicit, lazy, override
• try, catch, finally, throw
• if, else, match, case, do, while, for, return, yield
• def, val, var
• this, super
• new
• true, false, null
```

#### 标识符命名规则

Scala 中的标识符声明，基本和 Java 是一致的，但是细节上会有所变化：

- 以字母或者下划线开头，后接字母、数字、下划线
- 以操作符开头，且只包含操作符（+ - * / # !等）
- 用反引号`....`包括的任意字符串，即使是 Scala 关键字（39 个）也可以

#### 字符串输出

（1）字符串，通过+号连接 

（2）printf 用法：字符串，通过%传值。 

（3）字符串模板（插值字符串）：通过$获取变量值

多行字符串，在 Scala中，利用三个双引号包围多行字符串就可以实现

输入的内容，带有空格、\t 之类，导致每一行的开始位置不能整洁对齐。 //应用 scala 的 stripMargin 方法，在 scala 中 stripMargin 默认 是“|”作为连接符，//在多行换行的行头前面加一个“|”符号即可。

```scala
object S003_StringPrint {
  def main(args: Array[String]): Unit = {
    val name: String = "Edwin Xu"
    var age: Int = 24

    println(name + " - " + age)
    printf("I'm %s, and I am %d years old.", name, age)

    // 如果使用字符串模板， 前面加 s 
    val hello =
      s"""
        |I'm $name, and I am ${age+2} years old.
        |""".stripMargin
    println(hello)
  }
}
```

#### input

StdIn.readLine()、StdIn.readShort()、StdIn.readDouble()

```scala
object S004_Input {
  def main(args: Array[String]): Unit = {
    val name: String = StdIn.readLine()
    val age: Int = StdIn.readInt()
    println(name + " - " + age)
  }
}
```

#### 数据类型

1）Scala中**一切数据都是对象，都是Any的子类**。 

2）Scala中数据类型分为两大类：**数值类型（AnyVal）、 引用类型（AnyRef**），**不管是值类型还是引用类型都是 对象**。 

3）Scala数据类型仍然遵守，低**精度的值类型向高精 度值类型，自动转换（隐式转换）** 

4）Scala中的**StringOps**是对Java中的String增强 

5）**Unit**：**对应Java中的void**，用于方法返回值的位置，表 示方法没有返回值。**Unit是 一个数据类型，只有一个对象 就是()。Void不是数据类型，只是一个关键字**

6）**Null**是一个类型，**只 有一个对 象就 是null**。**它是 所有引用类型（AnyRef）的子类。** 

7）**Nothing**，是所有数据类型的子类，主要用在一个函数没有明确返回值时使 用，因为这样我们可以把抛出的返回值，返回给任何的变量或者函数。

![image-20211209005631260](_images/ScalaNotes.assets/image-20211209005631260.png)

##### 整数类型

Byte、Short、Int、Long

- Byte [1] 8 位有符号补码整数。数值区间为 -128 到 127 
- Short [2] 16 位有符号补码整数。数值区间为 -32768 到 32767 
- Int [4] 32 位有符号补码整数。数值区间为 -2147483648 到 2147483647 
- Long [8] 64 位有符号补码整数。数值区间为 -9223372036854775808 到 9223372036854775807 = 2 的(64-1)次方-1

Scala 各整数类型有固定的表示范围和字段长度，不受具体操作的影响，以保证 Scala 程序的可移植性。

Scala 的整型，默认为 Int 型，声明 Long 型，须后加‘l’或‘L’

##### 浮点类型

- Float [4] 32 位, IEEE 754 标准的单精度浮点数 

- Double [8] 64 位 IEEE 754 标准的双精度浮点数

Scala 的浮点型常量默认为 Double 型，声明 Float 型常量，须后加‘f’或‘F’。

##### 字符 Boolean

转义：

\\ ：表示\

\\" ：表示"

boolean 类型占 1 个字节

Booolean 类型数据只允许取值 true 和 false

##### Unit、Null、Nothing



24













