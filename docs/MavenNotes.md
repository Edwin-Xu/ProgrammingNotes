# Maven Notes

## Maven Basic

### 功能与特性

- **项目构建**
- **依赖管理**
- 测试驱动开发TDD
- 项目模块化管理
- 项目骨架创建
- 约定由于配置

### 基本架构设计

maven对构建(build)的过程进行了抽象和定义，这个过程被称为构建的生命周期(lifecycle)。生命周期(lifecycle)由多个阶段(phase)组成,每个阶段(phase)会挂接一到多个goal。goal是maven里定义任务的最小单元，goal分为两类，一类是绑定phase的，就是执行到某个phase，那么这个goal就会触发，另外一类不绑定，就是单独任务

Maven预设了三个Lifecycle ，各包含了下列Phases.

1. 1. Clean Lifecycle
      - pre-clean
      - clean
      - post-clean
   2. Default Lifecycle
      - validate
      - initialize
      - generate-sources
      - process-sources
      - generate-resources
      - process-resources
      - compile
      - process-classes
      - generate-test-sources
      - process-test-sources
      - process-test-resources
      - test-compile
      - process-test-classes
      - test
      - prepare-package
      - package
      - pre-integration-test
      - integration-test
      - post-integration-test
      - verify
      - install
      - deploy
   3. Site Lifecycle
      - pre-site
      - site
      - post-site
      - site-deploy



### maven仓库

- 本地仓库
- 远程仓库
  - 私服，自建Nexus：http://nexus.corp.qunar.com/
  - 中央仓库
  - 中央仓库镜像

### 定位

- groupid: 公司组织域名倒序 + 项目名
- artifact: 模块名

### POM

project of maven

- properties: 属性

- dependencyManagement：依赖管理，主要是版本管理，只是定义，不会有实际的引入。被动依赖上，约束被动依赖的属性，比如 A包隐式依赖B，我们只能引入A不能控制B，使用本标签可以管理被动依赖的属性。

- profile：针对不同的环境提供不同的配置文件，比如有环境local、dev、beta、prod

  ```xml
  <profiles>
      <profile>
          <id>dev_evn</id>
          <properties>
              <db.driver>com.mysql.jdbc.Driver</db.driver>
              <db.url>jdbc:mysql://localhost:3306/test</db.url>
              <db.username>root</db.username>
              <db.password>root</db.password>
          </properties>
      </profile>
      <profile>
          <id>test_evn</id>
          <properties>
              <db.driver>com.mysql.jdbc.Driver</db.driver>
              <db.url>jdbc:mysql://localhost:3306/test_db</db.url>
              <db.username>root</db.username>
              <db.password>root</db.password>
          </properties>
      </profile>
  </profiles>
  ```

  开发时可以用 mvn 命令后面添加“-P dev_evn”激活“dev_evn profile”

  用户可以在 mvn 命令行中添加参数“-P”，指定要激活的 profile 的 id。如果一次要激活多个 profile，可以用逗号分开一起激活。例如：

  > mvn clean install -Pdev_env,test_evn

### BOM

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Greenwich.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

BOM（Bill of Materials）定义一整套相互兼容的jar包版本集合，使用时只需要依赖该BOM文件，即可放心的使用需要的依赖jar包，且无需再指定版本号。BOM的维护方负责版本升级，并保证BOM中定义的jar包版本之间的兼容性。

为什么需要BOM？
使用BOM除了可以方便使用者在声明依赖的客户端时不需要指定版本号外，最主要的原因是可以解决依赖冲突。
考虑以下的依赖场景：
Project A依赖B 2.1.3和C 1.2.0版本；
B 2.1.3依赖D 1.1.6版本；
C 1.2.0依赖D 1.3.0版本。
则 Project A对于D的依赖就出现冲突，按照maven dependency mediation的规则，最后生效的是1.1.6版本（就近原则）。
在这种情况下，由于C依赖1.3.0版本的D，但是在运行时生效的确是1.1.6版本，所以在运行时很容易产生问题，如 NoSuchMethodError, ClassNotFoundException等。

如何定义BOM？
BOM本质上是一个普通的POM文件，区别是对于使用方而言，生效的只有<dependencyManagement>这一个部分。只需要在<dependencyManagement>定义对外发布的客户端版本即可。

dependency management takes precedence over dependency mediation for transitive dependencies.

如何使用BOM？
首先需要在pom.xml文件的<dependencyManagement>中，声明对BOM的依赖，然后在实际使用依赖的地方把版本去掉即可。


### **scope**

约定优于配置：Convention Over Configuration

scope指定了依赖的作用范围

- 作用范围包括，所在项目的**测试、编译、运行、打包等**生命周期
- 其中，编译和运行还分为
  - **测试代码**的编译和运行
  - **非测试代码**的编译和运行



- compile
  默认的scope，表示 dependency 参与当前项目的**编译、测试、运行、打包**。而且，这些dependencies 会传递到依赖的项目中。适用于所有阶段，会随着项目一起发布
  
- provided
  provided 表明该**依赖已经提供，故只在未提供时才被使用这个scope** ，只能作用在编译和测试时，运行的时候使用已经提供的依赖而不使用导入的依赖，同时没有传递性。
  
