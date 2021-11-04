# Algorithm Notes

## 位运算

### LSB MSB

**最低有效位**（**the least significant bit**，**lsb**）是指一个二进制数字中的第0位（即最低位），具有权值为2^0，可以用它来检测数的奇偶性。与之相反的称之为最高有效位。在大端序中，lsb指最右边的位



**最高有效位**（**the Most Significant Bit**，**msb**），是指一个n位二进制数字中的n-1位，具有最高的权值2^n − 1。与之相反的称之为最低有效位。在大端序中，msb即指最左端的位。

### xor & (-xor)

取异或值最后一个二进制位为 1 的数字作为 mask，如果是 1 则表示两个数字在这一位上不同。

```java
  int mask = xor & (-xor);
```