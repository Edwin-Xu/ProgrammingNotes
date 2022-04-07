# FrontEnd Notes

## CSS

### Stryle

#### word-break

```css
style="word-break: break-word"
```

单词内换行

## Vue

### 绑定与深克隆

使用v-model绑定一个对象时，如果要更新对象，尽量全局更新，而不是对该对象的一个个属性逐个更新

### 生命周期

#### activated

说到activated不得不提到[keep-alive](https://cn.vuejs.org/v2/api/#keep-alive)，你切换出去又切出来会调用到它。（你可以理解为生命周期钩子函数，用法也一样）

**activated**：是组件被激活后的钩子函数，`每次回到页面都会执行`

1.这里有个关键词是实例，也就是说如果你用了$refs，你就得注意了。
2.mounted先执行，首次进入时候两个一起执行



## JS

### 三点运算符

三个点（...）真名叫扩展运算符，是在ES6中新增加的内容，它可以在函数调用/数组构造时，将数组表达式或者string在语法层面展开；还可以在构造字面量对象时将对象表达式按照key-value的方式展开

说白了就是把衣服脱了，不管是大括号（[]）、花括号（{}），统统不在话下，**全部脱掉脱掉！**

```javascript
// 数组
var number = [1,2,3,4,5,6]
console.log(...number) //1 2 3 4 5 6
//对象
var man = {name:'chuichui',height:176}
console.log({...man}) / {name:'chuichui',height:176}
```

注意，只能脱一层。

可以用来实现浅克隆.

```javascript
const form = { ...this.form }

form.meta = { ...this.form.meta }
form.model = { ...this.form.model } // 手动深克隆
```

当我们想把数组中的元素迭代为函数参数时，用它！

### Clone

#### `Object.assign()` Method

浅拷贝，简单快速，ES6

`Object.assign(target, source1, soure2, ...)` method. This method copies all enumerable own properties of one or more source objects to a target object, and returns the target object:

```javascript
const moreFruits = Object.assign({}, fruits);
```

#### Spread Operator

The spread operator (`...`)

ES6 浅拷贝

和Object.assign()类似

```javascript
const moreFruits = { ...fruits };
```

#### JSON Methods

If your object only contains primitive types, and doesn't include nested or external objects, arrays, `Date` objects, functions, and so on, you can easily create a deep clone of the object by using [JSON methods] (https://attacomsian.com/blog/json-parse-stringify): `JSON.stringify()` and `JSON.parse()`:

#### Lodash's `cloneDeep()` Method

[Lodash] (https://lodash.com/docs/4.17.15#cloneDeep) provides the `cloneDeep()` method that recursively copies everything in the original object to the new object. It works for all data types, including functions, nested objects, arrays, and symbols.

```javascript
const _ = require('lodash');

const obj = {
    name: 'John Doe',
    age: 45,
    address: {
        city: 'Berlin',
        country: 'DE'
    },
    job: undefined,
    credits: Infinity
};

const cloned = _.cloneDeep(obj);

console.log(cloned);
```

### delete

 **`delete` 操作符**用于删除对象的某个属性；如果没有指向这个属性的引用，那它最终会被释放。

```javascript
const Employee = {
  firstname: 'John',
  lastname: 'Doe'
};

console.log(Employee.firstname);
// expected output: "John"

delete Employee.firstname;

console.log(Employee.firstname);
// expected output: undefined
```

 *expression* 的计算结果应该是某个属性的引用，例如：

```javascript
delete object.property
delete object['property']
```

对于所有情况都是`true`，除非属性是一个[`自身的`][`不可配置`]的属性，在这种情况下，非严格模式返回 `false`。

注意：

- 如果你试图删除的属性不存在，那么delete将不会起任何作用，但仍会返回true

- 如果对象的原型链上有一个与待删除属性同名的属性，那么删除属性之后，对象会使用原型链上的那个属性（也就是说，delete操作只会在自身的属性上起作用）

- 任何使用 

  `var`

   声明的属性不能从全局作用域或函数的作用域中删除。

  - 这样的话，delete操作不能删除任何在全局作用域中的函数（无论这个函数是来自于函数声明或函数表达式）
  - 除了在全局作用域中的函数不能被删除，在对象(object)中的函数是能够用delete操作删除的。

- 任何用[`let`]或[`const`]声明的属性不能够从它被声明的作用域中删除。

- 不可设置的(Non-configurable)属性不能被移除。这意味着像[`Math`], [`Array`], [`Object`]内置对象的属性以及使用[`Object.defineProperty()`]方法设置为不可设置的属性不能被删除。

### if

null、undefined、0都会被判false



0：注意





## Webpack

### webpackJsonp 

vue打包上线项目报错webpackJsonp is not defined

在[vue]单页面项目出现该问题是由于使用了CommonsChunkPlugin这个插件。
场景： 本地调试是没有问题，但是打包上线就会出现 `Uncaught ReferenceError: webpackJsonp is not defined`

原因：这是因为**公共文件必须在自己引用的js文件之前引用**。

方案：
文件位置 build/[webpack](https://so.csdn.net/so/search?from=pc_blog_highlight&q=webpack).prod.conf.js
添加代码：

```java
  chunks: ['manifest', 'vendor', 'app'],
```



```html
new HtmlWebpackPlugin({
  filename: 'index.html',
  template: 'index.html',
  inject: true,
  favicon: resolveApp('favicon.ico'),
  minify: {
    removeComments: true,
    collapseWhitespace: true,
    removeRedundantAttributes: true,
    useShortDoctype: true,
    removeEmptyAttributes: true,
    removeStyleLinkTypeAttributes: true,
    keepClosingSlash: true,
    minifyJS: true,
    minifyCSS: true,
    minifyURLs: true
  },
  path: config.build.assetsPublicPath + config.build.assetsSubDirectory,
  // necessary to consistently work with multiple chunks via CommonsChunkPlugin

	// 解决打包公用代码没用添加进去
    chunks: ['manifest', 'vendor', 'app'],

  chunksSortMode: 'dependency'
}),
```



## Node.js

### node-gyp

gyp:generate your project

gyp是一种根据c++源代码编译的工具，node-gyp就是为node编译c++扩展的时候使用的编译工具。





## 组件库

### Lodash

https://www.lodashjs.com/

Lodash 是一个一致性、模块化、高性能的 JavaScript 实用工具库













