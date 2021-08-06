# Common Notes

## 序列化

序列化 (Serialization)是将对象的状态信息转换为可以存储或传输的形式的过程。在序列化期间，对象将其当前状态写入到临时或持久性存储区。以后，可以通过从存储区中读取或反序列化对象的状态，重新创建该对象。

- 二进制序列化保持类型保真度，这对于在应用程序的不同调用之间保留对象的状态很有用。例如，通过将对象序列化到剪贴板，可在不同的应用程序之间共享对象。您可以将对象序列化到流、磁盘、内存和网络等等。远程处理使用序列化“通过值”在计算机或应用程序域之间传递对象。

- XML 序列化仅序列化公共属性和字段，且不保持类型保真度。当您要提供或使用数据而不限制使用该数据的应用程序时，这一点是很有用的。由于 XML 是一个开放式标准，因此，对于通过 Web 共享数据而言，这是一个很好的选择。SOAP 同样是一个开放式标准，这使它也成为一个颇具吸引力的选择。

### 二进制序列化

![image-20210806165231754](CommonNotes.assets/image-20210806165231754.png)

#### JDK

- **无法跨语言**：致命伤害，对于跨进程的服务调用，通常都需要考虑到不同语言的相互调用时候的兼容性。jdk序列化操作时是使用了java语言内部的私有协议，在对其他语言进行反序列化的时候会有严重的阻碍。

- **序列化之后的码流过大**：序列化编码之后产生的字节数组过大，占用的存储内存空间也较高



#### Hessian

支持多种语言

码流也较小，处理数据的性能方面远超于java内置的jdk序列化方式

```java
    public static void main(String[] args) throws IOException {
        long begin = System.currentTimeMillis();
        for (int i = 0; i < 2000; i++) {
            Person person = new Person();
            person.setId(1);
            person.setUsername("idea");
            person.setTel("99562352");
            ByteArrayOutputStream os = new ByteArrayOutputStream();
            HessianOutput ho = new HessianOutput(os);
            ho.writeObject(person);
            byte[] userByte = os.toByteArray();
            ByteArrayInputStream is = new ByteArrayInputStream(userByte);
            //Hessian的反序列化读取对象
            HessianInput hi = new HessianInput(is);
            Person newPerson = (Person) hi.readObject();
        }
        long end = System.currentTimeMillis();
        System.out.println("耗时：" + (end - begin));
    }
```

#### Kryo

Kryo是一种非常成熟的序列化实现，已经在Twitter、Groupon、 Yahoo以及多个著名开源项目（如Hive、Storm）中广泛的使用，它的性能在各个方面都比hessian2要优秀些，因此dubbo后期也开始渐渐引入了使用Kryo进行序列化的方式。

```xml
<dependency>
    <groupId>com.esotericsoftware</groupId>
    <artifactId>kryo-shaded</artifactId>
    <version>3.0.3</version>
</dependency>
```

```java
    public static void main(String[] args) throws FileNotFoundException {
        Kryo kryo=new Kryo();
        Output output = new Output(new FileOutputStream("person.txt"));
        Person person=new Person();
        person.setId(1);
        person.setUsername("idea");
        kryo.writeObject(output, person);
        output.close();
        Input input = new Input(new FileInputStream("person.txt"));
        Person person1 = kryo.readObject(input, Person.class);
        input.close();
        System.out.println(person1.toString());
        assert "idea".equals(person1.getUsername());
    }
```

Kryo不支持没有无参构造函数的对象进行反序列化，因此如果某个对象希望使用Kryo来进行序列化操作的话，需要有相应的无参构造函数才可以。

Kryo不是线程安全

#### Xstream

在使用XStream进行序列化技术的实现过程中，类中的字符串组成了 XML 中的元素内容，而且该对象还不需要实现 Serializable 接口。XStream不关心被序列化/反序列化的类字段的可见性，该对象也不需要有getter/setter方法和默认的构造函数。

```xml
<dependency>
            <groupId>com.thoughtworks.xstream</groupId>
            <artifactId>xstream</artifactId>
            <version>1.4.9</version>
        </dependency>
```



#### Protobuf

