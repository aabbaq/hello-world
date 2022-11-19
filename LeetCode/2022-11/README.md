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

---

## [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # 回溯递归，参数是目前搜索的列表（比起字符串增减容易），左右括号的个数
        def search(_res, left, right):
            # 终止条件，当前列表长度为2倍的n，添加到结果列表中
            if len(_res) == 2*n:
                res.append(''.join(_res))
                return
            # 保证终止条件中的组合是正确的关键，左括号数在进入下一层递归时小于一半的长度，这样下层递归就会刚好为n个左括号（最后的左括号递归那层）并进入右括号判断
            if left < n:
                _res.append('(')
                search(_res, left+1, right)
                _res.pop()
            # 关键其二，一定在右括号数量少于左括号的时候才添加
            if right < left:
                _res.append(')')
                search(_res, left, right+1)
                _res.pop()
        #起始的搜索条件，搜索状态空，左右括号为0
        search([], 0, 0)
        return res
```

十分讨厌的，并不擅长的，关于字符串排列的题，还是括号这种需要匹配机制的题；不在状态的时候很难思考出一个好方法，看看题解发现这题一年前做过一遍，而且看题解理解起来比自己纯想容易的多。看到所有排列想到回溯，但是如何添加括号是个问题。和平常的回溯不大一样，有两处搜索，左括号添加与弹出，右括号添加与弹出，保证正确性的做法是控制数量和保证左右括号的顺序性（先左后右）。总而言之，需要再多做做回溯题保证思考清晰。

---

## [816. 模糊坐标](https://leetcode.cn/problems/ambiguous-coordinates/)

我们有一些二维坐标，如 `"(1, 3)"` 或 `"(2, 0.5)"`，然后我们移除所有逗号，小数点和空格，得到一个字符串`S`。返回所有可能的原始字符串到一个列表中。

```python
import itertools as it
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        res = []
        # 一个生成函数，用来生成所有可能的小数或整数组合
        def generate(_s):
            _res = []
            
            # 不添加小数点，那么这个数不含先导0或者本身就为0
            if _s[0] != '0' or _s == '0':
                _res.append(_s)
             
            # 从1开始分割整数与小数，第一次分界，左侧只有_s[0]一位为整数部分
            # 最后一次分界i=len(_s)-1，右侧只有_s[-1]一位为小数部分
            for i in range(1, len(_s)):
                # 一旦整数部分含先导0或小数部分含后置0（包括.0）就跳过，唯一的特殊情况是整数部分为0，即i=1且_s[0]=‘0’
                if i != 1 and _s[0] == '0' or _s[-1] == '0':
                    continue
                _res.append(_s[:i] + '.' + _s[i:])
            return _res
        
        # 处理字符串消除括号
        s = s[1:-1]
        l = len(s)
        
        # 主循环，仿照生成函数的分割方式，从1开始
        for i in range(1, l):
            # 生成x坐标的所有可能组合
            x = generate(s[:i])
            # 一旦没有正确的x，跳过该循环
            if x == []:
                continue
            # 生成y坐标的所有可能组合
            y = generate(s[i:])
            # 一旦没有正确的y，跳过该循环（即使x生成成功）
            if y == []:
                continue
            # x，y均成功的时候，使用itertools.product()方法产生笛卡尔积来添加元素
            for j,k in it.product(x,y):
                res.append('('+j+', '+k+')')
        return res
