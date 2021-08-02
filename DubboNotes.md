# Dubbo Notes



## 基础知识



### Stub

桩的应用

dubbo stub：

 相当于代理，通过它转发，可以增强。

用法：

- cache
- 服务降级
- 统一异常处理

sub需要一个使用对应server的构造方法



dubbo filter做监控





## problems

### timeout过小导致连接不上问题

```yml
dubbo:
	registry:
		address: zookeeper://42.192.203.208:2181
		timeout: 30000
```

**timeout默认值太小了，容易连不上，需要设置大一点**