- test

  **针对测试相关代码的编译和运行**，在**通常代码**的编译和运行时都不需要，只有在**有关测试的代码编译和运行测试代码阶段**可用

- runtime 

  依赖**无需参与当前项目的编译**，但是后期的**运行和测试**需要参与。 如MySQL驱动

- system

  被依赖项**不会从maven仓库下载**，而是**从本地系统指定路径下寻找**，需要 systemPath 属性
  
- import
  
  我们知道Maven的继承和Java的继承一样，是无法实现多继承的，这个父模块的dependencyManagement可能会包含大量的依赖。如果你想把这些依赖分类以更清晰的管理，那就不可能了，import scope依赖能解决这个问题。你可以把dependencyManagement放到单独的专门用来管理依赖的pom中，然后在需要使用依赖的模块中通过import scope依赖，就可以引入dependencyManagement。
  
  例如，在Spring boot 项目的POM文件中，我们可以通过在POM文件中继承 Spring-boot-starter-parent来引用Srping boot默认依赖的jar包
  
  但是，**通过上面的parent继承的方法，只能继承一个 spring-boot-start-parent。实际开发中，用户很可能需要继承多个parent配置，这个时候可以使用 scope=import 来实现多继承**。
  
  ![image-20210804161408713](_images/MavenNotes.assets/image-20210804161408713.png)
  
  注意：**import scope只能用在dependencyManagement里面**，且仅用于type=pom的dependency
  
  这样就可以导入spring-boot-dependencies-Hoxton.RELEASE.pom文件中dependencyManagement配置的jar包依赖。



Scope的依赖传递：

A–>B–>C。当前项目为A，A依赖于B，B依赖于C。知道B在A项目中的scope，那么怎么知道C在A中的scope呢？

  答案是：

  **当C是test或者provided时，C直接被丢弃**，A不依赖C； 否则A依赖C，C的scope继承于B的scope。

### optional

Maven 中的依赖是有传递（Transitive）性的，默认会包含传递的依赖，这样就不用手动引用每一个依赖了。比如下面这个依赖关系中，A 依赖 B，B 依赖了 C……，如果你依赖 A 的话，就会自动包含 A/B/C/D/E

解决这个依赖传递导致的冲突问题，有两种方案：

**「1」** 在使用者，也就是发起依赖方进行排除

**「2」** 在提供方，将依赖的范围定义为**不传递**，这样在构建时就不会包含这些**不传递**的依赖包了，不传递的配置有两种方式：

- 定义 dependency scope 为 provided
- 定义 <optional>true</optional>

在这两种**不传递**配置下，依赖关系都将在声明它们的模块的 classpath 中，但是使用将它们定义为依赖关系的模块不会在其他项目中传递它们，即不会形成依赖传递

**optional：可选的，可以理解为此功能/此依赖可选，如果不需要某项功能，可以不引用这个包。**

**scope provided：提供的，可以理解为此包不由我直接提供，需要调用者/容器提供。**





### packaging

打包方式：war, jar

还有一种：pom， 表示父子工程，父模块必须使用pom类型

**<packaging>pom</packaging>**



### 版本号

> 主版本.次版本.增量版本-里程碑版本
>
> 主版本表示一个大的更新，次版本是一个小一点的更新，比如一个feature，增量版本是一个小版本。

- PRE：灰度版本(Qunar规范)
- SNAPSHOT：不确定版本，用于开发调试，底层通过时间戳确定版本，引入时选择最新的时间戳
- RELEASE或者不带后缀：正式版本，发布版本



### 生命周期

- clean：preclean--clean-- post-clean
- default: ...--compile--test-package-install--package
- site

### Maven插件

如maven-dependency-plugin

使用 ```mvn dependency:tree/list/analyze```是插件执行的，而不是maven本身

### 依赖冲突

> A - B - C1.0
>
> D - C2.0

怎么仲裁？

- dependencyManagement如果声明了，选择指定版本即可
- 短路径有限：选短的
- 先声明者优先

不推荐使用exclusion排除，因为很可能导致错误



引入多个不同版本的统一依赖，不会报错，遇到谁就是谁，双亲委派模型

### 父子工程

父子各模块版本必须一直



### 如何写好pom

- 父pom只做版本管理
- 子pom不管理依赖版本
- 父pom统一指定版本
- 字模块相互依赖，使用\${project.version}$​​
- 使用properties统一管理、定义
- 直接依赖的包要显式引入，不要间接引入
- 避免使用exclusion，使用dependencyManagement
- 

### Wrapper

要使用maven那就必要要安装maven,如果有些用户不想安装maven怎么办？或者说用户不想全局安装maven,那么可以使用**项目级别的Maven Wrapper**来实现这个功能。

如果大家使用IntelliJ IDEA来开发Spring boot项目, 如果选择从Spring Initializr来创建项目，则会在项目中自动应用Maven Wrapper。简单点说就是在项目目录下面会多出两个文件： **mvnw 和 mvnw.cmd**。



#### Maven Wrapper的结构

mvnw是Linux系统的启动文件。

