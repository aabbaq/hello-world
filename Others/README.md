# 一些怪东西

### Magic Number 魔数

之前只认识程序里的魔数，没有标识出具体含义意义不明的数字，尽量少用，这个情况一般出现在常量定义与赋值上，不好修改也不好识别，除此以外，还有一些其他含义：

- 0x5f3759df：[**平方根倒数速算法**](https://en.wikipedia.org/wiki/Fast_inverse_square_root)，i = 0x5f3759df - ( i >> 1 )，求一个数的平方根倒数，看的不是很明白，但是这个数字很神奇；

- 标识文件格式的魔数：
  1. `FF D8` & `FF D9`：JPEG文件开头与结尾；
  2. `52 50 44 46`：PDF文件开头（%PDF）；
  3. `CA FE BA BE`：Java Class文件开头；

参考：

- [知乎 编程中的「魔数」（magic number）是什么意思？平时我们能接触到哪些魔数？](https://www.zhihu.com/question/22018894)

- [维基 Magic number (programming)](https://en.wikipedia.org/wiki/Magic_number_(programming))