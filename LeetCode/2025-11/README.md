# 每日一题

又回来了，好久都没有做算法题了。有些话我想放在其他地方说，这里就不提了，这里的每日一题也并不是总是LeetCode推荐的每日一题。大概率我选择的没有做过的题目，一天不止一题的情况也是有的。

## [3512. 使数组和能被 K 整除的最少操作次数](https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k/)

给你一个整数数组 `nums` 和一个整数 `k`。你可以执行以下操作任意次：

- 选择一个下标 `i`，并将 `` 替换为 `nums[i] - 1`。

返回使数组元素之和能被 `k` 整除所需的**最小**操作次数。

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
```

看错题目了，看成 `nums[i]` 替换成 `nums[i-1] -1` ，看了半天真想不出来是怎么解。

## [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/)

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

```java
class Solution {
    public int findPeakElement(int[] nums) {
        // edge of array, check
        int n = nums.length;
        if (n == 1) return 0;
        if (nums[0] > nums[1]) return 0;
        if (nums[n-1] >nums[n-2]) return n-1;

        
        int left = 0;
        int right = n;
        int idx = (left+right) / 2;
        while (idx > 0 && idx < n-1) {
            int prev = nums[idx-1];
            int curr = nums[idx];
            int next = nums[idx+1];
            if (prev < curr && curr > next) {
                return idx;
            }
            if (prev > curr) {
                right = idx;
                idx = (left+right) / 2;
                continue;
            }
            if (next > curr) {
                left = idx;
                idx = (left+right) / 2;
            }
        }
        return idx;
    }
}
```

log n复杂度很容易联想到二分法，但是如何确定二分法的查找方向是这题的考点。假设我们选中一个点，相邻的点如果比该点大那么说明趋势是往顶点走的，而且必定会有一个顶点，因为题目规定超出边界的点必然比数组的边界点小。这就导致了上升趋势必然停止在某处（目标点），这样即可确定查找方向了。当然如果是谷底的话，那么选哪边都无所谓了，可以把边界检查提前来加快运行速度。

## [1590. 使数组和能被 P 整除](https://leetcode.cn/problems/make-sum-divisible-by-p/)

给你一个正整数数组 `nums`，请你移除 **最短** 子数组（可以为 **空**），使得剩余元素的 **和** 能被 `p` 整除。 **不允许** 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 `-1` 。

**子数组** 定义为原数组中连续的一组元素。

```java
class Solution {
    public int minSubarray(int[] nums, int p) {
        var map = new HashMap<Integer, Integer>();
        int n = nums.length;
        int[] prefixSums = new int[n+1];
        int res = n;

        for (int i=0; i<n; i++) {
            prefixSums[i+1] = (prefixSums[i] + nums[i]) % p;
        }

        // final remainder
        int r = prefixSums[n];
        if (r == 0) return 0;

        for (int i=0; i<n+1; i++) {
            map.put(prefixSums[i], i-1);
            int tmpR = (prefixSums[i] - r + p)  % p;
            if (map.containsKey(tmpR)) {
                int minLength = i-1-map.get(tmpR);
                res = Math.min(res, minLength);
            }
        }

        return res == n ? -1 : res;
    }
```

最折磨的一集，提交了7次才过。这题思路需要很明确并且还要知道余数公式才能顺利做出来。首先看题目求和算余数，并且去除一个子数组（相当于：数组和Sum-子数组和SubSum）很容易联想到前缀和的方法。问题是怎么找到这个子数组。

1. 求得数组和Sum后找到余数r，那么目标变为找到一个子数组他的和拥有相同的余数r：
   $$
   (prefix[right+1]−prefix[left])\bmod p = r
   $$
   这个式子可以转化为:
   $$
   (prefix[right+1]−r) \bmod p = prefix[left] \bmod p
   $$
   这样，相当于遍历到 `idx=right+1` 时，找到一个 `left` 能够使等式成立，那么就相当于找到了一个可能得子数组，计算这个数组的长度 `right-left+1` 更新最小长度即可。 

2.  思路是这样一个思路，但是有几个坑：

   1. 前缀和可能超出Integer范围，这个可以通过每次求和后取模解决：
      $$
      (a+b)\bmod k=((a\bmod k)+(b\bmod k))\bmod k
      $$

   2. `r` 余数可能大于计算的前缀和的余数，这样会对负数取模，解决方法是计算时补充一个p进行求解 `(prefixSums[i+1] - r + p)  % p`

   3. 根据上述思路，我们是遍历到 `right+1` 时寻找是否有满足条件的 `left`，那么我们需要把等式右侧的 `prefixSums[left]` 对应的索引值记录下来，并且要求 `left` 越大越好，这样使用一个 `HashMap` 在遍历时更新值和索引即可

   4. 由于我们这里直接保存了整个前缀和数组，并且我习惯是 `prefixSums[i+1] = prefixSums[i] + nums[i]` ，所以没有初始化 `HashMap`  的特殊处理了，而且可以看到第二个循环里是用不到 `nums` 这个数组的。

