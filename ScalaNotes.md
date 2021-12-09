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

Unit：表示无值，和其他语言中 void 等同。用作不返回任何结果的方法的结果 类型。Unit 只有一个实例值，写成()

Null：null

Nothing: Nothing 类型在 Scala 的类层级最低端；它是任何其他类型的子类型。 当一个函数，我们确定没有正常的返回值，可以用 Nothing 来指定返回类 型，这样有一个好处，就是我们可以把返回的值（异常）赋给其它的函数 或者变量（兼容性）

**Null 可以赋值给任 意引用类型（AnyRef），但是不能赋值给值类型（AnyVal）**

Nothing，可以作为没有正常返回值的方法的返回类型，**非常直观的告诉你这个方 法不会正常返回**，而且由于 Nothing 是其他任意类型的子类，他还能跟要求返回值的方法兼 容。

```scala
object S005_Type {
  def main(args: Array[String]): Unit = {
    val a: Byte = 1
    val b: Short = 2
    val c: Int = 3
    val d: Long = 4

    val e: Char = 'a'

    val f: Boolean = false

    val g: Float = 3.0f
    val h: Double = 4.0

    val i: Null = null
    // val i:Int = null  ERR: null不能赋值给AnyVal
    val j: Unit = Unit
    val k: Unit = ()

    def f1(): Unit = {

    }

    def f2(): Nothing = {
      // no return
      throw new Exception()
    }
  }
}
```

##### 类型隐式转换

当 Scala 程序在进行赋值或者运算时，精度小的类型自动转换为精度大的数值类型，这 个就是自动类型转换（隐式转换）。数据类型按精度（容量）大小排序为

![image-20211209234145705](_images/ScalaNotes.assets/image-20211209234145705.png)

（1）自动提升原则：有多种类型的数据混合运算时，系统首先自动将所有数据转换成 精度大的那种数据类型，然后再进行计算。 

（2）把精度大的数值类型赋值给精度小的数值类型时，就会报错

（3）（byte，short）和 char 之间不会相互自动转换。 

（4）byte，short，char 他们三者可以计算，在计算时首先转换为 int 类型

```scala
object S006_TypeCast {
  def main(args: Array[String]): Unit = {
    val a = 1 + 0.2 + 3.4f + 'c'
    println(a) // 103.60000009536743  !

    val b: Byte = 1
    val c: Char = 'a'
    val d: Short = 1
    val e = b + c - d
    println(e)
  }
}
```

scala 还提供隐式函数、隐式类等的转换



##### 类型强制转换

强制转换：**自动类型转换的逆过程**，将精度大的数值类型转换为精度小的数值类型。使用时要加上 强制转函数，但可能造成精度降低或溢出，格外要注意

强转符号只针对于最近的操作数有效，往往会使用小括号提升优先级

```scala
object S007_TypeForceCast {
  def main(args: Array[String]): Unit = {
    val a: Double = 1.2
    val b: Int = a.toInt
    val c = 2.2f.toByte
    println(b, c)
  }
}
```

##### 数值类型和String转换

（1）基本类型转 String 类型（语法：将基本类型的值+"" 即可） 

（2）String 类型转基本数值类型（语法：s1.toInt、s1.toFloat、s1.toDouble、s1.toByte、s1.toLong、s1.toShort）

在将 String 类型转成基本数值类型时，要确保 String 类型能够转成有效的数据，比如我 们可以把"123"，转成一个整数，但是不能把"hello"转成一个整数。

```scala
object S008_NumStrCast {
  def main(args: Array[String]): Unit = {
    // num to str
    val a: String = 1.toString
    val b: String = 2 + ""
    // str to num
    val c: Int = "234".toInt
    val d: Double = "1.2".toDouble
    println(a, b, c, d)
  }
}
```

#### 运算法

- +
- -
- *
- *
- %
- /:整数除和小数除是有区别的：整数之间做除法时，只保留整 数部分而舍弃小数部分。
- //: rand
- ==: ==更加类似于 Java 中的 equals
- << >> >>>

注意：Scala 中没有++、--操作符，可以通过+=、-=来实现同样的效果



Scala运算符本质：

**在 Scala 中其实是没有运算符的，所有运算符都是方法**。

1）当调用对象的方法时，点.可以省略 

2）如果函数参数只有一个，或者没有参数，()可以省略

```scala
object S009_Operator {
  def main(args: Array[String]): Unit = {
    val a = 1 >> 10 / 3 // 4

    val c = a.equals(1)

    // 标准的加法运算
    val d: Int = 1.+(2)

    // 当调用对象的方法时， .可以省略
    // 如果函数的参数个数 <=1，()可以省略
    println(1.toString())
    println(1.toString)
    println(1 toString)
    println(1    toString)
  }
}
```

#### 流程控制

Scala 中 if else 表达式其实是有返回值的，具体返回值取决于满足条件的 代码体的最后一行内容。

**在 Scala 中没有 Switch，而是使用模式匹配来处理**



For 循环控制 Scala 也为 for 循环这一常见的控制结构提供了非常多的特性，这些 for 循环的特性被称 为 **for 推导式或 for 表达式**

41























