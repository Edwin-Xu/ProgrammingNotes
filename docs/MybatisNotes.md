# Mybatis Notes

## Site

https://mybatis.org/mybatis-3/zh/index.html

## Basic

- mybatis-config.xml
- 定义mapper
- 通过config得到SQLSessionFactory
- 得到sqlSession, 和数据库交互

### SqlSession SqlSessionFactory

通过SqlSessionFactory获取SqlSession，

![image-20210804201103147](_images/MybatisNotes.assets/image-20210804201103147.png)



### \<sql>

用于将SQL的公共部分提取出来，便于其他SQL使用



### 传参

![image-20210804203319479](_images/MybatisNotes.assets/image-20210804203319479.png)

![image-20210804203408606](_images/MybatisNotes.assets/image-20210804203408606.png)

![image-20210804203442101](_images/MybatisNotes.assets/image-20210804203442101.png)

![image-20210804203523828](_images/MybatisNotes.assets/image-20210804203523828.png)





### 注解

![image-20210804201653326](_images/MybatisNotes.assets/image-20210804201653326.png)



#### @MapKey

有时我们的一条查询语句返回了多个实体对象或Map集合

比如这样：

```
List<User> users = abcDao.getNamesByIds(idList);
```

但我们在sql中这样让它返回

```
Map<id, User> m = abcDao.getNamesByIds(idList);
```

那`ResultType`属性可以指定为`User`

并且在方法上加上注解

```
@MapKey("id")
Map<id, User> m = abcDao.getNamesByIds(idList);
```

| 注解      | 使用对象 | 描述                                                         |
| :-------- | :------- | :----------------------------------------------------------- |
| `@MapKey` | 方法     | 这是一个用在返回值为 Map 的方法上的注解。它能够将存放对象的 List 转化为 key 值为对象的某一属性的 Map。属性有： `value`，填入的是对象的属性名，作为 Map 的 key 值 |









### 动态SQL 

if  

choose

where

set

trim: prefix, prefixOverrides(删除前缀，suffix)





### type

#### typeHandler

自定义两种方式：

- 实现TypeHandler接口
- 继承BaseTypeHandler

比如对象和Json字符串

#### 什么时候应该使用jdbcType

Mybatis中什么时候应该声明jdbcType？

当Mybatis不能自动识别你传入对象的类型时

you need to specify the `jdbcType` when passing null values for parameters.

Some databases need to know the value's type even if the value itself is NULL. 

The JDBC type is only required for nullable columns upon insert, update or delete. This is a JDBC requirement, not a MyBatis one. So even if you were coding JDBC directly, you'd need to specify this type – but only for nullable values.

Most of the times you don't need to specify the `jdbcType` as MyBatis is smart enough to figure out the type from the objects you are working with. But if you send your parameters to the MyBatis statement inside a `HashMap`, for example, and one of the parameters is null, MyBatis won't be able to determine the type of the parameter by looking at the `HashMap` because the `HashMap` is just a generic container and `null` itself carries no type information. At that point it would be o good idea to provide the `jdbcType` so that switching the database implementation later on does not cause any issues with null values.



### plugins

拦截器



可以拦截： 参数、结果集、批处理

- 



如何实现？

- 实现interceptor接口，指定拦截的方法签名
- 注册到配置文件

TODO 自己实现一下，类型处理器也是

### 表关联

association

collection



### \$ \# #

\$直接替换​

#防止SQL注入 

表明列明使用\$



**对于形如#{variable} 的变量，Mybatis会将其视为字符串值，在变量替换成功后，缺省地给变量值加上引号**。例如：

order by #{variable1}