```

又是讨厌的题目，分类讨论是非常难受的，尤其是在笔试的时候（这题最近笔试做过，忘记自己做得怎么样了）查找错误非常痛苦。查看了题解之后有了更好的认知，主要思路是先插入 `,` ，再插入 `.` 。而排除失败答案的方法：

1. 分离x，y坐标，双方都成功生成时才添加进结果集；
2. 每个坐标先判断能否不添加小数部分，这要求不含先导 `0`；再判断加入小数点后，整数部分是否不含有先导 `0`，小数部分是否不含有后置  `0`；两种特殊情况都是整数部分就是 `0`；

另外，循环的索引设置从1开始非常合理，以及 `itertools.product()` 方法节省了写两遍循环的时间。总而言之，好好理清思路这题就非常简单了。

---

## [764. 最大加号标志](https://leetcode.cn/problems/largest-plus-sign/)

在一个 `n x n` 的矩阵 `grid` 中，除了在数组 `mines` 中给出的元素为 `0`，其他每个元素都为 `1`。`mines[i] = [xi, yi]`表示 `grid[xi][yi] == 0`

返回  `grid` 中包含 *`1`* 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 `0`。

```Python
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 初始化，grid表示真实的矩阵
        grid = [[1]*n for _ in range(n)]
        # 未简化的三维dp
        dp = [[[1]*4 for _ in range(n)] for _ in range(n)]
        # 为了直接max求最大长度，用一维列表
        res = [0] * n * n
        # 初始化，当该位置值为0时，不可能形成加号，因此dp四个方向均为0
        for x,y in mines:
            grid[x][y] = 0
            dp[x][y][0] = 0
            dp[x][y][1] = 0
            dp[x][y][2] = 0
            dp[x][y][3] = 0
        
        # 一开始出错了，没注意dp顺序，这里必须要从上向下，从左到右更新上方向和左方向的dp
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    if i > 0 and grid[i-1][j] == 1:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    if j > 0 and grid[i][j-1] == 1:
                        dp[i][j][2] = dp[i][j-1][2] + 1
		# 同理，反向再更新一遍下方向和右方向的dp，区别在于求了每个位置最小的加号臂长（最大的加号阶）
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 0:
                    if i < n-1 and grid[i+1][j] == 1:
                        dp[i][j][1] = dp[i+1][j][1] + 1
                    if j < n-1 and grid[i][j+1] == 1:
                        dp[i][j][3] = dp[i][j+1][3] + 1
                    res[i*n+j] = min(dp[i][j])
		
        # 求出整个矩阵中最大的阶
        return max(res)
```

很恶心的题，我很讨厌，原因是不想写这种四个方向找值的题，涉及边界（i，j取值范围）的题我也不是很喜欢。

用dp的原因是每个格子都会影响相邻的格子，上述方法是最麻烦（垃圾）的方法，需要三维的dp，其中第三维用来存放四个方向不同的值，每个位置不同方向的值仅仅朝一个方向相关（比如在2,3位置向左延伸，那么这个格子会与2,2位置的左方向dp挂钩，根据自身是否为0，维持不变或+1）。另外，求二维矩阵的max值可以max(map(max, res))来求，单一的max会找出第一个值最大的那一行，当然也可以展平。这道题题解大部分都简化了第三维，因为上述的特殊性，但是我很笨想不清楚，就这样吧，神志不清了。

---

## [856. 括号的分数](https://leetcode.cn/problems/score-of-parentheses/)

给定一个平衡括号字符串 `S`，按下述规则计算该字符串的分数：

- `()` 得 1 分。
- `AB` 得 `A + B` 分，其中 A 和 B 是平衡括号字符串。
- `(A)` 得 `2 * A` 分，其中 A 是平衡括号字符串。

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # 给予初始stack内值为0，代表空串
        stack = [0]
        # 栈方法，左括号添加0，代表该括号右侧的字符串值，初始化为0
        for each in s:
            if each == '(':
                stack.append(0)
            # 如果为右括号，那么计算该括号左侧的字符串值
            else:
                # 取出目前计算的该括号左侧的字符串值，如果为0，则证明左侧正好是左括号，中间为空串；如果不为0，说明已经被计算过，需要将值*2；最后计算好的值加到栈顶的值上（上一层括号的值）
                in_value = stack.pop()
                stack[-1] += max(1, 2*in_value)
        # 返回栈顶的值，但最后一定只会剩下一个值
        return stack[0]  
```

自己能想到使用栈，类似于做一个简易计算器的方法，但是失败了；