google protobuf是一个灵活的、高效的用于序列化数据的协议。相比较XML和JSON格式，protobuf更小、更快、更便捷。google protobuf是跨语言的，并且自带了一个编译器(protoc)，只需要用它进行编译，可以编译成Java、python、C++、C#、Go等代码，然后就可以直接使用，不需要再写其他代码，自带有解析的代码。
protobuf相对于kryo来说具有更加高效的性能和灵活性，能够在实际使用中，当对象序列化之后新增了字段，在反序列化出来的时候依旧可以正常使用。



### XML/JSON序列化

#### Jackson

 Jackson可以轻松的将Java对象转换成json对象和xml文档，同样也可以将json、xml转换成Java对象。

基于事件驱动，与GSON相同，先创建一个对应于JSON数据的JavaBean类就可以通过简单的操作解析出所需JSON数据。但和Gson解析不同的是，GSON可按需解析，即创建的JavaBean类不一定完全涵盖所要解析的JSON数据，按需创建属性，但Jackson解析对应的JavaBean必须把Json数据里面的所有key都有所对应，即必须把JSON内的数据所有解析出来，无法按需解析。但Jackson的解析速度和效率都要比GSON高　　　

优势

1、解析效率最高 

2、在数据量大的情况优势尤为明显、占存少

缺点

必须完全解析文档，如果要按需解析的话可以拆分Json来读取，操作和解析方法复杂；

```java
public static void main(String[] args) {
        System.out.println(toJson(new user(1,"张三","男",new Date())));
    }
    public static String toJson(Object obj){
        String re=null;
        //对象映射
        ObjectMapper objectMapper=new ObjectMapper();
        //设置时间格式
        SimpleDateFormat dateFormat=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        objectMapper.setDateFormat(dateFormat);
        try {
            re=objectMapper.writeValueAsString(obj);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return re;
    }
```



#### FastJson

FastJson是阿里巴巴公司提供的一个用Java语言编写的高性能功能完善的JSON库，该库涉及的最基本功能就是序列化和反序列化。Fastjson支持java bean的直接序列化,同时也支持集合、Map、日期、Enum和泛型等的序列化。你可以使用com.alibaba.fastjson.JSON这个类进行序列化和反序列化，常用的序列化操作都可以在JSON类上的静态方法直接完成。Fastjson采用独创的算法，将parse的速度提升到极致，号称超过所有Json库。

1、快速FAST（比任何一款都快） 
2、面向对象 
3、功能强大（支持普通JDK类任意java bean Class,Collection,Map,Date或者enum） 
4、零依赖（只需要有JDK即可） 
5、支持注解，全类型序列化

```java
JSON.toJSONString(new user(1, "张三", "男", new Date())
```



fastjson存在很多安全问题，虽然历史版本发现的问题都被修复了，但是为了安全考虑，还是不建议使用。

https://zhuanlan.zhihu.com/p/157211675



#### Gson

 Google提供的用来java对象和JSON数据之间进行映射的JAVA类库，可以将一个JSON字符转成一个java对象，反过来也OK。

1、快速，高效 
2、代码量少 
3、面向对象 
4、数据传输解析方便 

注意事项

1、内部嵌套的类必须是static的，要不然解析会出错； 
2、类里面的属性名必须跟Json字段里面的Key是一模一样的； 
3、内部嵌套的用[]括起来的部分是一个List，所以定义为 public List< B> b，而只用{}嵌套的就定义为 public C c，是不是很简单，而且现在android studio上可以直接用插件生成实体类，那更加方便了

```java
public static void main(String[] args) {
        System.out.println(toJson(new user(1, "张三", "男", new Date())));
    }
    public static String toJson(Object obj){
        String re=null;
            Gson gson=new Gson();
        re= gson.toJson(obj);
        return  re;
    }

//反序列化 gson.formJson()
// List<String> ls = gson.fromJson(aaa,new TypeToken<List<String>>(){}.getType());
```

FastJson和jackson在把对象序列化成json字符串的时候，是通过遍历出该类中的所有getter方法进行的。Gson并不是这么做的，他是通过反射遍历该类中的所有属性，并把其值序列化成json。



### 对比

![image-20210806172117714](CommonNotes.assets/image-20210806172117714.png)

## Corn Expression

Cron表达式是一个具有时间含义的字符串，字符串以5个空格隔开，分为6个域，格式为`X X X X X X`。其中`X`是一个域的占位符。单个域有多个取值时，使用半角逗号`,`隔开取值。每个域可以是确定的取值，也可以是具有逻辑意义的特殊字符。