假设variable1传入值为“name”，则最终[SQL语句](https://so.csdn.net/so/search?q=SQL语句&spm=1001.2101.3001.7020)等同为：

order by "name"

而**这个结果在日志里是发现不了的**，该句子语法检查亦能通过，可以执行。

**对于形如${variable}的变量，Mybatis会将其视作直接变量，即在变量替换成功后，不会再给其加上引号**。例如：

order by ${variable1}

假设variable1传入值为“name”，则最终SQL语句等同为：

order by name





### 全局配置文件

如果不使用SpringBoot集成，需要使用mybatis-config.xml配置

需要配置那些东西



1. type-aliases-package: 指定entity包的路径，在mapper中就不用使用全路径，直接使用类名即可。
2. 



```yml
mybatis:
  type-aliases-package: cn.edw.ems.entity
  # 定义mapper的路径
  mapper-locations: classpath:mapper/*.xml
  configuration:
  	# underscore：下划线，下划线映射到驼峰
    map-underscore-to-camel-case: true
```



### 分页

逻辑分页 Vs. 物理分页

**物理分页（后端分页）：**每次只从[数据库](_images/https://cloud.tencent.com/solution/database?from=10680)查出当前页的数据，并查出总条数，前端显示页码和数据

**逻辑分页（前端分页）：**数据一次性查询到前端，由前端根据总数据，来设置分页页码和当前页数据



- 物理分页适用于数据量大、更新频繁的场景
- 逻辑分页适用于数据量少、更新不频繁的场景



Mybatis实现分页的方法

- 使用RowBounds对象进行逻辑（逻辑内存中）分页，它是针对ResultSet结果集执行的内存分页。
- 使用pageHelper插件进行物理分页（其实是依赖物理数据库实体）



mybatis-plus是物理分页？



### 缓存

一级缓存：默认打开

二级缓存：默认关闭



### 转义

> \&lt; -- <
>
> \&gt; -- 
>
> 



### 和Spring的整合

#### @MapperScan

@Mapper注解：作用：在接口类上添加了@Mapper，在编译之后会生成相应的接口实现类

如果想要每个接口都要变成实现类，那么需要在每个接口类上加上@Mapper注解，比较麻烦，解决这个问题用@MapperScan。指定要变成实现类的接口所在的包，然后包下面的所有接口在编译之后都会生成相应的实现类



## 原理

### 架构

![image-20210804204056087](_images/MybatisNotes.assets/image-20210804204056087.png)



### 执行

![image-20210804204219517](_images/MybatisNotes.assets/image-20210804204219517.png)



### 插件 拦截器

TODO mybatis-plus这个配置要好好理解一下

```java
package cn.edw.ems.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.autoconfigure.ConfigurationCustomizer;
import com.baomidou.mybatisplus.core.MybatisConfiguration;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

import javax.sql.DataSource;
import java.util.Properties;

/**
 * @author Edwin Xu
 * @date 3/7/2021 9:19 PM.
 *
 * MyBatis-Plus 配置
 */
@Configuration
public class MybatisPlusConfig {

    /**
     * 分页插件，其实就是添加一个拦截器
     * */
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return interceptor;
    }

    @Bean
    public ConfigurationCustomizer configurationCustomizer() {
        return new ConfigurationCustomizer() {
            @Override
            public void customize(MybatisConfiguration configuration) {
                configuration.setUseGeneratedKeys(true);
            }
        };
    }



    /**
     * SqlSessionFactory不要使用原生的，使用MybatisSqlSessionFactory。
     * https://mp.baomidou.com/guide/faq.html#%E5%87%BA%E7%8E%B0-invalid-bound-statement-not-found-%E5%BC%82%E5%B8%B8
     * https://www.cnblogs.com/zeyfra/p/ZeyFra-MyBatis-Plus-01.html
     * */
    @Bean("sqlSessionFactory")
    @Primary
    public SqlSessionFactory sqlSessionFactory(@Autowired @Qualifier("dataSource") DataSource dataSource) throws Exception {
        // MybatisPlus内部过滤器
        // 为自动分页插件设置DB类型
        MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
        PaginationInnerInterceptor paginationInnerInterceptor= new PaginationInnerInterceptor(DbType.MYSQL);
        paginationInnerInterceptor.setOptimizeJoin(true);
        mybatisPlusInterceptor.addInnerInterceptor(paginationInnerInterceptor);

        Properties properties = new Properties();
        properties.setProperty("reasonable", "true");
        mybatisPlusInterceptor.setProperties(properties);
        // MybatisConfiguration
        MybatisConfiguration mybatisConfiguration = new MybatisConfiguration();
        // 添加自定义拦截器
        mybatisConfiguration.addInterceptor(mybatisPlusInterceptor);

        // 这里被我删了，是什么拦截器？
        // mybatisConfiguration.addInterceptor(new UpdateInterceptor());

        // 使用MybatisSqlSessionFactoryBean
        MybatisSqlSessionFactoryBean sqlSessionFactoryBean = new MybatisSqlSessionFactoryBean();

        // 设置数据源
        sqlSessionFactoryBean.setDataSource(dataSource);

        // 添加设置
        sqlSessionFactoryBean.setConfiguration(mybatisConfiguration);

        // 设置xml路径
//        sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
//                .getResources("classpath:/mapper/*Mapper.xml"));



        //其他配置
//        Properties properties = new Properties();

        //设置方言：oracle,mysql,mariadb,sqlite,hsqldb,postgresql,db2,sqlserver,informix,h2,sqlserver2012,derby
        //properties.setProperty("helperDialect", "sqlserver");

        //默认值为false，当该参数设置为 true 时，会将 RowBounds 中的 offset 参数当成 pageNum 使用，可以用页码和页面大小两个参数进行分页。
        //properties.setProperty("offsetAsPageNum", "true");

        //默认值为false，该参数对使用 RowBounds 作为分页参数时有效。 当该参数设置为true时，使用 RowBounds 分页会进行 count 查询。
        //properties.setProperty("rowBoundsWithCount", "true");

        //分页合理化参数，默认值为false。当该参数设置为 true 时，pageNum<=0 时会查询第一页， pageNum>pages（超过总数时），会查询最后一页。默认false 时，直接根据参数进行查询。
//        properties.setProperty("reasonable", "true");

        //添加设置
//        interceptor.setProperties(properties);

        //也可直接通过以下方式直接添加拦截器或Interceptor数组
//        sqlSessionFactoryBean.setPlugins(new Interceptor[] {interceptor});

        return sqlSessionFactoryBean.getObject();
    }


```



## 常见问题

### 插入后返回自增ID

- 方式一: @Options分别设置参数useGeneratedKeys，keyProperty，keyColumn值

  ```java
  // 返回主键字段id值
  @Options(useGeneratedKeys = true, keyProperty = "id", keyColumn = "id")
  @Insert("insert into t_person(name,sex,age,create_time,update_time) values(#{name},#{sex},#{age},now(),now())")
  Integer insertPerson(Person person);
  ```

- 方式二：添加单一记录时返回主键ID

  ```xml
  # keyProperty：表示将返回的值设置到某一列，此处为id；
  <insert id="insertPerson" parameterType="cn.mybatis.mydemo.domain.Person">
      <selectKey resultType="INTEGER" order="AFTER" keyProperty="id">
        SELECT LAST_INSERT_ID()
      </selectKey>
      insert into t_person(name,sex,age,create_time,update_time) 
      values(#{name},#{sex},#{age},now(),now())
    </insert>
  ```

-  批量增加记录时返回主键ID

  ```xml
  <mapper namespace="cn.mybatis.mydemo.mapper">
      <!-- 插入数据：返回记录主键id值 -->
      <insert id="insertPerson" parameterType="java.util.List" useGeneratedKeys="true" keyProperty="id" keyColumn="id" >
          insert into t_person(name,sex,age,create_time,update_time) 
          values
          <foreach collection="list" item="item" index="index" separator="," >
              (
              #{item.name},
              #{item.sex},
              #{item.age},
              now(),
              now()    
              )
          </foreach>
      </insert>
  </mapper>
  ```



### test 判断0无效

判断是否为空一般为：

```xml
<if test="state!=null and state!=''">state = #{state},</if>
```

但是如果传入的值为0，就不运行该条，因为mybatis默认0和""相等，要解决这个问题，可以把代码改为：

```xml
<if test="state!=null and state!='' or state==0">state = #{state},</if>
//或者把判断是否为空字符串去掉，变为：
<if test="state!=null">state = #{state},</if>
```

或者将0转化为String类型，也可以解决该问题



Any object can be used where a boolean is required. OGNL interprets objects as booleans like this:
任何对象都可以使用布尔值。
• If the object is a Boolean, its value is extracted and returned;
如果对象是布尔布尔值，则提取并返回其值
• If the object is a Number, its double-precision floating-point value is compared with zero; non-zero is treated as true, zero as false;
如果对象是一个数，它的双精度浮点值与零；零视为真实的，零是错误的；
• If the object is a Character, its boolean value is true if and only if its char value is non-zero;
如果对象是一个字符，则其布尔值为真，当且仅当其char值为非零时
• Otherwise, its boolean value is true if and only if it is non-null.
否则，它只is true if布尔值，如果它是非空的。

原因： 0和“”都会被转成double进行比较，都会变成0.0，这就是mybati中 0 判定为false的原因

这里有必要再提一个“坑”，如果你有类似于String str =“A”; 这样的写法时，你要小心了。因为单引号内如果为单个字符时，OGNL将会识别为Java 中的 char类型，显然String 类型与char类型做==运算会返回false，从而导致表达式不成立。解决方法很简单，修改为< if test = ’ str != null and str == “A” '>即可




## 注意事项

### 返回list

在没有指定limit 1的情况下，默认就是返回list，所以不要指定

```sql
resultType="java.util.List"
```

而是要指定list中的类型



### ''

把<if test="takeWay == '1' and workday != null ">

改为<if test='takeWay == "1" and workday != null '>

或改为<if test="takeWay == '1'.toString() and workday != null ">即可。

原因是：mybatis是用OGNL表达式来解析的，在OGNL的表达式中，’1’会被解析成字符，java是强类型的，char 和 一个string 会导致不等，所以if标签中的sql不会被解析。

总结下使用方法：单个的字符要写到双引号里面或者使用.toString()才行！



## MybatisPlus

https://wiki.corp.qunar.com/confluence/pages/viewpage.action?pageId=370275901





### 配置





```
<!-- 5、mybatisplus的全局策略配置 -->
<bean id="globalConfiguration" class="com.baomidou.mybatisplus.core.config.GlobalConfig">
    <property name="dbConfig" ref="dbConfig"/>
</bean>

<bean id="dbConfig" class="com.baomidou.mybatisplus.core.config.GlobalConfig.DbConfig">
    <!-- 全局主键自增策略，0表示auto -->
    <property name="idType" value="AUTO"/>
    <!--Select策略：当不为空时才作为where条件-->
    <property name="selectStrategy" value="NOT_EMPTY"/>
</bean>

<!-- mybatis整合spring的配置 -->
<bean id="sqlSessionFactory" class="com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean">
    <!-- dataSource用于指定mybatis的数据源 -->
    <property name="dataSource" ref="dynamicDataSource"/>
    <!-- mapperLocations用于指定mybatis中mapper文件所在的位置 -->
    <property name="mapperLocations" value="classpath*:mappers/**/*.xml"/>
    <!--Mybatis Plus全局配置-->
    <property name="globalConfig" ref="globalConfiguration"/>
    <property name="configuration">
        <bean class="com.baomidou.mybatisplus.core.MybatisConfiguration">
            <property name="logImpl" value="org.apache.ibatis.logging.stdout.StdOutImpl"></property>
        </bean>
    </property>
    <property name="plugins">
        <array>
            <bean class="com.github.pagehelper.PageInterceptor">
                <property name="properties">
                    <value>
                        helperDialect=mysql
                        reasonable=false
                        supportMethodsArguments=true
                        params=count=countSql
                        autoRuntimeDialect=true
                    </value>
                </property>
            </bean>
            <bean class="com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor">
                <property name="interceptors">
                    <list>
                        <bean id="innerInterceptor" class="com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor">
                            <property name="dbType" value="MYSQL"/>
                        </bean>
                    </list>
                </property>
            </bean>
            <bean class="com.qunar.fintech.datacommon.interceptors.DynamicDataSourceInterceptor">
            </bean>
        </array>
    </property>
</bean>

    <!--批量注册mybatis中的dao。 使用这种方式，Dao的实现就不会被调用 -->
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
        <property name="basePackage" value="com.qunar.fintech.dm.dao.mapper,com.qunar.fintech.bi.dao.mapper,com.qunar.fintech.ai.dao.mapper"/>
        <property name="sqlSessionFactoryBeanName" value="sqlSessionFactory"/>
    </bean>
```



QueryWapper的lambda中，如果字段为NULL，默认仍然会参与where条件，如果需要过滤，则需要配置：

mybatis-plus: global-config: db-config: select-strategy: not_empty