1. 根本想不到每个字符串都可以由空串拼接而成，只要空串值为0，相邻的平衡括号字符串只会相加不影响结果，顺着这个思路可能可以想到在最左侧（栈底）添加一个0；不添加0，最后一步stack会弹出所有元素。
2. else内的操作也很讲究，首先弹出配对的左括号到该右括号区间的值，括号就是这样，永远都配对。如果不为空串说明中间已经计算过了空串的值了，`()` 这种空串情况一定存在并被计算了；乘2之后加到左侧栈顶，很巧妙，因为有0这个值的存在，所以如果是外层括号内部的最左侧括号，那么左侧栈顶这个值会为0，之后结果会不断累加；按照这个逻辑，直到最后所有括号被计算，这个值会和最开始赋值的栈底值0相加求和，得出最后的结果。

---

## [1684. 统计一致字符串的数目](https://leetcode.cn/problems/count-the-number-of-consistent-strings/)

给你一个由不同字符组成的字符串 `allowed` 和一个字符串数组 `words` 。如果一个字符串的每一个字符都在 `allowed` 中，就称这个字符串是 **一致字符串**。请你返回 `words` 数组中 **一致字符串** 的数目。

```python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            for c in word:
                if c not in allowed: 
                    break
            else:
                res += 1
        return res
```

没什么注释，简单题，但是看到题解有人提到了 `for...else` 语法，所以记录一下。

---

## [1620. 网络信号最好的坐标](https://leetcode.cn/problems/coordinate-with-maximum-network-quality/)

给你一个数组 `towers` 和一个整数 `radius` 。

数组 `towers` 中包含一些网络信号塔，其中 `towers[i] = [xi, yi, qi]` 表示第 `i` 个网络信号塔的坐标是 `(xi, yi)` 且信号强度参数为 `qi` 。所有坐标都是在 X-Y 坐标系内的 **整数** 坐标。两个坐标之间的距离用 **欧几里得距离** 计算。

整数 `radius` 表示一个塔 **能到达** 的 **最远距离** 。如果一个坐标跟塔的距离在 `radius` 以内，那么该塔的信号可以到达该坐标。在这个范围以外信号会很微弱，所以 `radius` 以外的距离该塔是 **不能到达的** 。

如果第 `i` 个塔能到达 `(x, y)` ，那么该塔在此处的信号为 `⌊qi / (1 + d)⌋` ，其中 `d` 是塔跟此坐标的距离。一个坐标的 **信号强度** 是所有 **能到达** 该坐标的塔的信号强度之和。

请你返回数组 `[cx, cy]` ，表示 **信号强度** 最大的 **整数** 坐标点 `(cx, cy)` 。如果有多个坐标网络信号一样大，请你返回字典序最小的 **非负** 坐标。

```python
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # 求最大范围，题目中指出所有坐标都在0到50的范围内，所以也可以不求
        max_x = max([tower[0] for tower in towers])
        max_y = max([tower[1] for tower in towers])
        res = []
        strength = -1
		
        # 题目要求字典序最小的非负坐标，因此从左至右从下至上搜索
        for i in range(max_x+1):
            for j in range(max_y+1):
                # 强度总和初始化
                _strength = 0
                for x,y,q in towers:
                    distance = math.sqrt(abs(i-x)**2 + abs(j-y)**2)
                    # 注意信号范围超过了就忽略该信号
                    if distance <= radius:
                        _strength += math.floor(q / (1+distance))
                if _strength > strength:
                    res = [i, j]
                    strength = _strength
        
        return res
```

注意概念**欧几里得距离**指最普通的距离，还有其他的距离例如**曼哈顿距离**是直接求坐标差绝对值之和等等；另外，可以证明不需要搜索类似于max_x+radius这种搜索范围，因为总能找到一个字典序更小的坐标，这个坐标的强度大于或等于范围外的这些点；此外还要注意求最大值的这个列表的使用，别忘记了。

---

## [790. 多米诺和托米诺平铺](https://leetcode.cn/problems/domino-and-tromino-tiling/)

