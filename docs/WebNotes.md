# Web Notes

## HTTP

### Header

#### Content-Encoding

`Content-Encoding`实体头用于压缩媒体类型。如果存在，它的值表示哪些编码应用于实体主体。它让客户知道，如何解码以获取`Content-Type`标题引用的媒体类型。

建议尽可能压缩数据并因此使用此字段，但某些类型的资源（如 jpeg 图像）已被压缩。有时使用额外的压缩不会减少有效载荷的大小，甚至可能使有效载荷更长。

```bash
Content-Encoding: gzip
Content-Encoding: compress
Content-Encoding: deflate
Content-Encoding: identity
Content-Encoding: br

// Multiple, in the order in which they were applied
Content-Encoding: gzip, identity
Content-Encoding: deflate, gzip
```

`gzip`一种使用 [Lempel-Ziv 编码 ](_images/http://en.wikipedia.org/wiki/LZ77_and_LZ78#LZ77)（ LZ77 ）和32位 CRC 的格式。这最初是 UNIX *gzip* 程序的格式。

`x-gzip`为了兼容性的目的，HTTP / 1.1 标准还建议支持该内容编码的服务器应该将其识别为别名。

`compress`使用 [Lempel-Ziv-Welch] (http://en.wikipedia.org/wiki/LZW)（ LZW ）算法的格式。值名取自实施此算法的 UNIX *压缩*程序。

`deflate`使用 [*deflate* ] (http://en.wikipedia.org/wiki/DEFLATE)压缩算法（在 [RFC 1951中](_images/http://tools.ietf.org/html/rfc1952)定义）使用 [zlib ] (http://en.wikipedia.org/wiki/Zlib)结构（在 [RFC 1950中](_images/http://tools.ietf.org/html/rfc1950)定义）。

`identity`指示身份功能（即不压缩，也不修改）。除非明确指定，否则此标记始终被视为可接受。

`br`使用 [Brotli ] (https://en.wikipedia.org/wiki/Brotli)算法的格式。



例子：用 gzip 压缩

在客户端，您可以公布一个将在 HTTP 请求中发送的压缩方案列表。`Accept-Encoding` header 被用于协商内容编码。

```javascript
Accept-Encoding: gzip, deflate
```

服务器响应所使用的方案，由`Content-Encoding`响应 header 。

```javascript
Content-Encoding: gzip
```

服务器需要手动按约定进行编码，Content-Encoding只是声明



## 





