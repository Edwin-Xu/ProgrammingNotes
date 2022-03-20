# Blog

> Edwin Xu's blogs, wikis and so on.

## 博客搭建

### Hexo 

### docsify

https://docsify.js.org/#/zh-cn/?id=docsify

一个神奇的文档网站生成器。

docsify 可以快速帮你生成文档网站。不同于 GitBook、Hexo 的地方是它不会生成静态的 `.html` 文件，所有转换工作都是在运行时。如果你想要开始使用它，只需要创建一个 `index.html` 就可以开始编写文档并直接[部署在 GitHub Pages](https://docsify.js.org/#/zh-cn/deploy)。

- 无需构建，写完文档直接发布
- 容易使用并且轻量 (压缩后 ~21kB)
- 智能的全文搜索
- 提供多套主题
- 丰富的 API
- 支持 Emoji
- 兼容 IE11
- 支持服务端渲染 SSR

index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Edwin Xu Notes</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Description">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '',
      repo: ''
    }
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <!-- PDF Embed Plugin -->
  <!-- PDFObject.js is a required dependency of this plugin -->
  <script src="//cdnjs.cloudflare.com/ajax/libs/pdfobject/2.1.1/pdfobject.min.js"></script> 
  <!-- docsify-pdf-embed.js  -->
  <script src="//unpkg.com/docsify-pdf-embed-plugin/src/docsify-pdf-embed.js"></script>
</body>
</html>

```



## 基于反射的工具类的使用思考

看到项目中有使用一些工具类，比如Spring提供的BeanUtils，其中copyProperties可以拷贝两个对象的属性值(浅拷贝)，这样可以大大方面我们的使用，但是个人对其性能也表示怀疑，于是做了一番探究。

写两个属性相同的类，使用不同数量的对象，进行拷贝

```java
public class Test {
    @AllArgsConstructor
    @NoArgsConstructor
    @Getter
    @ToString
    private static class A{
        String a;
        String b;
        String c;
        String d;
        String e;
    }
    @AllArgsConstructor
    @NoArgsConstructor
    @Setter
    private static class B {
        String a;
        String b;
        String c;
        String d;
        String e;
    }

    /**
     * 手动copy
     * */
    public static void copyProperties(A a, B b){
        b.a = a.a;
        b.b = a.b;
        b.c = a.c;
        b.d = a.d;
        b.e = a.e;
    }

    public static void main(String[] args) {
        int size = 1000000;
        final ArrayList<A> as = new ArrayList<>(size);
        final ArrayList<B> bs1 = new ArrayList<>(size);
        final ArrayList<B> bs2 = new ArrayList<>(size);

        for (int i = 0; i < size; i++) {
            as.add(new A("a"+i, "b"+i, "c"+i, "d"+i, "e"+i));
            bs1.add(new B());
            bs2.add(new B());
        }

        long start = System.currentTimeMillis();
        for (int i = 0; i < size; i++) {
            BeanUtils.copyProperties(as.get(i), bs1.get(i));
        }
        System.out.println("BeanUtils.copyProperties():"+(System.currentTimeMillis() - start));

        start = System.currentTimeMillis();
        for (int i = 0; i < size; i++) {
            copyProperties(as.get(i), bs2.get(i));
        }
        System.out.println("My copyProperties():" + (System.currentTimeMillis() - start));
    }
}
```

1-1000000的数据量复制耗时统计

```java
/* 数据量    BeanUtils.copyProperties()耗时 手动复制耗时
 * 1:       1121                            0
 * 10:      1125                            0
 * 100:     1178                            0
 * 1000:    1107                            1
 * 10000:   1218                            2
 * 100000:  1887                            52
 * 1000000: 2663                            161
 * */
```

可以发现BeanUtils.copyProperties()耗时远高于手动属性拷贝。但是随着数据量的增加，前者的增量却不大，用经济学的话来说就是边际成本很小。

进一步探索，打印每次拷贝所有的时长：

```java
1373 0 0 1 0 0 0 0 0 0 0 0 0 0 0 12 1 0 0 0 
BeanUtils.copyProperties():1387
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
My copyProperties():3
```

发现BeanUtils.copyProperties()只有第一次会非常耗时，因为其底层使用反射，在类加载时会消耗大量时间，而只有第一次使用才会进行类加载，故后面的使用速度相对很快，不过和手动set还是有一定差距。

所以在一些对性能要求很高的程序中应该尽量避免使用，对于其他工具类也一样。