有两种形状的瓷砖：一种是 `2 x 1` 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

![img](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

给定整数 n ，返回可以平铺 `2 x n` 的面板的方法的数量。**返回对** `109 + 7` **取模** 的值。

平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。

```python
class Solution:
    def numTilings(self, n: int) -> int:
        # 初始化dp列表，第二个维度代表第i列的瓷砖分布情况，0全空，1上方有瓷砖，2下方有瓷砖，3瓷砖铺满第i列，这些状态分别从前一列（i-1）列的不同状态转移
        dp = [[0]*4 for i in range(n)]
        # 只有全空和全铺满的情况会出现在第一列
        dp[0][3] = 1
        dp[0][0] = 1
        # 状态转移，看解析比较好
        for i in range(1, n):
            dp[i][0] = dp[i-1][3]
            dp[i][1] = dp[i-1][2] + dp[i-1][0]
            dp[i][2] = dp[i-1][1] + dp[i-1][0]
            dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
        # 返回最后一列铺满时的总数，并且注意取模
        return dp[-1][3] % (10**9+7)
```

根本看不懂题目描述的最后一句，但是这是一道非常经典的题（听别人说的）。解法还能用其他找规律的思路，或者矩阵快速幂，这个改天脑子比较清楚的时候再看。动态规划的话，可以参考下面这个图：

![img](https://assets.leetcode-cn.com/solution-static/790/1.png)

偷的图，总而言之转移方式就这样，唯一令我不解的是最后一种 `dp[i-1][0] -> dp[i][3] ` 还有一种重复的，就是两个多米诺竖着插入，但是这个状态和最后一种是重复的，所以被忽略了？如果之后再出现这种状态重复的情况再来看吧。最后，有意思的是这些形状还有其他版本的，比如四格骨牌：[Tetromino](https://en.wikipedia.org/wiki/Tetromino)，很神秘的俄罗斯方块形状。

---

## [791. 自定义字符串排序](https://leetcode.cn/problems/custom-sort-string/)

给定两个字符串 `order` 和 `s` 。`order` 的所有单词都是 **唯一** 的，并且以前按照一些自定义的顺序排序。

对 `s` 的字符进行置换，使其与排序的 `order` 相匹配。更具体地说，如果在 `order` 中的字符 `x` 出现字符 `y` 之前，那么在排列后的字符串中， `x` 也应该出现在 `y` 之前。

返回 *满足这个性质的 `s` 的任意排列* 。

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 对字符串计数
        counter = collections.Counter(s)
        res = []
        # 按顺序检查字符串s是否含有顺序的字符，如果有直接插入相应个数的字符串
        for c in order:
            if c in counter.keys():
                res.append(c * counter[c])
                counter[c] = 0
		# 检查剩下的不需要顺序的字符串，并插入
        for key, count in counter.items():
            if count != 0:
                res.append(key * count)
        return ''.join(res)
```

虽然是自己写的方法，但是思路是**计数排序**法，我并没有注意到这点。另外，Python需要掌握的是 `sorted()` 的使用方法，因此再给出另一种直接排序的解法：

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 字典，默认值为0
        d = collections.defaultdict(int)
        # 按权重从小到大排序，注意i需要从1开始，因为不排序的字符权重默认为0
        for i, c in enumerate(order):
            d[c] = i + 1
        # 排序，需要注意的是这里的排序，所有不在排序规则内的字符会在结果字符串前面
        return ''.join(sorted(s, key=lambda x: d[x]))
```

---

## [416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 排序，做特殊判断的初始化
        nums.sort()
        n = len(nums)
        _sum = sum(nums)
        target = _sum // 2
		# 如果和为奇数，证明不能等分
        if target * 2 != _sum: return False
		# 设置背包dp，row表示数字的选取与否，col表示选取值的和
        dp = [[False] * (target+1) for _ in range(n)]
		# 初始化，每个数字不选的时候，和为0都成立
        for i in range(n):
            dp[i][0] = True
		# dp填充过程，从下至上，从左至右
        for i in range(1, n):
            for j in range(1, target+1):
                # dp转移方程
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # 返回选择在可选所有物品条件下和为target值的真假
        return dp[-1][-1]
```

这道题需要把原有问题转化为一个0-1背包问题，只要选取部分数字达到全部数字和的一半，那么剩下一半数字必定能分成相同和的一组；dp内的值为布尔值，用来直接判断在选取数字 `num[:i+1]`的情况下是否能组成一个和 `j` ，转移方程的含义如下：

1. 如果当前数字小于（或等于）目标和 `j`，这里我可以选择是否添加该数字 `i`，这个选择取决于上一层状态，我是否能组成和 `j-i`，如果可以，那么此时从之前状态选择 `i` 组成目标和 `j` 转移到当前状态，` dp[i][j]` 为真。另一种情况下，是当前和与目标和相同，已经为 `j`，那么此时不选则数字也可以设置当前 ` dp[i][j]` 为真；
2. 如果当前数字大于目标和 `j` ，那么该数字不可选，只能看上一层状态的和是否可以为 `j` ；

---

## [474. 一和零](https://leetcode.cn/problems/ones-and-zeroes/)

给你一个二进制字符串数组 `strs` 和两个整数 `m` 和 `n` 。

请你找出并返回 `strs` 的最大子集的长度，该子集中 **最多** 有 `m` 个 `0` 和 `n` 个 `1`。

如果 `x` 的所有元素也是 `y` 的元素，集合 `x` 是集合 `y` 的 **子集** 。

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 定义三维dp列表dp[i]表示选取前0个0-1字符串的最大子集长度
        l = len(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(l+1)]
		# 从第二行i=1开始，表示选择第一个0-1字符串
        for i in range(1, l+1):
            # 求0,1的个数
            c0 = strs[i-1].count('0')
            c1 = strs[i-1].count('1')
            # 注意这里必须从0开始，因为对0,1的计量是组合形式的，和二维不同
            for j in range(m+1):
                for k in range(n+1):
                    # 如果不能添加字符串（这里也是组合形式，0,1都必须在j,k范围内）
                    if j < c0 or k < c1:
                        dp[i][j][k] = dp[i-1][j][k]
                    # 可以添加字符串，就看添加过后长度大一些还是不添加时大一些
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-c0][k-c1] + 1)

        return dp[-1][-1][-1]
```

总而言之，是0-1背包的三维形式，`dp[i][j][k]` 代表了选择前i个字符串的情况下，`0，1`个数分别为 `j，k` 时所能得到的最大子集长度为多少，需要注意的两点：

1. 如果设定row（物品数，在这里是字符串数组的长度）+1，那么可以正常遍历，如果不设置+1，需要手动初始化第一行（第一个字符串的情况），dp的初始化看个人喜好吧；
2. 关于0,1个数的维度范围，需要从0开始，因为有的字符串可能只含0或1，而遍历时需要遍历到j=0，k=0...n或者k=0, j=0...m的情况，不从0开始会错过很多状态，这也是和二维不同的地方，需要注意；同理，**不能添加**的时候只需满足1个数太多或者0个数太多两个条件的**其中之一**；

---

## [494. 目标和](https://leetcode.cn/problems/target-sum/)

给你一个整数数组 `nums` 和一个整数 `target` 。

向数组中的每个整数前添加 `'+'` 或 `'-'` ，然后串联起所有整数，可以构造一个 **表达式** ：

- 例如，`nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。

返回可以通过上述方法构造的、运算结果等于 `target` 的不同 **表达式** 的数目。

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 特判，只有一个元素的时候，该元素必须等于-target或target
        if n == 1:
            if nums[0] == target or nums[0] == -target:
                return 1
            else:
                return 0
        
        # 找出pos的和应该为多少
        pos2 = target + sum(nums)
        pos = pos2 >> 1
        # 不能被2整除，所以无解
        if pos << 1 != pos2: return 0

        # dp初始化，和前几个背包问题一样
        dp = [[0] * (pos+1) for _ in range(n)]    
        for i in range(n):
            dp[i][0] = 1
        # 注意特例，当nums第一个元素为0的时候，需要赋值为2，因为+0-0都为0，但是其他人的解没有这项
        # 这里代码可能会有些迷惑，这里不仅设置了特殊值nums[0]为0，还初始化了第一行
        dp[0][nums[0]] = 2 if nums[0] == 0 else 1

        # 稍微有所不同，j从0开始遍历，因为物品中（数字）可能存在0
        for i in range(1, n):
            for j in range(pos+1):
                # 不能选择数字的情况
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                # 求的是不同种类的组合数，所以状态转移为加法
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]

        return dp[-1][-1]
```

直接照搬之前的解法，发现自己写的注释还是很迷惑，重新梳理了一下，首先根据公式：

$$
pos + neg = sum \\
pos = target + neg \\
pos = {{target + sum}\over 2}
$$
转化问题为一个0-1背包问题，目标就是选取一些数字，让它们的和成为 `pos` 部分，依旧包含特例，比如只有一个数字可选的情况；

初始化这里也在注释中写了，这里可能会有疑问，为什么 `dp[i][j]` 中的j一定是非负的，target可能是负的啊？因为abs(target)肯定小于sum，不然公式不成立，而sum一定是非负数，因此dp是正确的。初始化第一行的时候考虑第一个数字为0的情况，因此对应的和位置需要初始化为2，其他数字为1。当然根据之前的dp理论，可以选择不同的初始化方法，比如让row+1。又因为该背包物品重量可能为0，因此不能简单的不考虑 `j=0`的情况。

---

## [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/)

有一堆石头，用整数数组 `stones` 表示。其中 `stones[i]` 表示第 `i` 块石头的重量。

每一回合，从中选出**任意两块石头**，然后将它们一起粉碎。假设石头的重量分别为 `x` 和 `y`，且 `x <= y`。那么粉碎的可能结果如下：

- 如果 `x == y`，那么两块石头都会被完全粉碎；
- 如果 `x != y`，那么重量为 `x` 的石头将会完全粉碎，而重量为 `y` 的石头新重量为 `y-x`。

最后，**最多只会剩下一块** 石头。返回此石头 **最小的可能重量** 。如果没有石头剩下，就返回 `0`。

```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = sum(stones)
        n = len(stones)
        # 特殊值的判断，仅有一颗石头，就返回石头重量
        if n == 1: return stones[0]
    	# 也可以写成 target = _sum // 2, 总之，接近均值即可
        target = ceil(_sum / 2)
		
        dp = [[False] * (target+1) for _ in range(n)]
		# 经典初始化，第一列都可以凑出（不选）
        for i in range(n):
            dp[i][0] = True
        # 第一行初始化，第一块石头选择的情况下凑出重量stone[0]
        dp[0][stones[0]] = True
		# 填充dp
        for i in range(1, n):
            for j in range(1, target+1):
                if stones[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i]]
        
		# 特殊的解法，找到最后一行，即所有石头均可选择的情况下，最接近均值的重量是多少（从右到左）
        for i in range(target, -1, -1):
            if dp[-1][i]:
                # 找到该重量后，进行计算
                # 如果之前的target选择的是_sum//2, 那么此处直接_sum - i*2即可
                return abs(i - (_sum-i)) 
```

和之前的思路相通，问题转化为0-1背包问题，即把石头分为两堆，使这两堆石头重量尽可能相同，区别是，这里组成的重量和不确定，可以为一半也可以不为，总之，选择的是最接近一半的重量和最为目标即可；很多题解中使用的是向下取整的target，这是经过了公式推导的。但这里其实也能使用直接的逻辑选择向上取整，只不过最后求值的时候需要做一些处理；同理初始化也可以根据自己喜好选择不同的初始化方式。
