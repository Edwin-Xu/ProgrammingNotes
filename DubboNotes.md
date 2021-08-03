# Dubbo Notes

## 服务通信协议

### RPC

RPC，一台机器通过网络远程调用另一台机器上的服务

RPC四个点：

- 资源定位
- 服务发现
- 协议格式
- 数据传输

### HTTP

- URI
- URL
- URN

### TCP

tcp连接的建立和关闭开销很大

- **长连接** (通过心跳机制保持连接)
- **连接池**



### 序列化

Jackson

- @JsonIgnore
- @JsonProperty
- @JsonCreator

使用mapper序列化





## 基础知识

公司的Dubbo服务治理平台

http://cactus.dev.qunar.com/



QunarAsyncClient, 支持异步、高性能、封装了调用者信息



官方与QUNAR的异步 不一样，建议使用公司的



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

