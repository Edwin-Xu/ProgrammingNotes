# Guava

三点建议:

1. 调试

2. 结构化思维

3. 交流







set via CAS





什么时候开启多个线程来执行？

> 是否需要占用CPU？
>
> io密集型 CPU密集型
>
> CPU密集的单CPU下线程少比较好，没有切换开销。
>
> io密集的多线程比较好





设计锁需要考虑的因素

- 粒度：重量级 轻量级
- 使用场景：读写锁、CountDownLatch、CyclicBarrier
- 公平性：公平、非公平
- 开销/性能/并发/阻塞
- 



## 数值处理

### Ints

Ints用于补充Integer和Arrays中对Int类型的操作



### Objects & MoreObjects

```java
Objects.requireNonNull(args);
System.out.println(Objects.equals(new Integer(0), new Integer(0)));
System.out.println(Objects.deepEquals(new Integer(0), new Integer(0)));


// 返回第一个不为null的
System.out.println(MoreObjects.firstNonNull(null, 1));
```



### Optional

### 函数式编程

Guava也提供Function和Predictate

```java
public static <F, T> List<T> transform(
    List<F> fromList, Function<? super F, ? extends T> function) {
```

```java
public static <T> @Nullable T find(
    Iterable<? extends T> iterable, Predicate<? super T> predicate, @Nullable T defaultValue) 
```

过度使用函数式编程会导致代码冗长混乱可读性差



什么使用需要使用函数式编程？

- 代码行减少
- 为了提高效率，转换集合的结果需要使用懒视图，而不是明确计算的结果







## 字符串处理

### Strings

String工具类

- isNullOrEmpty
- nullToEmpty
- emptyToNull
- padStart(str, num, 'c'): 往str前面添加字符c，使总长度是num
- padEdnd
- repeat
- commonPrefix
- commonSuffix

### Joiner

```java
System.out.println(Joiner.on("||").useForNull("NULL").join(list));
```

### Splitter

**Splitter用于将字符串按照某个separator分割为list或者map**



Splitter MapSplitter

Immutable ThreadSafe

trimResults omitEmptyStrings

```java
String str  = ",1,2,3,4,";
final Iterable<String> split = Splitter.on(",").split(str);
split.forEach(System.out::println);

System.out.println("===========");
Splitter.on(",").trimResults().omitEmptyStrings().split(str).forEach(System.out::println);

str = "a=1&b=2&c=3";
final Map<String, String> map = Splitter.on("&").withKeyValueSeparator("=").split(str);

map.forEach((s, s2) -> System.out.println(s +" > "+s2));
```



### intern

1 String中的intern方法有什么作用？ 
2 对比一下Guava的**Interners**。





## 异常处理

### Throwables

```java
// 获取异常链
public static List<Throwable> getCausalChain(Throwable throwable) 
// 获取最原始的异常
public static Throwable getRootCause(Throwable throwable) {
// 类似 SneakyThrows, 包装为RuntimeExecption 返回
public static RuntimeException propagate(Throwable throwable) {


```



## 容器

###  工具类

- **Lists **

- **Sets **

- **Maps**
- **Iterables**
- 



### 容器

asList 、asMap等返回的视图，会影响到原数据 

#### Multiset



#### MultiMap

ListMultiMap

SetMultiMAp

HashMultiMAp

TreeMultiMap



#### BiMap

#### RangeMap RangeSet







写个例子证明SimpleDateFormat不是线程安全的





## IO

### java io



### guava io

更高层的抽象

更方便的工具类



ByteStreams & CharStreams



Files Resources

源 与 汇：Source and Sink













