mvnw.cmd是windows系统的启动文件。

本文不会详细讲解启动文件的内部信息，有兴趣的小伙伴可以自行去研究。除了这两个启动文件，在项目中还会生成一个.mvn的隐藏文件夹



如果不是使用IntelliJ IDEA，我们该怎么样下载Maven Wrapper呢？

在程序的主目录下面：

```shell
mvn -N io.takari:maven:wrapper
```

如果要指定maven版本：

```shell
mvn -N io.takari:maven:wrapper -Dmaven=3.5.2
```

-N 意思是 –non-recursive，只会在主目录下载一次。



Maven Wrapper的使用和maven命令是一样的，比如：

```shell
./mvnw clean install
./mvnw spring-boot:run
```

### profile

profile定义的地方不同，它的作用范围也不同。

- 针对于特定项目的profile配置我们可以定义在该项目的pom.xml中。
- 针对于特定用户的profile配置，我们可以在用户的settings.xml文件中定义profile。该文件在用户家目录下的“.m2”目录下。
- 全局的profile配置。全局的profile是定义在Maven安装目录下的“conf/settings.xml”文件中的。

当profile定义在settings.xml中时意味着该profile是全局的，它会对所有项目或者某一用户的所有项目都产生作用。因为它是全局的，所以在settings.xml中只能定义一些相对而言范围宽泛一点的配置信息，比如远程仓库等

定义在pom.xml中的profile可以定义更多的信息。主要有以下这些：

```text
l <repositories>
l <pluginRepositories>
l <dependencies>
l <plugins>
l <properties>
l <dependencyManagement>
l <distributionManagement>
l 还有build元素下面的子元素，主要包括：
<defaultGoal>
<resources>
<testResources>
<finalName>
```

Maven给我们提供了多种不同的profile激活方式。比如我们可以使用-P参数显示的激活一个profile，也可以根据环境条件的设置让它自动激活等。



**使用activeByDefault设置激活**: <activeByDefault>true</activeByDefault> 

```text
<profiles> 
    <profile> 
        <id>profileTest1</id> 
        <properties> 
            <hello>world</hello> 
        </properties> 
        <activation> 
            <activeByDefault>true</activeByDefault> 
        </activation> 
    </profile> 

    <profile> 
        <id>profileTest2</id> 
        <properties> 
            <hello>andy</hello> 
        </properties> 
    </profile> 
</profiles>
```



如果写了多个激活，后面定义的会覆盖前面定义的。



**使用-P参数显示的激活一个profile**：

```text
mvn package –P profileTest1 
```

当我们使用activeByDefault或settings.xml中定义了处于激活的profile，但是当我们在进行某些操作的时候又不想它处于激活状态，这个时候我们可以这样做：

```bash
Mvn package –P !profileTest1 
```

profile一个非常重要的特性就是它可以根据不同的环境来激活，比如说根据操作系统的不同激活不同的profile，也可以根据jdk版本的不同激活不同的profile



**查看当前处于激活状态的profile**

　　我们可以同时定义多个profile，那么在建立项目的过程中，到底激活的是哪一个profile呢？Maven为我们提供了一个指令可以查看当前处于激活状态的profile都有哪些，这个指定就是**mvn help:active-profiles**。





### original

.jar.original 是普通jar包，不包含依赖
.jar 是可执行jar包，包含了pom中的所有依赖，可以直接用java -jar 命令执行
**如果是部署，就用.jar
如果是给别的项目用，就要给.jar.original这个包**







## plugin

### Maven Enforcer plugin

Enforcer可以在项目validate时，对项目环境进行检查。

Enforcer配置后默认会在validate后执行enforcer:enforce,然后对项目环境进行检查。拿上面对JDK的校验为例，我们在pom.xml中配置插件。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project>
...
    <build>
        <plugins>
            <plugin>
                <artifactId>maven-enforcer-plugin</artifactId>
                <version>1.4.1</version>
                <executions>
                    <execution>
                        <id>default-cli</id>
                        <goals>
                            <goal>enforce</goal>
                        </goals>
                        <phase>validate</phase>
                        <configuration>
                            <rules>
                                <requireJavaVersion>
                                    <message>
                                        <![CDATA[You are running an older version of Java. This application requires at least JDK ${java.version}.]]>
                                    </message>
                                    <version>[${java.version}.0,)</version>
                                </requireJavaVersion>
                            </rules>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    <properties>
        <java.version>1.8</java.version>
    </properties>
 
</project>
```





## Nexus

Nexus是Maven仓库管理器，如果你使用Maven。

你可以从[Maven中央仓库] (https://link.zhihu.com/?target=http%3A//repo1.maven.org/maven2/) 下载所需要的构件（artifact），但这通常不是一个好的做法，你应该在本地架设一个Maven仓库服务器，在代理远程仓库的同时维护本地仓库，以节省带宽和时间，Nexus就可以满足这样的需要。此外，他还提供了强大的仓库管理功能，构件搜索功能，它基于REST，友好的UI是一个extjs的REST客户端，它占用较少的内存，基于简单文件系统而非数据库。这些优点使其日趋成为最流行的Maven仓库管理器





## Tail



























