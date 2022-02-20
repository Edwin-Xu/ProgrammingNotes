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



## Cache

缓存分为本**地缓存与分布式缓存**。本地缓存为了保证[线程安全]问题，一般使用`ConcurrentMap`的方式保存在内存之中，而常见的分布式缓存则有`Redis`，`MongoDB`等。

- 一致性：本地缓存由于数据存储于内存之中，每个实例都有自己的副本，可能会存在**不一致**的情况；**分布式缓存**则可有效避免这种情况
- 开销：本地缓存会**占用JVM内存**，会影响GC及系统性能；分布式缓存的开销则在于**网络时延和对象序列化**，故主要影响**调用时延**
- 适用场景：本地缓存适用于**数据量较小或变动较少**的数据；分布式缓存则适用于**一致性要求较高**及**数量量大**的场景(可弹性扩容)
  

Guava Cache 是Google Fuava中的一个内存缓存模块，用于将数据缓存到JVM内存中。

- 提供了get、put封装操作，能够集成数据源 ；
- 线程安全的缓存，与ConcurrentMap相似，但前者增加了更多的元素失效策略，后者只能显示的移除元素；
- Guava Cache提供了多种基本的缓存回收方式
- 监控缓存加载/命中情况
   

```sql
CacheBuilder.newBuilder()
		// 设置并发级别为cpu核心数，默认为4
	.concurrencyLevel(Runtime.getRuntime().availableProcessors()) 
	.initialCapacity(100)
	.maximumSize(1000)
		.build();

```

我们在构建缓存时可以为缓存设置一个合理大小初始容量，由于Guava的缓存使用了分离锁的机制，扩容的代价非常昂贵。所以合理的初始容量能够减少缓存容器的扩容次数。

Guava Cache可以在构建缓存对象时指定缓存所能够存储的最大记录数量。当Cache中的记录数量达到最大值后再调用put方法向其中添加对象，Guava会先从当前缓存的对象记录中选择一条删除掉，腾出空间后再将新的对象存储到Cache中。



缓存清除策略

- 基于存活时间的清除策略
  - expireAfterWrite 写缓存后多久过期
  - expireAfterAccess 读写缓存后多久过期
    存活时间策略可以单独设置或组合配置
- 基于容量的清除策略
  通过CacheBuilder.maximumSize(long)方法可以设置Cache的最大容量数，当缓存数量达到或接近该最大值时，Cache将清除掉那些最近最少使用的缓存

- 基于权重的清除 策略
  使用CacheBuilder.weigher(Weigher)指定一个权重函数，并且用CacheBuilder.maximumWeight(long)指定最大总重。如每一项缓存所占据的内存空间大小都不一样，可以看作它们有不同的“权重”（weights）,作为执行清除策略时优化回收的对象

- 显式清除

  - 清除单个key：`Cache.invalidate(key)`

  - 批量清除key：`Cache.invalidateAll(keys)`

  - 清除所有缓存项：`Cache.invalidateAll()`

- 基于引用的清除策略
  在构建Cache实例过程中，通过设置使用弱引用的键、或弱引用的值、或软引用的值，从而使JVM在GC时顺带实现缓存的清除
  CacheBuilder.weakKeys()：使用弱引用存储键。当键没有其它（强或软）引用时，缓存项可以被垃圾回收
  CacheBuilder.weakValues()：使用弱引用存储值。当值没有其它（强或软）引用时，缓存项可以被垃圾回收
  CacheBuilder.softValues()：使用软引用存储值。软引用只有在响应内存需要时，才按照全局最近最少使用的顺序回收。考虑到使用软引用的性能影响，我们通常建议使用更有性能预测性的缓存大小限定. 垃圾回收仅依赖`==`恒等式，使用弱引用键的缓存用而不是`equals()`，即同一对象引用。

### LoadingCache

使用自定义`ClassLoader`加载数据，置入内存中。从`LoadingCache`中获取数据时，若数据存在则直接返回；若数据不存在，则根据`ClassLoader`的`load`方法加载数据至内存，然后返回该数据

























