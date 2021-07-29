# Dubbo Notes

## problems

### timeout过小导致连接不上问题

```yml
dubbo:
	registry:
		address: zookeeper://42.192.203.208:2181
		timeout: 30000
```

**timeout默认值太小了，容易连不上，需要设置大一点**

