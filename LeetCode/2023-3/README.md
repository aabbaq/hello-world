# 每日一题

## [面试题 05.02. 二进制数转字符串](https://leetcode.cn/problems/bianry-number-to-string-lcci/)

二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

```java
class Solution {
    public String printBin(double num) {
        StringBuilder sb = new StringBuilder("0.");
        int y;
        for (int i=0; i<32; i++) {
            num *= 2;
            if (num < 1) {
                sb.append('0');
            } else if (num > 1) {
                sb.append('1');
                num -= 1;
            } else {
                sb.append('1');
                return sb.toString();
            }
        }
        return "ERROR";
    }
}
```

这里是一个如何表示二进制小数的概念，不断将该小数*2，取整数位的数字作为二进制表示，接着将小数位置的数字继续进行此操作；这个循环直到最后整数位数字为1，小数为0时，也就是计算结果为1的时候结束。若超出位数限制（32次）则返回一个ERROR。注意这里也要加上一个整数位0，最后的计算结果表示为0.11001...；

此外，可以在这里证明事实上循环六次就可以满足条件了：[证明：至多循环 6 次](https://leetcode.cn/problems/bianry-number-to-string-lcci/solution/zheng-ming-zhi-duo-xun-huan-6-ci-pythonj-b6sj/)

## [1487. 保证文件名唯一](https://leetcode.cn/problems/making-file-names-unique/)

给你一个长度为 `n` 的字符串数组 `names` 。你将会在文件系统中创建 `n` 个文件夹：在第 `i` 分钟，新建名为 `names[i]` 的文件。

由于两个文件 **不能** 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 `(k)` 的形式为新文件夹的文件名添加后缀，其中 `k` 是能保证文件名唯一的 **最小正整数** 。

返回长度为 *`n`* 的字符串数组，其中 `ans[i]` 是创建第 `i` 个文件夹时系统分配给该文件夹的实际名称。

```java
class Solution {
    public String[] getFolderNames(String[] names) {
        HashMap<String, Integer> map = new HashMap<>();
        String[] res= new String[names.length];
        int len = names.length;
        for (int i=0; i<len; i++) {
            String name = names[i];
            if (!map.containsKey(name)) {
                map.put(name, 1);
                res[i] = name;
            } else {
                int nextNum = map.get(name);
                StringBuilder sb = new StringBuilder(name);
                sb.append("(");
                sb.append(nextNum);
                sb.append(")");
                while (map.containsKey(sb.toString())) {
                    nextNum += 1;
                    sb.setLength(name.length());
                    sb.append("(");
                    sb.append(nextNum);
                    sb.append(")");
                }
                map.put(name, nextNum);
                map.put(sb.toString(), 1);
                res[i] = sb.toString();
            }
        }
        return res;
    }
}
```

一开始使用的是set，每次检查是否存在name，若存在就从1开始不断尝试能否生成一个不存在的名字；这样做会超时；因此需要使用map存储一下目前已经存在的文件（这里我们存放下一个需要放在括号的数字），这样就不用从1开始了；另外，每次存放一个新文件，类似于xxx(y)的时候，可能将来也会插入一个一样的文件，带括号的那种，因此不仅要更新原来xxx的下一个生成序号，还需要添加一个xxx(y) 的下一个生成序号1，也就是 `xxx(y)(1)`  。