| 域   | 是否必需 | 取值范围                                                     | 特殊字符      |
| :--- | :------- | :----------------------------------------------------------- | :------------ |
| 秒   | 是       | [0, 59]                                                      | * , - /       |
| 分钟 | 是       | [0, 59]                                                      | * , - /       |
| 小时 | 是       | [0, 23]                                                      | * , - /       |
| 日期 | 是       | [1, 31]                                                      | * , - / ? L W |
| 月份 | 是       | [1, 12]或[JAN, DEC]                                          | * , - /       |
| 星期 | 是       | [1, 7]或[MON, SUN]。若您使用[1, 7]表达方式，`1`代表星期一，`7`代表星期日。 | * , - / ? L # |



| 特殊字符 | 含义                                                         | 示例                                                         |
| :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| `*`      | 所有可能的值。                                               | 在月域中，`*`表示每个月；在星期域中，`*`表示星期的每一天。   |
| `,`      | 列出枚举值。                                                 | 在分钟域中，`5,20`表示分别在5分钟和20分钟触发一次。          |
| `-`      | 范围。                                                       | 在分钟域中，`5-20`表示从5分钟到20分钟之间每隔一分钟触发一次。 |
| `/`      | 指定数值的增量。                                             | 在分钟域中，`0/15`表示从第0分钟开始，每15分钟。在分钟域中`3/20`表示从第3分钟开始，每20分钟。 |
| `?`      | 不指定值，仅日期和星期域支持该字符。                         | 当日期或星期域其中之一被指定了值以后，为了避免冲突，需要将另一个域的值设为`?`。 |
| `L`      | 单词Last的首字母，表示最后一天，仅日期和星期域支持该字符。**说明** 指定 `L`字符时，避免指定列表或者范围，否则，会导致逻辑问题。 | 在日期域中，`L`表示某个月的最后一天。在星期域中，`L`表示一个星期的最后一天，也就是星期日（`SUN`）。如果在`L`前有具体的内容，例如，在星期域中的`6L`表示这个月的最后一个星期六。 |
| `W`      | 除周末以外的有效工作日，在离指定日期的最近的有效工作日触发事件。`W`字符寻找最近有效工作日时不会跨过当前月份，连用字符`LW`时表示为指定月份的最后一个工作日。 | 在日期域中`5W`，如果5日是星期六，则将在最近的工作日星期五，即4日触发。如果5日是星期天，则将在最近的工作日星期一，即6日触发；如果5日在星期一到星期五中的一天，则就在5日触发。 |
| `#`      | 确定每个月第几个星期几，仅星期域支持该字符。                 | 在星期域中，`4#2`表示某月的第二个星期四。                    |



| 示例                 | 说明                                                         |
| :------------------- | :----------------------------------------------------------- |
| `0 15 10 ? * *`      | 每天上午10:15执行任务                                        |
| `0 15 10 * * ?`      | 每天上午10:15执行任务                                        |
| `0 0 12 * * ?`       | 每天中午12:00执行任务                                        |
| `0 0 10,14,16 * * ?` | 每天上午10:00点、下午14:00以及下午16:00执行任务              |
| `0 0/30 9-17 * * ?`  | 每天上午09:00到下午17:00时间段内每隔半小时执行任务           |
| `0 * 14 * * ?`       | 每天下午14:00到下午14:59时间段内每隔1分钟执行任务            |
| `0 0-5 14 * * ?`     | 每天下午14:00到下午14:05时间段内每隔1分钟执行任务            |
| `0 0/5 14 * * ?`     | 每天下午14:00到下午14:55时间段内每隔5分钟执行任务            |
| `0 0/5 14,18 * * ?`  | 每天下午14:00到下午14:55、下午18:00到下午18:55时间段内每隔5分钟执行任务 |
| `0 0 12 ? * WED`     | 每个星期三中午12:00执行任务                                  |
| `0 15 10 15 * ?`     | 每月15日上午10:15执行任务                                    |
| `0 15 10 L * ?`      | 每月最后一日上午10:15执行任务                                |
| `0 15 10 ? * 6L`     | 每月最后一个星期六上午10:15执行任务                          |
| `0 15 10 ? * 6#3`    | 每月第三个星期六上午10:15执行任务                            |
| `0 10,44 14 ? 3 WED` | 每年3月的每个星期三下午14:10和14:44执行任务                  |



## IaC

”基础设施即代码”(IaC)

