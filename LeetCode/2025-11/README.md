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