# Spring 

## 课程笔记

xml:

- 配置繁琐
- 代码逻辑割裂



循环依赖： 三级缓存



先官方文档，在源码，Spring的源码结构比较复杂。



factoryBean  &获取



Spring的扩展点：

- BeanFactoryPostProcessor
- BeanPostProcessor: DI是通过它实现的
- initMethod , destoryMethod
- aware
- 

有接口，可以使用JDK代理，但是没有接口只能使用CGLIB。

那些场景下代理不能生成？final，。。。

目前两种代理方式的性能相差不大



织入的几种方式：

- 运行期
- 编译器
- 。。。



切点表达式有那些：

- 注解？
- exec 表达式
- 



@Aspect是  Aspect的，不是Spring的，所以如果要引入到Spring容器中还需要Component





Spring JDBC

JDBC本质是一种协议、规约



Spring事务：在数据库事务上进一步封装，并且引入了新的东西



模板方法 复习下



transManager事务管理器，看源码

事务的传播级别，传播机制

Spring如何维护事务状态，如何维护连接的？？？

> **事务的最大作用范围是连接，其中利用到了ThreadLocal**

private方法事务有效吗

嵌套事务如何实现的

spring事务支持跨线程吗

方法的调用，x call y, 事务有效吗



starter的原理

## AOP

### 代理

静态代理：

- 容易编码实现
- 容易理解
- 实现代码量大，不可重用

Java动态代理：

- 基于InvocationHandlerProxy实现
- 可重用
- **只能基于接口实现**
- SpringAPO的优先选择

cglib代理

	- **不能代理final类和私有方法**
	- **能够对接口和类进行代理**
	- **通过生成子类的方式创建代理**

### AOP概念

- 连接点： jointpoint, 需要在程序中插入横切关注点的扩展点，spring只支持方法执行连接点。其他还有类初始化、方法执行、字段调用等
- 切入点：pointcut，连接点的集合
- 通知：advice，在连接点上执行的增强行为
- 切面：aspect，横切关注点的模块化
- 目标对象
- APO代理：代理模式创建对象，从而实现在连接点插入通知
- 织入：**weaving，织入是一个过程，是将切面应用到目标对象从而创建出AOP代理对象的过程，**织入可以发生在**编译期、类装载期、运行期**。
- 前置通知
- 后置通知：
  - 返回通知
  - 异常通知
  - 后置通知
- 环绕通知



## MVC

架构：

![image-20210729184441376](SpringNotes.assets/image-20210729184441376.png)

![image-20210729184528280](SpringNotes.assets/image-20210729184528280.png)

![image-20210729184941525](SpringNotes.assets/image-20210729184941525.png)

MVC测试

![image-20210729193108318](SpringNotes.assets/image-20210729193108318.png)

![image-20210729195116046](SpringNotes.assets/image-20210729195116046.png)



## SpringBoot

### 特点

- 丰富的starter简化pom配置
- 智能装配autoconfigure
- 可视化运行信息
- 不要求xml配置
- 约定大于配置



springboot插件

spring-boot-maven-plugin



> <scope>provided</scope>



#### AutoConfiguration

![image-20210729200730887](SpringNotes.assets/image-20210729200730887.png)

@Import

![image-20210729200916513](SpringNotes.assets/image-20210729200916513.png)

![image-20210729200931597](SpringNotes.assets/image-20210729200931597.png)

### 监控

运维监控 Starter Actuator

```
http://ip:port/manage
```











## 其他



公司推荐使用logback

异常栈必须放到最后

必须使用占位符



ELK方案



日志汇总：

- Kibana: 
- 容器化的环境： 

QUNAR目前都是拥抱云原生，使用Docker部署







一开始，不要设立天花板，能学多深就学多深







baeldung.com/learn-spring-course





```
- simpledateformat 多线程问题
- bigdecimal dubbo丢失精度问题
  
```







Spring SPI

- mvc： SSH、SpringMVC、SpringBoot
- MVP：model、view、presenter，代表Android
- MVVM：model view view-model， 代表avalon，vue



Servlet：

= service + applet，表示小服务程序java.servlet.Servlet

Struts: 从直接操纵Servlet到应用框架

Struts2: 更加友好的应用框架





不推荐fastjson， 使用jackson



@ExceptionHandler





java -jar 是怎么发现jar的main入口的?

SpringBootApplication.class



如何写starter???  SpringSPI??



SpringWebFlux

reactive Streams







dubbo 异步，provider consumer，2X2，四种情况？？？



dubbo异步，最新版本





mybatis-plus









### 冯子恺 日报回复

1.首先理解缓存的使用场景，什么场景下适用于缓存

2.理解缓存的选择，必须采用分布式缓存吗？本地缓存可以吗，比如guava的loading cache？

3.理解分布式，分布式锁的概念

4.分布式锁的使用场景，必须使用分布式锁吗？如果不使用会有其他方案满足业务需要吗？

5.技术只是银弹，合适的场景最简单的方案就是最好的









