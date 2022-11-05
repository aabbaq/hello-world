## [95.不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees-ii/)

给你一个整数 `n` ，请你生成并返回所有由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的不同 **二叉搜索树** 。可以按 **任意顺序** 返回答案。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 递归，设置一个递归函数，这个函数会产生从start到end之间树的列表
        def search(start, end):
            # 终止条件，注意返回一个列表
            if start > end:
                return [None]
            # 初始化
            res = []
            # 思路是在范围内选root的值，根据bst的规则，左侧start到i-1，右侧i+1到end（闭区间）搜索
            for i in range(start, end+1):
                left_trees = search(start, i-1)
                right_trees = search(i+1, end)
                # 返回的值依然是列表，两个循环组合一遍
                for left in left_trees:
                    for right in right_trees:
                        # 此时列表内已经处理好，没有处理好的是root
                        curr_node = TreeNode(val=i)
                        curr_node.left = left
                        curr_node.right = right
                        res.append(curr_node)
            return res
        # 题目给的节点从1~n，不是0
        return search(1, n)
```
本来在找DP的题目，但是不知道这个题为什么分类在DP中，而且只是一个递归，很像回溯（一个列表，返回所有排列）。

---

## [97.交错字符串](https://leetcode.cn/problems/interleaving-string/)

给定三个字符串 `s1`、`s2`、`s3`，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2` **交错** 组成的。

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        # 长度不相等时的特殊判定，这里需要不是为了提升速度，而是这个dp解法只能保证l1*l2范围内的正确性
        if len(s3) != l1+l2:
            return False
		# 初始化二维列表
        dp = [[False]*(l2+1) for _ in range(l1+1)]
        # 长度为0的空字符串一定可以交错（根据题目描述）
        dp[0][0] = True
		
        # 一般来说dp会初始化第一行行与列，这里寻找s1与s3的相同头部，也可以用dp推导（dp[i-1][0] and s1[i-1]==s3[i-1]）
        for i in range(1, l1+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
        
        # 同理寻找s2与s3
        for j in range(1, l2+1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True
        # dp主循环，经典双层，并且从1开始
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                # 转移方程，有两种方式转移，代表了s1与s2交错的方式（谁先谁后）
                # 注意+1长度的dp列表中的索引（之前做过的字符串算法dp[i-1]一般和s[i]产生联系）
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[-1][-1]
```

一开始没啥思路，碰到这种有关于子串的题目，不知道如何增减索引进行对比，我觉得我对不确定更新范围的处理PTSD。但是其实就是一个字符对比，逐渐更新DP。

---

## [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/)

给定一个三角形 `triangle` ，找出自顶向下的最小路径和。

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int: 
        l = len(triangle)
        # 虽然是dp，但是只用到了三角型部分的矩阵，求最小值初始化为最大值
        dp = [[math.inf]*l for _ in range(l)]
		# 按要求triangle列表长度至少为1，初始化第一个（相当于第一行）
        dp[0][0] = triangle[0][0]

        # 经典循环，行从第二行（索引1）开始，列到行索引为止
        for i in range(1, l):
            for j in range(i+1):
                # 转移方程，只能从上层左侧或正上方转移
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        # 返回最后一行的最小值
        return min(dp[-1])
```

标的是中等，觉得应该划到简单里。