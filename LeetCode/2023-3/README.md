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

## [982. 按位与为零的三元组](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/)

给你一个整数数组 `nums` ，返回其中 **按位与三元组** 的数目。

**按位与三元组** 是由下标 `(i, j, k)` 组成的三元组，并满足下述全部条件：

- `0 <= i < nums.length`
- `0 <= j < nums.length`
- `0 <= k < nums.length`
- `nums[i] & nums[j] & nums[k] == 0` ，其中 `&` 表示按位与运算符。

```java
class Solution {
    public int countTriplets(int[] nums) {
        int[] count = new int[1 << 16];
        int res = 0;

        for(var a: nums) {
            for(var b: nums) {
                count[a&b] += 1;
            }
        }

        for(var num : nums) {
            for(int i=0; i< 1<<16; i++) {
                if((num & i) == 0)
                    res += count[i];
            }
        }

        return res;
    }
}
```

这一题有更好的做法，和子集有关；那么如果我没有相关知识，就得想想如何才能让整体的复杂度降低；首先题意非常清楚，使用三重循环遍历出每一个结果即可。这样会造成一些重复，例如前两个元组的元素与值相同（有重复元素），那么第三个元素和该值与运算后为0时，相当于重复计算了相同的值。

那么一种简单的思路是，将这些值出现的次数记录下来，然后对第三个值遍历的时候直接进行加算，那么复杂度从O(n^3) 降低为了 O(n^2 + n*2^16)；这里需要注意，这个范围是题目定的最大值，我们也可以使用哈希表来计算（计算之后哈希表反而慢一些，不知道为什么），而且数组大小也是通过位运算的右移设置的。

## [1599. 经营摩天轮的最大利润](https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/)

你正在经营一座摩天轮，该摩天轮共有 **4 个座舱** ，每个座舱 **最多可以容纳 4 位游客** 。你可以 **逆时针** 轮转座舱，但每次轮转都需要支付一定的运行成本 `runningCost` 。摩天轮每次轮转都恰好转动 1 / 4 周。

给你一个长度为 `n` 的数组 `customers` ， `customers[i]` 是在第 `i` 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 `i` 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 `boardingCost` ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。

你可以随时停下摩天轮，即便是 **在服务所有游客之前** 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，**将免费进行所有后续轮转**。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 **下一次轮转** 。

返回最大化利润所需执行的 **最小轮转次数** 。 如果不存在利润为正的方案，则返回 `-1` 。

```java
class Solution {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        int num = 0;
        int profit = 0;
        int sum = Arrays.stream(customers).sum();
        int i = 0;

        while (sum > 0) {
            if (sum*boardingCost <= runningCost) break;
            if (i < customers.length) num += customers[i];
            if (num > 4) {
                num -= 4;
                sum -= 4;
                profit += boardingCost*4 - runningCost;
            } else {
                profit += boardingCost*num - runningCost;
                sum -= num;
                num = 0;
            }
            i++;
        }
        return profit > 0 ? i : -1;
    }
}
```

很无聊的模拟题，维护一个剩余游客数量以及一个现在排队的游客数量。剩余游客数量用来计算是否需要停止服务，一旦剩下的游客不能获利了，那么就停止运营，这里注意等于也在条件判断内，因为如果可以获利0元，那么求最小轮转次数干脆就停止即可；另外一个是排队游客数量，用于分情况计算利润；最后利润>0就返回轮次，否则-1；
