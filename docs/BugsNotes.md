# Bugs

### Interesting Bugs

#### lastIndexOf

```java
// java
public int lastIndexOf(String str, int fromIndex);
// 注意这个fromIndex是从后往前的Index，而不是从前往后

String s = "xxxx.y.zzz.....";
int lastIndex = s.lastIndexOf(".", 5);
// 本来想找y后的第一个点，但是却找成了y前的第一个
```







