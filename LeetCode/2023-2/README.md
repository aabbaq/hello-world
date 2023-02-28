## [283. 移动零](https://leetcode.cn/problems/move-zeroes/)

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int p = 0, q = 0;
        int tmp = -1;
        int l = nums.length;
        while (q < l) {
            if (nums[q] != 0) {
                tmp = nums[p];
                nums[p] = nums[q];
                nums[q] = tmp;
                p += 1;
            }
            q += 1;
        }
    }
}
```

- 右指针的移动在操作之后移动，为了不错过第一个值；
- 右指针寻找非0元素，将其放置在左侧，具体实现是和左指针交换值，之后左指针右移1位，左指针左侧元素已经符合要求；
- 右指针每个循环都移动一次；

---

## [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

```java
class Solution {
    public int[] exchange(int[] nums) {
        int l = nums.length;
        int p = 0, q = 0;
        int tmp = -1;
        while (q < l) {
            if (nums[q] % 2 == 1) {
                tmp = nums[p];
                nums[p] = nums[q];
                nums[q] = tmp;
                p += 1;
            }
            q += 1;
        }
        return nums;
    }
}
```

一样的题，增加熟练度；

---

## [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

给你一个 **升序排列** 的数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致**。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 `k` 个元素，那么 `nums` 的前 `k` 个元素应该保存最终结果。

将最终结果插入 `nums` 的前 `k` 个位置后返回 `k` 。

不要使用额外的空间，你必须在 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int p = 0, q = 0;
        int l = nums.length;
        while (q < l) {
            if (nums[p] < nums[q]) {
                p += 1;
                nums[p] = nums[q];
            }
            q += 1;
        }
        return p + 1;
    }
}
```

可以使用前两题的双指针做，但是会引入一个Set，额外空间，并且没有利用到升序数组的特征；因此设定左指针一直指向排好序的数组最右端，并不断比较右指针与其的大小，若出现了不一致（右指针指向的元素较大），那么就移动左指针并将右指针指向的元素赋予左指针指向的位置，原因是左指针右侧的所有元素都没有什么用；

---

## [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)

给你一个有序数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使得出现次数超过两次的元素**只出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **[原地 ](https://baike.baidu.com/item/原地算法)修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int l = nums.length;
        if (l < 3) {
            return l;
        }
        int p = 1, q = 2;
        while (q < l) {
            if (nums[p] == nums[q] && nums[p-1] == nums[q]) {
                q += 1;
            } else {
                p += 1;
                nums[p] = nums[q];
                q += 1;
            }
        }
        return p+1;
    }
}
```

很直白的想法，首先p指针代表着当前已经完成好排列的末尾索引，而q代表着当前的检查索引；比较两处索引位置的值，以及p-1位置的值，如果相同那么q指针指向的位置的数需要略过，否则，就将这个数放在p的下一个位置，同时p也向右移动一位；此外，p=1，q=2的设置是因为前两位（0,1）是必定符合题目规定的；

实际上可以简化成 `nums[p-1] == nums[q]` 一个条件即可，因为如果此处相等，那么 `nums[p] == nums[q]` 必定相等，因为是升序数组，中间的值也都是一样的，官方题解中的左指针并不是p末尾索引，而是末尾索引+1的位置，需要注意；

最令人震惊的是一年前写的Python代码：

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p = 1
        q = 2
        l = len(nums)
        while q < l:
            if nums[q] == nums[p] and nums[q] == nums[p-1]:
                q += 1
            else:
                p += 1
                nums[p] = nums[q]
                q += 1
        return p + 1
```

思路一模一样... 毫无成长，不过Python代码中有个bug，长度为1的数组会返回2；

---

## [165. 比较版本号](https://leetcode.cn/problems/compare-version-numbers/)

给你两个版本号 `version1` 和 `version2` ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 `'.'` 连接。每个修订号由 **多位数字** 组成，可能包含 **前导零** 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 。下一个修订号下标为 1 ，以此类推。例如，`2.5.33` 和 `0.1` 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 **忽略任何前导零后的整数值**。也就是说，修订号 `1` 和修订号 `001` **相等**。如果版本号没有指定某个下标处的修订号，则该修订号视为 `0`。例如，版本 `1.0` 小于版本 `1.1` ，因为它们下标为 `0` 的修订号相同，而下标为 `1` 的修订号分别为 `0` 和 `1` ，`0 < 1`。

返回规则如下：

- 如果 `*version1* > *version2*` 返回 `1`，
- 如果 `*version1* < *version2*` 返回 `-1`，
- 除此之外返回 `0`。

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        int l1 = version1.length();
        int l2 = version2.length();
        int p = 0, q = 0;

        while (p < l1 || q <l2) {
            int x = 0;
            for (; p < l1 && version1.charAt(p) != '.'; p++) {
                x += x*10 + version1.charAt(p) - '0';
            }
            p += 1;
            int y = 0;
            for (; q < l2 && version2.charAt(q) != '.'; q++) {
                y += y*10 + version2.charAt(q) - '0';
            }
            q += 1;
            if (x != y) {
                return x > y ? 1 : -1;
            }
        }
        return 0;
    }
}
```

标准的双指针解法，其中需要注意的点为：

- `while` 循环条件为 `||` ，这是为了比较长度，如果其中一方指针已经指向终点，那么它的内层 `for` 循环会终止，他所计算出的修订号也会为初始值0，这样最后就会得出该版本号小于另一个版本号的结论；
- `for` 循环的终止条件，第一个是指针到达末尾，第二个是遇到 `.` 间隔，在处理间隔条件完成后，需要在外侧将指针值+1，移动指针至下一个修订号；
- 算修订号可以直接利用类似十进制的累加进行计算 ( `x += x*10 + y` )，这样前导0会被自然消除；

---

# 搜索（BFS & DFS）简单练习



## [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：**叶子节点是指没有子节点的节点。

```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) {
            return 1;
        }
        int min = Integer.MAX_VALUE;
        if (root.left != null) {
            min = Math.min(minDepth(root.left), min);
        }
        if (root.right != null) {
            min = Math.min(minDepth(root.right), min);
        }
        return min + 1;
    }
    
    public int minDepth2(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        int depth = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i=0; i<size; i++) {
                TreeNode node = queue.poll();
                if (node.left == null && node.right == null) return depth+1;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            depth++;
        }
        return depth;
    }

}
```

DFS方法慢一些，需要递归调用方法；而且感觉上DFS中间不好构造，很诡异，每一层都需要设置一个最大值去寻找最小值；DFS终止条件是两个，第一个是根节点为null的情况，这个是特殊情况，因为之后的递归都不会传入null的root节点了，第二个为出现叶子结点，这个时候需要返回1，题目问的是这条路径上的节点数量，因此递归到叶子结点时返回自身的数量。

BFS方法比较巧妙，特殊一些的是一层一层的遍历，以此来累加depth。此外，不用担心错过最小值，因为多个最小深度也必定出现在同一层，可以直接提前返回；

---

## [1469. 寻找所有的独生节点](https://leetcode.cn/problems/find-all-the-lonely-nodes/)

二叉树中，如果一个节点是其父节点的唯一子节点，则称这样的节点为 “**独生节点**” 。二叉树的根节点不会是独生节点，因为它没有父节点。

给定一棵二叉树的根节点 `root` ，返回树中 **所有的独生节点的值所构成的数组** 。数组的顺序 **不限** 。

```java
class Solution {
    public List<Integer> getLonelyNodes(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        dfs(root, res);
        return res;
    }

    public void dfs(TreeNode root, List<Integer> list) {
        if (root.left != null) {
            if (root.right == null) list.add(root.left.val);
            dfs(root.left, list);
        }
        if (root.right != null) {
            if (root.left == null) list.add(root.right.val);
            dfs(root.right, list);
        }
    }
    
    
    public List<Integer> getLonelyNodes2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.left != null) {
                if (node.right == null) res.add(node.left.val);
                queue.offer(node.left);
            }
            if (node.right != null) {
                if (node.left == null) res.add(node.right.val);
                queue.offer(node.right);
            }
        }
        return res;
    }
}
```

这一题BFS比DFS慢一些，可能是因为设计到两个集合的操作，效率不是很高；不过原理比较容易，搜索的时候先判断是否为非空，再判断另一个节点是否为空即可；

---

## [1379. 找出克隆二叉树中的相同节点](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

给你两棵二叉树，原始树 `original` 和克隆树 `cloned`，以及一个位于原始树 `original` 中的目标节点 `target`。

其中，克隆树 `cloned` 是原始树 `original` 的一个 **副本**。

请找出在树 `cloned` 中，与 `target` **相同** 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。

```java
class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        if (target == null) return null;
        return dfs(original, cloned, target);
    }

    public TreeNode dfs(TreeNode oRoot, TreeNode cRoot, TreeNode target) {
        if (oRoot == target) return cRoot;
        TreeNode res = null;

        if (oRoot.left != null) res = dfs(oRoot.left, cRoot.left, target);
        if (res != null) return res;

        if (oRoot.right != null)  res=  dfs(oRoot.right, cRoot.right, target);
        return res;
    }
}
```

感觉上写法很丑陋，但是思路是清晰地，同步遍历即可；另外题目提示说两棵树没用重复值，那就很没意思了；

---

## [993. 二叉树的堂兄弟节点](https://leetcode.cn/problems/cousins-in-binary-tree/)

在二叉树中，根节点位于深度 `0` 处，每个深度为 `k` 的节点的子节点位于深度 `k+1` 处。

如果二叉树的两个节点深度相同，但 **父节点不同** ，则它们是一对*堂兄弟节点*。

我们给出了具有唯一值的二叉树的根节点 `root` ，以及树中两个不同节点的值 `x` 和 `y` 。

只有与值 `x` 和 `y` 对应的节点是堂兄弟节点时，才返回 `true` 。否则，返回 `false`。

```java
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<TreeNode> fathers = new LinkedList<>();
        queue.offer(root);
        fathers.offer(root);
        int depth = 0;

        int[] xInfo = new int[2];
        int[] yInfo = new int[2];

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i=0; i<size; i++) {
                TreeNode node = queue.poll();
                TreeNode father = fathers.poll();
                if (node.val == x) {
                    xInfo[0] = depth;
                    xInfo[1] = father.val;
                } else if (node.val == y) {
                    yInfo[0] = depth;
                    yInfo[1] = father.val;
                }
                if (node.left != null) {
                    queue.offer(node.left);
                    fathers.offer(node);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                    fathers.offer(node);
                }
            }
            depth += 1;
        }

        return (xInfo[0] == yInfo[0] && xInfo[1] != yInfo[1]) ? true : false;
    }
}
```

很死板的方法，这道题比上面几题复杂，思路是查询两个节点的父节点信息以及层数信息，即可确定他们是否为堂兄弟节点；只不过我想练习BFS，和Python不同的是，Java需要构建一个类才可以使用一个队列完成操作，也许会有更好的方法，但目前我并不清楚，总之按照层序遍历完成后得到两个节点信息，比较即可；其中不足之处是刚才提到过的两个队列问题，第二点是找到两个节点后可以直接退出的优化问题；

---

## [965. 单值二叉树](https://leetcode.cn/problems/univalued-binary-tree/)

如果二叉树每个节点都具有相同的值，那么该二叉树就是*单值*二叉树。

只有给定的树是单值二叉树时，才返回 `true`；否则返回 `false`。

```java
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        int value = root.val;
        return dfs(root, value);
    }

    public boolean dfs(TreeNode root, int value) {
        if (root.val != value) return false;
        boolean res1 = true;
        boolean res2 = true;
        if (root.left != null) {
            res1 = dfs(root.left, value);
        }
        if (root.right != null) {
            res2 = dfs(root.right, value);
        }
        return res1 && res2;
    }
    
    public boolean dfs2(TreeNode root, int value) {
        if (root.val != value) return false;
        if (root.left != null && !dfs(root.left, value)) {
            return false;
        }
        if (root.right != null && !dfs(root.right, value)) {
            return false;
        }
        return true;
    }
}
```

一个简单题提交了三次才过😅，递归的时候需要得到左右子树是否为单值的结果。

---

## [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值**。

差值是一个正数，其数值等于两值之差的绝对值。

```java
class Solution {
    public int getMinimumDifference(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        dfs(root, list);
        for (int i=1; i<list.size(); i++) {
            min = Math.min(Math.abs(list.get(i)-list.get(i-1)), min);
        }
        return min;
    }

    public void dfs(TreeNode root, List<Integer> list) {
        if (root.left != null) {
            dfs(root.left, list);
        }
        list.add(root.val);
        if (root.right != null) {
            dfs(root.right, list);
        }
    }
}
```

中序遍历得到结果后再对每一个两个值进行求最小值，明显复杂了；另一种做法是在遍历的时候就进行运算，明天再写；

---

## [559. N 叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/)

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

```java
class Solution {
    public int maxDepth(Node root) {
        if (root == null) return 0;
        Queue<Node> queue = new LinkedList<>();
        int depth = 0;
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i=0; i<size; i++) {
                Node node = queue.poll();
                for (Node subNode : node.children) {
                    queue.offer(subNode);
                }
            }
            depth++;
        }
        return depth;
    }
}
```

BFS，逐层增加深度

---

## [637. 二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10-5` 以内的答案可以被接受。

```java
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> avgs = new ArrayList<>();
        if (root == null) return avgs;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            double sum = 0;
            for (int i=0; i<size; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            avgs.add(sum / size);
        }
        return avgs;
    }
}
```

继续练习，顺便复习Java数字；

---

## [653. 两数之和 IV - 输入二叉搜索树](https://leetcode.cn/problems/two-sum-iv-input-is-a-bst/)

给定一个二叉搜索树 `root` 和一个目标结果 `k`，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 `true`。

```java
class Solution {
    public HashSet<Integer> set = new HashSet<>();

    public boolean findTarget(TreeNode root, int k) {
        if (root == null) return false;
        if (set.contains(k-root.val)) {
            return true;
        }
        else {
            set.add(root.val);
            return findTarget(root.left, k) || findTarget(root.right, k);
        }
    }
}
```

没想到，最初的直直思路是进行中序遍历之后用双指针，但很明显可以在遍历的时候就进行双指针模拟，还是不好想；最后还是用哈希表进行遍历算了；

---

## [LCP 44. 开幕式焰火](https://leetcode.cn/problems/sZ59z6/)

「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。

给定一棵二叉树 `root` 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。

```java
class Solution {
    public HashSet<Integer> set = new HashSet<>();

    public int numColor(TreeNode root) {
        dfs(root);
        return set.size();
    }

    public void dfs(TreeNode root) {
        if (root == null) return;
        set.add(root.val);
        dfs(root.left);
        dfs(root.right);
    }
}
```

和上题类似，用哈希表解决，简单；

---

## [面试题 08.10. 颜色填充](https://leetcode.cn/problems/color-fill-lcci/)

编写函数，实现许多图片编辑软件都支持的「颜色填充」功能。

待填充的图像用二维数组 `image` 表示，元素为初始颜色值。初始坐标点的行坐标为 `sr` 列坐标为 `sc`。需要填充的新颜色为 `newColor` 。

「周围区域」是指颜色相同且在上、下、左、右四个方向上存在相连情况的若干元素。

请用新颜色填充初始坐标点的周围区域，并返回填充后的图像。

```java
class Solution {
    public int rows = 0;
    public int cols = 0;
    public int color = -1;
    public int oldColor = -1;

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        rows = image.length;
        cols = image[0].length;
        color = newColor;
        oldColor = image[sr][sc];
        if (oldColor == color) return image;
        dfs(image, sr, sc);
        return image;
    }

    public void dfs(int[][] image, int x, int y) {
        if (image[x][y] != oldColor) return;
        else {
            image[x][y] = color;
            if (x+1 < rows) dfs(image, x+1, y);
            if (x-1 > -1) dfs(image, x-1, y);
            if (y+1 < cols) dfs(image, x, y+1);
            if (y-1 >-1) dfs(image, x, y-1);
        }
    }
}
```

唯一需要注意的是首先判断开始染色的方块是否已经达成目标，不然会造成死循环；

# 搜索（BFS & DFS）中等练习

## [934. 最短的桥](https://leetcode.cn/problems/shortest-bridge/)

给你一个大小为 `n x n` 的二元矩阵 `grid` ，其中 `1` 表示陆地，`0` 表示水域。

**岛** 是由四面相连的 `1` 形成的一个最大组，即不会与非组内的任何其他 `1` 相连。`grid` 中 **恰好存在两座岛** 。

你可以将任意数量的 `0` 变为 `1` ，以使两座岛连接起来，变成 **一座岛**。

返回必须翻转的 `0` 的最小数目。

```java
class Solution {
    public int rows = 0;
    public int cols = 0;
    public int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public Queue<int[]> island = new ArrayDeque<>();

    public int shortestBridge(int[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (grid[i][j] == 1){
                    grid[i][j] = -1;
                    dfs(i, j, grid);
                    return bfs(grid);
                }
            }
        }
        return -1;
    }

    public void dfs(int x, int y, int[][] grid) {
        island.add(new int[] {x, y});
        for (int i=0; i<4; i++) {
            int nx = x + dirs[i][0];
            int ny = y + dirs[i][1];
            if (nx > -1 && nx < rows && ny >-1 && ny < cols && grid[nx][ny] == 1) {
                grid[nx][ny] = -1;
                dfs(nx, ny, grid);
            }
        }
    }

    public int bfs(int[][] grid) {
        int bridge = 0;
        while (!island.isEmpty()) {
            int size = island.size();
            for (int i=0; i<size; i++) {
                int[] block = island.poll();
                for (int j=0; j<4; j++) {
                    int nx = block[0] + dirs[j][0];
                    int ny = block[1] + dirs[j][1];
                    if (nx > -1 && nx < rows && ny > -1 && ny < cols) {
                        if (grid[nx][ny] == 1) return bridge;
                        else if (grid[nx][ny] == 0) {
                            island.offer(new int[] {nx, ny});
                            grid[nx][ny] = -1;
                        }
                    }
                }           
            }
            bridge++;
        }
        return -1;
    }
}
```

对于我来说，没有思路，但是得到解决方法之后变得非常简单，首先使用dfs或者bfs寻找其中一个岛屿的所有方格，将其放入队列中存储，标记已访问的方格；之后使用bfs逐层寻找，直到搜索到另一个岛屿停止；

---

## [542. 01 矩阵](https://leetcode.cn/problems/01-matrix/)

给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1`。

```java
class Solution {
    public Queue<int[]> queue = new ArrayDeque<>();
    public int rows = 0;
    public int cols = 0;
    public int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int[][] updateMatrix(int[][] mat) {
        rows = mat.length;
        cols = mat[0].length;
        boolean[][] visited = new boolean[rows][cols]; 
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (mat[i][j] == 0) {
                    queue.offer(new int[] {i, j});
                    visited[i][j] = true;
                }
            }
        }
        int step = 1;   
        while (!queue.isEmpty()) {
            int sz = queue.size();
            for (int i=0; i<sz; i++) {
                int[] block = queue.poll();
                for (int[] dir : dirs) {
                    int x = block[0] + dir[0];
                    int y = block[1] + dir[1];
                    if (x < rows && x > -1 && y < cols && y > -1 && !visited[x][y]) {
                        mat[x][y] = step;
                        visited[x][y] = true;
                        queue.offer(new int[] {x, y});
                    }
                }
            }
            step++;
        }
        return mat;
    }
}
```

思路和上题一模一样，但是方法略有不同，首先不需要进行第一次的搜索算法，直接遍历出所有的0方格加入队列即可；之后使用bfs为每一个1位置赋予距离，开始的时候我尝试不使用visited记录搜索过的节点，等于1就加入队列，后来才注意到本来就会有距离为1的方格，这些方格在后续会被继续计算，因此不可行；

---

## [剑指 Offer II 105. 岛屿的最大面积](https://leetcode.cn/problems/ZL6zAn/)

给定一个由 `0` 和 `1` 组成的非空二维数组 `grid` ，用来表示海洋岛屿地图。

一个 **岛屿** 是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在水平或者竖直方向上相邻。你可以假设 `grid` 的四个边缘都被 `0`（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 `0`。

```java
class Solution {
    public int rows = 0;
    public int cols = 0;
    public int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        rows = grid.length;
        cols = grid[0].length;
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = -1;
                    res = Math.max(dfs(i, j, grid), res);
                }
            }
        }
        return res;
    }

    public int dfs(int x, int y, int[][] grid) {
        int curSize = 1;
        for (var dir : dirs) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx < rows && nx > -1 && ny < cols && ny > -1 && grid[nx][ny] == 1) {
                grid[nx][ny] = -1;
                curSize += dfs(nx, ny, grid);
            }
        }
        return curSize;
    }
}
```

用dfs对每一个岛屿搜索，记录其面积，并且将搜索位置标记避免重复；注意dfs算面积的结束条件就是自身面积1的情况，跳过if从而返回自己；

---

## [314. 二叉树的垂直遍历](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/)

给你一个二叉树的根结点，返回其结点按 **垂直方向**（从上到下，逐列）遍历的结果。如果两个结点在同一行和列，那么顺序则为 **从左到右**。

```java
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        
        if (root == null) return res;
        int minPos = 0;

        Queue<TreeNode> queue = new ArrayDeque<>();
        Queue<Integer> idxs = new ArrayDeque<>();
        queue.offer(root);
        idxs.offer(0);


        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int idx = idxs.poll();
            List<Integer> list = map.getOrDefault(idx, new ArrayList<Integer>());
            list.add(node.val);
            map.put(idx, list);
            if (node.left != null) {
                queue.offer(node.left);
                idxs.offer(idx-1);
                minPos = Math.min(idx-1, minPos);
            }
            if (node.right != null) {
                queue.offer(node.right);
                idxs.offer(idx+1);
            }
        }

        for (int i=minPos; i<minPos+map.size(); i++) {
            res.add(map.get(i));
        }
        return res;
    }
}
```

事实上还是二叉树的层序遍历，但是需要进行一些额外处理；首先令root的坐标为0，每次遍历左子树将其坐标-1，右子树则加1，以坐标升序存放进一个哈希表，以此取出即可；因此需要两个队列（类似于Python用元组放进队列）存储节点以及其坐标，取出后在哈希表中拿相应坐标的列表，添加即可；因为需要从上至下，从左到右遍历，因此用层序遍历就完成了；

---

## [417. 太平洋大西洋水流问题](https://leetcode.cn/problems/pacific-atlantic-water-flow/)

有一个 `m × n` 的矩形岛屿，与 **太平洋** 和 **大西洋** 相邻。 **“太平洋”** 处于大陆的左边界和上边界，而 **“大西洋”** 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 `m x n` 的整数矩阵 `heights` ，`heights[r][c]` 表示坐标 `(r, c)` 上单元格 **高于海平面的高度**。

岛上雨水较多，如果相邻单元格的高度 **小于或等于** 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回网格坐标 `result` 的 **2D 列表** ，其中 `result[i] = [ri, ci]` 表示雨水从单元格 `(ri, ci)` 流动 **既可流向太平洋也可流向大西洋** 。

```java
class Solution {
    public int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public int rows;
    public int cols;
    public boolean[][] pacific;
    public boolean[][] atlantic;
    public int[][] heights;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        rows = heights.length;
        cols = heights[0].length;
        pacific = new boolean[rows][cols];
        atlantic = new boolean[rows][cols];
        this.heights = heights;

        for (int i=0; i<rows; i++) {
            dfs(i, 0, pacific);
        }
        for (int j=0; j<cols; j++) {
            dfs(0, j, pacific);
        }
        for (int i=rows-1; i>-1; i--) {
            dfs(i, cols-1, atlantic);
        }
        for (int j=cols-1; j>-1; j--) {
            dfs(rows-1, j, atlantic);
        }
        
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> list = new ArrayList<>();
                    list.add(i);
                    list.add(j);
                    res.add(list);
                }
            }
        }
        return res;
    }

    public void dfs(int x, int y, boolean[][] flows) {
        if (flows[x][y]) return;
        flows[x][y] = true;
        for (var dir : dirs) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx > -1 && nx < rows && ny > -1 && ny < cols && heights[nx][ny] >= heights[x][y]) {
                dfs(nx, ny, flows);
            }
        }
    }
}
```

思路，反向搜索，标记水流可以到达的区域，对两大洋分别进行一次标记。此时标记条件为大于等于时才进行搜索；要点有两个，第一个搜索起点为太平洋上边左边，大西洋右边下边；第二个是跳过已经确定能够流过的区域，在dfs方法的第一行语句。

---

## [994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/)

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`*。

```java
class Solution {
    public int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        int total = 0;
        Queue<int[]> queue = new LinkedList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (grid[i][j] == 0) {
                    continue;
                }
                if (grid[i][j] == 2) {
                    queue.offer(new int[] {i, j});
                }
                total += 1;
            }
        }

        int steps = 0;
        int rotten = queue.size();
        if (rotten == total) return 0;

        while (!queue.isEmpty()) {
            int sz = queue.size();
            for (int i=0; i<sz; i++) {
                int[] block = queue.poll();
                for (var dir : dirs) {
                    int nx = block[0] + dir[0];
                    int ny = block[1] + dir[1];
                    if (nx > -1 && nx < rows && ny > -1 && ny < cols && grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        rotten += 1;
                        queue.offer(new int[] {nx, ny});
                    }
                }
            }
            steps += 1;
        }

        return (total > rotten) ? -1 : steps-1;
    }
}
```

经典bfs搜索，这里用两个int记录一下腐烂橘子和总共的橘子数量，然后每次都将队列里所有的腐烂源出队污染其他橘子；两个要点，第一个要点是搜索完所有橘子后判断是否已经不存在新鲜橘子，不存在返回0；要点二是steps这个值在尝试搜索后才+1，也就是说，返回值需要-1。例如如果全局就一个烂橘子，那么step为0，但是还是要尝试搜索1轮，steps会在这里+1；

---

## [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历**。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();
        if (root == null) return res;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean isEven = false;
        while (!queue.isEmpty()) {
            int sz = queue.size();
            Deque<Integer> list = new LinkedList<>();
            for (int i=0; i<sz; ++i) {
                TreeNode node = queue.poll();
                if (isEven) list.offerFirst(node.val);
                else list.offer(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right); 
            }
            res.add(new LinkedList<Integer>(list));
            isEven = !isEven;
        }   
        return res;
    }
}
```

可以考虑的方法是，记录每一次遍历的奇偶次序，然后偶数时翻转该层的遍历结果；也可以使用双端队列，偶数层时从前端插入遍历值；

---

## [1254. 统计封闭岛屿的数目](https://leetcode.cn/problems/number-of-closed-islands/)

二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一个 `完全` 由1包围（左、上、右、下）的岛。请返回 *封闭岛屿* 的数目。

```java
class Solution {
    public int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int rows = -1;
    public int cols = -1;
    public int[][] grid;

    public int closedIsland(int[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        this.grid = grid;

        int res = 0;
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (grid[i][j] == 0 && dfs(i, j)) {
                    res++;
                }
            }
        }
        return res;
    }

    public boolean dfs(int x, int y) {
        if (x < 0 || x >= rows || y < 0 || y >= cols) return false;
        if (grid[x][y] == 1) return true;
        grid[x][y] = 1;
        return dfs(x+1, y) & dfs(x-1, y) & dfs(x, y+1) & dfs(x, y-1);
    }
    
    public boolean dfs2(int x, int y) {
        grid[x][y] = -1;
        boolean isClosed = true;
        if (x == 0 || x == rows-1 || y == 0 || y == cols-1) {
            isClosed = false;
        }
        for (var dir : dirs) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx < rows && nx > -1 && ny < cols && ny > -1 && grid[nx][ny] == 0) {
                isClosed = isClosed & dfs(nx, ny);
            }
        }
        return isClosed;
    }
}
```

思路是，朴素的搜索算法搜寻整个岛屿，若有地块在边界处，则该岛屿不是封闭岛屿。注意：dfs2 是我写的方法，其中有一个问题一直困扰了我，首先 Java中的 `&` 没有短路功能，而 `&& ` 有，因此使用第二种与会丢失一些岛屿为-1的机会；第二不可以在第一个 `if` 中返回，原理是相同的，如果第一次扫描到边界处就直接返回，会丢失与其链接的岛屿地块；所以必须完整找到岛屿后，再返回结果。





# 排序 中等练习

## [179. 最大数](https://leetcode.cn/problems/largest-number/)

给定一组非负整数 `nums`，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

**注意：**输出结果可能非常大，所以你需要返回一个字符串而不是整数。

```java
class Solution {
    public String largestNumber(int[] nums) {
        int l = nums.length;
        String[] numbers = new String[l];
        for (int i=0; i<l; i++) {
            numbers[i] = nums[i] +"";
        }

        Arrays.sort(numbers, (x, y) -> {
            return (y+x).compareTo(x+y);
        });

        if (numbers[0].equals("0")) return "0";

        StringBuilder sb = new StringBuilder();
        for (var each : numbers) {
            sb.append(each);
        }
        
        return sb.toString();
    }
}
```

`sort` 方法中传入一个比较器，按照比较器规则，若返回的值**大于0**那么就交换参数的位置，在这里是 `x` 和 `y` ，例如比较两个数的大小，就是 `return x-y` 即可，`x` 较小时返回负数，位置关系不变；在本题中，我们需要重新组合两个数，查看其大小（字符串比较会比较每个元素的ASCII码大小），若 `y+x` 更大一些，那么通过 `compareTo()` 方法返回一个正数，就会交换 `x` `y` 的位置，完成排序（因为我们需要大数在前，然后进行拼接）；最后注意若存在多个0，事实上是只存在0的情况，直接判断排序后数组第一个元素，若为0就直接返回0，因为0在这里是最大的，没法进行比较了。

>  [面试题45. 把数组排成最小的数](https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/) 是一道一模一样的题，而且不需要去除先导0



# 栈 练习

## [1047. 删除字符串中的所有相邻重复项](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

给出由小写字母组成的字符串 `S`，**重复项删除操作**会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

```java
class Solution {
    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();
        int top = -1;
        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (top >= 0 && sb.charAt(top) == ch) {
                sb.deleteCharAt(top);
                top--;
            } else {
                top++;
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
```

不需要栈结构，用 `StringBuilder` 直接模仿，利用top记录栈顶元素即可；

---

## [剑指 Offer 31. 栈的压入、弹出序列](https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

 ```java
 class Solution {
     public boolean validateStackSequences(int[] pushed, int[] popped) {
         Deque<Integer> stack = new ArrayDeque<>();
         int n = pushed.length;
         for (int i=0, j=0; i<n; i++) {
             stack.push(pushed[i]);
             while (!stack.isEmpty() && stack.peek() == popped[j]) {
                 stack.poll();
                 j++;
             }
         }
         return stack.isEmpty();
     }
 }
 ```

比较简单，大致上就是一个模拟，不过注意stack的实现，在 `Deque` 中，`offer` 与 `push` 的推入元素方向相反，但`pop` 与 `poll` 相同，这里也可以使用 `pop` 方法弹出元素；另外可以在循环中初始化 `j` ，十分方便。

---

## [1190. 反转每对括号间的子串](https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/)

给出一个字符串 `s`（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 **不应** 包含任何括号。

```java
class Solution {
    public String reverseParentheses(String s) {
        Deque<String> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(sb.toString());
                sb.setLength(0);
            } else if (c == ')') {
                sb.reverse();
                sb.insert(0, stack.pop());
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

这题用python来做会比较轻松，用java的话，首先构造栈，以及一个类似于列表的结构，这里直接用 `StringBuilder`，当成临时存储；模拟逻辑如下：

1. 遇到字母，就加入临时sb中；
2. 遇到 `(` ，说明要处理新的字符串片段，将临时sb中的字符串存入stack，清空sb；
3. 遇到 `)` ，代表需要处理sb中的字符串，这个时候进行翻转；之后的逻辑事实上是，进行翻转后将sb入栈，紧接着将栈中的元素按顺序全部取出，等待下次操作，不过可以化简。将栈顶字符串片段直接插入sb的前端完成拼接即可；

有两点需要注意，第一个是 `stack.pop()` 是不会为空的，因为遇到 `)` 时，必定已经执行过一次对应的 `stack.push(sb.toString());` 不过开始的时候这东西加入了一个空串进去；

---

## [394. 字符串解码](https://leetcode.cn/problems/decode-string/)

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。

```java
class Solution {
    public String decodeString(String s) {
        StringBuilder sb = new StringBuilder();
        Deque<String> stack = new ArrayDeque<>();
        Deque<Integer> timesStack =  new ArrayDeque<>();
        Integer times = 0;

        for (var c: s.toCharArray()) {
            if (c == '[') {
                timesStack.push(times);
                stack.push(sb.toString());
                times = 0;
                sb.setLength(0);
            } else if (c == ']') {
                StringBuilder _sb = new StringBuilder();
                Integer _times = timesStack.pop();
                for (int i=0; i<_times; i++) {
                    _sb.append(sb);
                }
                sb = new StringBuilder(stack.pop() + _sb);
            } else if (Character.isDigit(c)) {
                times = times*10 + c - '0';
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

一种比较清晰的写法了，这题自己想的时候乱七八糟的，原因是Java字符串和字符转换啥的很不方便；准备两个栈，用来存放字符串以及倍数。然后按照以下规则模拟操作：

1. 遇到 `[` ，说明需要处理新的字符串片段了，而且倍数已经存储完成，那么将**倍数**以及当前**sb**内的字符串压入栈中，然后**清空倍数**以及**sb**；
2. 遇到 数字，按照自己写方法使用 `while` 推进找到所有数字的，不过容易把方法搞乱；这里的写法直接用一个int 倍数接收，做运算即可；
3. 遇到 字母，放入sb中；
4. 遇到 `]` ，说明需要做乘法处理了，这个时候我们需要从**倍数栈**中弹出上一个倍数，然后将当前的sb*该倍数完成计算。然后再将栈中的字符串弹出拼接到sb内；在 Java中我们看到了是通过临时sb做操作，然后sb调用new去完成栈和当前字符串的拼接的；

---

## [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/)

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

```java
class Solution {
    public int longestValidParentheses(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = s.length();
        int max = 0;
        int start = 0;
        for (int i=0; i<n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    start = i + 1;
                } else {
                    stack.pop();
                    if (stack.isEmpty()) {
                        max = Math.max(max, i-start+1);
                    } else {
                        max = Math.max(max, i-stack.peek());
                    }
                }
            }
        }
        return max;
    }
}
```

注意，这是一道困难题，在我查看之前的python代码时，觉得很不好理解，所以使用了这个方法；首先有效字符串长度，想要记录长度，可以在栈中记录索引值，以方便遍历的时候计算。原来的题解中，利用-1作为栈的填充，目的是为了记录未被匹配的右括号的值，用于重新记录新的连续合法括号长度。如果不用，那么我们需要维护一个变量start，按照如此规则来进行寻找：

1. 遇到 `(` ，记录索引值，压入栈中；
2. 遇到 `)` ，首先查看栈是否为空，为空可能是因为**还未开始匹配**或者**上一次匹配已经完成**，但无论如何，这个右括号都是匹配不上的，这个时候 `start = i + 1;` ，基本意思就是忽略掉这个右括号，重新规定本轮匹配的开始位置；若栈不为空，说明有对应的左括号可以匹配，那么弹出这个括号，此时又分为两种情况：
   1. 若此时栈不为空，那么**可能还会出现右括号匹配栈中的左括号**，而当前最长的匹配长度就是当前索引 `i` 减去栈顶索引（其实就是说匹配到栈顶索引对应的左括号位置右侧）；
   2. 此时栈为空，那么我们可以通过记录的start，开始位置来计算当前的最长匹配长度，很明显第一种情况不这样计算是因为还可能出现新的右括号匹配。但最终一定是会到达情况二的计算一轮匹配的长度的；.

最后返回记录的max即可

---

## [224. 基本计算器](https://leetcode.cn/problems/basic-calculator/)

给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()` 。

```java
class Solution {
    public Deque<Integer> nums = new LinkedList<>();
    public Deque<Character> ops = new LinkedList<>();

    public int calculate(String s) {
        s = s.replaceAll(" ", "");
        nums.push(0);
        char[] chars = s.toCharArray();
        for (int i=0; i<chars.length; i++) {
            char c = chars[i];
			if (c == '(') {
                ops.push(c);
            } else if (c == ')') {
                while (!ops.isEmpty()) {
                    char op = ops.peek();
                    if (op != '(') {
                        cal();
                    } else {
                        ops.pop();
                        break;
                    }
                }
            } else if (Character.isDigit(c)) {
                int j = i;
                StringBuilder sb = new StringBuilder();
                while (j < chars.length && Character.isDigit(chars[j])) {
                    sb.append(chars[j]);
                    j++;
                }
                nums.push(Integer.parseInt(sb.toString()));
                i = j-1;
            } else {
                if (i>0)
                    // System.out.printf("%d %s, previous %s, push 0\n", i, chars[i], chars[i-1]);
                if (i > 0 && (chars[i-1]=='(' || chars[i-1]=='+' || chars[i-1]=='-') ) {
                    nums.push(0);
                }
                while (!ops.isEmpty() && ops.peek() != '(') {
                    cal();
                }
                ops.push(c);
            }
        }
        while (!ops.isEmpty()) cal();
        return nums.pop();
    }

    public void cal() {
        if (nums.size() < 2 || nums.isEmpty()) return;
        if (ops.isEmpty()) return;
        int y = nums.pop();
        int x = nums.pop();
        char op = ops.pop();

        if (op == '+') {
            nums.push(x+y);
        } else if (op == '-') {
            nums.push(x-y);
        }
        // System.out.printf("%d %s %d = %s\n", x, op, y, nums.peek());
    }
}
```

友塔二面的算法题的简化版本，当时想着是两个栈存放符号以及数字，但是细节上实在是说得乱七八糟，因此来整理一下思路；这题还不存在符号优先级，只有加减；

- 首先用两个栈分别存放没有问题，但是什么时候进行运算是重点，遇到**左括号**或者**数字**的时候就直接入栈（数字需要进行处理，这里使用的是 `Stringbuilder` ，不过直接使用ASCII码的加减更简单）；

- 遇到运算符的时候，先不进行**该运算符**的运算，如果运算符栈内有符号，且第一个**不是左括号**，那么可以不断进行 `cal()` 操作，取两个数（这里要注意顺序，先弹出的是y，后弹出的是x）和一个运算符，完成运算后把结果压入数字栈，然后再将**该运算符入栈**，并且这里还有个条件用于处理**正负数**，如果我们遇到了运算符，并尝试获取上一个位置的元素，该元素也是一个运算符元素而不是数字时，说明这个运算符是表示正负的符号，处理方法是压入一个0进入数字栈。（这里我一开始直接在循环里跳过空格元素，导致这里bug查了好久，因为上一个遍历元素可能是空格，必须一开始就清空所有的空格）
- 遇到**右括号**的时候，不断进行 `cal()` 操作直到遇到左括号，并且将左括号弹出；
- 最后，完成遍历后，运算符栈中可能还存在（事实上大部分情况都存在）运算符，也要不断进行 `cal()` 操作；
- 注意，在第二种情况下，我们通过压入0来处理正负数符号，但可能一开始就会遇到这样的符号无法判别，因此直接在最初的数字栈中**添加一个0**，即使这个0不被用到也没有关系，因为最后的结束条件是运算符栈为空。

# 单调栈 练习

## [496. 下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/)

`nums1` 中数字 `x` 的 **下一个更大元素** 是指 `x` 在 `nums2` 中对应位置 **右侧** 的 **第一个** 比 `x` 大的元素。

给你两个 **没有重复元素** 的数组 `nums1` 和 `nums2` ，下标从 **0** 开始计数，其中`nums1` 是 `nums2` 的子集。

对于每个 `0 <= i < nums1.length` ，找出满足 `nums1[i] == nums2[j]` 的下标 `j`，并且在 `nums2` 确定 `nums2[j]` 的 **下一个更大元素** 。如果不存在下一个更大元素，那么本次查询的答案是 `-1`。

返回一个长度为 `nums1.length` 的数组 `ans` 作为答案，满足 `ans[i]` 是如上所述的 **下一个更大元素** 。

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i=nums2.length-1; i>-1; i--) {
            int num = nums2[i];
            while (!stack.isEmpty() && stack.peek() < num) {
                stack.pop();
            }
            if (stack.isEmpty()) map.put(nums2[i], -1);
            else map.put(nums2[i], stack.peek());
            stack.push(num);
        }
        int[] res = new int[nums1.length];
        for (int i=0; i<nums1.length; i++) {
            res[i] = map.get(nums1[i]);
        }
        return res;
    }
}

```

感觉单调栈一直都不是很好理解。在这题简单来说就是求 `nums2` 中每个元素之后的第一个比该元素大的元素是谁，（这里是元素的值，而不是索引）。按照官方题解，维护一个**单调递减的栈**，从后向前遍历；此时遍历到的数字如果比栈顶元素要大，说明比该数字大且在该数字后方的元素可能：1）还在栈的底层，此时需要不断弹出栈顶比该数字小的元素；2）不存在，若弹出栈里所有元素都寻找不到，说明不存在；

因此，通过while循环不断弹出数字后，若此时栈为空，则不存在比该数字大的元素了，向map中存-1；若此时不为空，则证明栈顶元素就是第一个比该数字大的元素了，想map中存栈顶元素；之后将该元素入栈，作为之后轮次中较大且靠前的元素。

```java
Deque<Integer> stack = new ArrayDeque<>();
Map<Integer,Integer> map = new HashMap<>();

for(int i=0; i<nums2.length; i++){
    int num = nums2[i];
    while(!stack.isEmpty() && num>stack.peek()){
        map.put(stack.pop(),num);
    }
    stack.push(num);
}

int[] res = new int[nums1.length];
for(int i=0; i<nums1.length; i++){
    res[i] = map.getOrDefault(nums1[i],-1);
}

return res;
```

不过，正序也是可以操作的，不过不好理解罢了。栈内还是单调递减的规则存放，直到遇见比栈顶元素大的数字，那么所有在栈内比当前数字小的元素都必须弹出栈，并且该数字就是这些元素能够第一次遇见的比它们大的数字了，因此在出栈的同时存放进map中，value就为当前遍历的数字；之后再进栈当前数字即可；这样，一些元素就可能存留在栈中，不存在比它们大的数字了，这个时候最后使用 `map.getOrDefault` 将它们赋值为-1即可。

---

## [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)

给定一个循环数组 `nums` （ `nums[nums.length - 1]` 的下一个元素是 `nums[0]` ），返回 *`nums` 中每个元素的 **下一个更大元素***。

数字 `x` 的 **下一个更大的元素** 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 `-1`。

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        Deque<Integer> stack = new ArrayDeque<>();
        int[] res = new int[n];
        Arrays.fill(res, -1);
        for (int i=0; i<n*2-1; i++) {
            int idx = i % n;
            int num = nums[idx];
            while (!stack.isEmpty() && nums[stack.peek()] < num) {
                res[stack.pop()] = num;
            }
            stack.push(idx);
        }
        return res;
    }
}
```

依旧是单调递减栈，然后特殊的地方在于：记录索引值，存放索引值，因为结果数组需要用索引来确定存放位置；另外就是数组的隐式循环，“相当于接上”前n-1个数。最后是一个 `Arrays.fill()` 方法的应用，全部初始化为-1即可。

---

## [1475. 商品折扣后的最终价格](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/)

给你一个数组 `prices` ，其中 `prices[i]` 是商店里第 `i` 件商品的价格。

商店里正在进行促销活动，如果你要买第 `i` 件商品，那么你可以得到与 `prices[j]` 相等的折扣，其中 `j` 是满足 `j > i` 且 `prices[j] <= prices[i]` 的 **最小下标**，如果没有满足条件的 `j` ，你将没有任何折扣。请你返回一个数组，数组中第 `i` 个元素是折扣后你购买商品 `i` 最终需要支付的价格。

```java
class Solution {
    public int[] finalPrices(int[] prices) {
        int n = prices.length;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i=0; i<n; i++) {
            int price = prices[i];
            while (!stack.isEmpty() && prices[stack.peek()] >= price) {
                prices[stack.pop()] -= price;
            }
            stack.push(i);
        }
        return prices;
    }
}
```

寻找第一个比较小（还可以是相等的）数字，因此使用一个**单调递增栈**；其余的步骤一样，因为返回结果是用数组返回，所以栈内存的是索引值；另外，可以不需要新建一个数组，直接在原数组上进行增减，因为只遍历一遍，前面的价格出栈后就不再会影响后面的了。

---

## [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/)

给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = heights.length;
        int[][] edges = new int[n][2];
        for (int i=0; i<n; i++) {
            edges[i][0] = -1;
            edges[i][1] = n;
        }
        for (int i=0; i<n; i++) {
            int num = heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > num) {
                int idx = stack.pop();
                edges[idx][1] = i;
            }
            stack.push(i);
        }
        stack.clear();
        for (int i=n-1; i>-1; i--) {
            int num = heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > num) {
                int idx = stack.pop();
                edges[idx][0] = i;
            }
            stack.push(i);
        }
        int max = 0;
        for (int i=0; i<n; i++) {
            // System.out.printf("%d : %d : %d \n", i, edges[i][0], edges[i][1]);
            int length = edges[i][1] - edges[i][0] - 1;
            max = Math.max(max, length*heights[i]);
        }
        return max;
    }
}
```

写的比较丑陋，但是思路非常清晰；怎么寻找最大的矩形，我们可以参照每一个位置的高度，查看用该高度向左右方向延伸的最长距离，例如，从高度为5的位置，可以发现，向左无法延伸，向右可以延伸至高度为6的位置。实际上就是寻找，左右侧**第一个**比该高度小的位置，作为边界，而在边界内的所有高度都会与该高度一致或者更高，那么我们就可以算出该位置的最大矩形面积了：`heights[i] * ((right-1)-(left+1)+1)` 

![img](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

所以，用一个二维数组存放左右边界，然后调用两次单调栈寻找每个高度的左右边界，最后计算高度即可；

---

## [402. 移掉 K 位数字](https://leetcode.cn/problems/remove-k-digits/)

给你一个以字符串表示的非负整数 `num` 和一个整数 `k` ，移除这个数中的 `k` 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

```java
class Solution {
    public String removeKdigits(String num, int k) {
        int l = num.length();
        if (l == k) return "0";
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i=0; i<l; i++) {
            int c = num.charAt(i) - '0';
            while (!stack.isEmpty() && stack.peek() > c && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<k; i++) {
            stack.pop();
        }
        // System.out.println(stack);
        boolean isZero = true;
        while (!stack.isEmpty()) {
            if (isZero && stack.peekLast() == 0) {
                stack.pollLast();
                continue;
            }
            isZero = false;
            sb.append(stack.pollLast());
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

感觉用Java写相当的难受，不知道用什么方法简化这个过程，而且各种出错反正。首先，需要明白，删除的是哪些数字。当ab....这个顺序出现时，比较a和b的大小，把大的那个移除掉，后面拼接的都会小一些。如果我们维护一个单调不减的栈（上升），那么就是说，每次遇到比栈顶元素小的数字，证明我们需要删除栈内部的某些元素来使最后的数字更小；这个删除的操作收到k大小的限制，只能最多弹出k次。并且，若没能完成k次的弹出，我们就删除后续进入的数字，直到操作次数达到上限。

这里的要点是，直接使用k--，k可以在两个循环内共用。之后，去除先导0的操作按照这个模板来就好，最后需要判断是否全部为0，若全部为0，需要手动返回“0”，因为此时cs里没有任何东西。

---

## [316. 去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/)

给你一个字符串 `s` ，请你去除字符串中重复的字母，使得每个字母只出现一次。

需保证 **返回结果的字典序最小**（要求不能打乱其他字符的相对位置）。

```java
class Solution {
    public String removeDuplicateLetters(String s) {
        HashSet<Character> set = new HashSet<>();
        Deque<Character> stack = new ArrayDeque<>();
        int[] times = new int[26];
        for (int i=0; i<s.length(); i++) {
            times[s.charAt(i)-'a'] += 1;
        }

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (!set.contains(c)) {
                while (!stack.isEmpty() && stack.peek() > c &&  times[stack.peek()-'a'] > 0) { 
                    set.remove(stack.pop());
                }
                stack.push(c);
                set.add(c);
            }
            times[c-'a'] -= 1;
            
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast());
        }
        return sb.toString();
    }
}
```

可能写法并不是很明智，因为Java思路不是很开阔。这题首先需要字典序最小，很容易联想到单调栈，内部元素以升序排列（因为要求去除重复数字）。那么每次出现比栈顶元素小的字母时，查看栈顶元素是否之后还存在，这里需要一个计数器记录每个字母的数量，如果后续没有该字母，也就不能出栈，这个时候新的字母直接进栈。另外需要维护一个set，或者一个布尔数组，来查看当前stack内已经存在的字母，若已存在，新的相同字母位置肯定不好，也就不需要做操作直接跳过即可。





# DP 练习

## [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int minPrice = prices[0];
        int max= 0;
        for (int i=0; i<n; i++) {
            minPrice = Math.min(prices[i], minPrice);
            max = Math.max(prices[i]-minPrice, max);
        }
        return max;
    }
}
```

虽然没用到dp数组，但是这其实是空间优化过的dp；`minPrice` 记录的是历史最低价格，然后每次遍历都用当前的价格-历史最低价格即可；同时，更新最大差值以及最低价格；

---

## [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

给你一个整数数组 `prices` ，其中 `prices[i]` 表示某支股票第 `i` 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 **最多** 只能持有 **一股** 股票。你也可以先购买，然后在 **同一天** 出售。

返回 *你能获得的 **最大** 利润*。

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        dp[0][1] = -prices[0];
        for (int i=1; i<n; i++) {
            dp[i][0] = Math.max(dp[i-1][0], prices[i] + dp[i-1][1]);
            dp[i][1] = Math.max(dp[i-1][0] - prices[i], dp[i-1][1]);
        }
        return dp[n-1][0];
    }
}
```

标准dp表示能获得的最大利润，第二维表示当前是否持有股票；那么状态转移很好推理，未持有股票可能因为本身就未持有，今天也不操作；也可能是因为卖掉了股票；持有股票可能是因为本身就持有，今天不操作或者是今天刚刚购入。返回最后一天不持有股票的利润即可；

---

## [714. 买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

给定一个整数数组 `prices`，其中 `prices[i]`表示第 `i` 天的股票价格 ；整数 `fee` 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

**注意：**这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

```java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        dp[0][1] = -prices[0];

        for (int i=1; i<n; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]+prices[i]-fee);
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0]-prices[i]);
        }

        return dp[n-1][0];
    }
}
```

上一题的基础上，每次卖出减一笔手续费即可；

---

## [309. 最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

给定一个整数数组`prices`，其中第 `prices[i]` 表示第 `*i*` 天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

- 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][3];
        dp[0][2] = -prices[0];
        for (int i=1; i<n; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][2]+prices[i];
            dp[i][2] = Math.max(dp[i-1][2], dp[i-1][0]-prices[i]);
        }
        return Math.max(dp[n-1][0], dp[n-1][1]);
    }
}
```

相比于前几题，这一题需要多存储一个状态，未持有股票并有冷却的状态，这个状态代表从持有股票的状态到卖掉了股票。其他的都一样。

---

## [62. 不同路径](https://leetcode.cn/problems/unique-paths/)

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i=0; i<m; i++) {
            dp[i][0] = 1;
        }
        for (int j=0; j<n; j++) {
            dp[0][j] = 1;
        }

        for (int i=1; i<m; i++) {
            for(int j=1; j<n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
}
```

基本的dp，先初始化第一行以及第一列，之后转移方程清晰明了。

---

## [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/)

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int col = obstacleGrid[0].length;
        int[][] dp = new int[row][col];
        for (int i=0; i<row; i++) {
            if (obstacleGrid[i][0] == 1) {
                dp[i][0] = 0;
                break;
            }
            dp[i][0] = 1;
        }
        for (int j=0; j<col; j++) {
            if (obstacleGrid[0][j] == 1) {
                dp[0][j] = 0;
                break;
            }
            dp[0][j] = 1;
        }
        for (int i=1; i<row; i++) {
            for (int j=1; j<col; j++) {
                if (obstacleGrid[i][j] == 1) {
                    continue;
                }
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[row-1][col-1];
    }
}
```

朴素dp，在遍历的时候遇到障碍物跳过就行了；另外需要注意的点是，初始化的时候，如果路上有障碍，那么接下来的路都走不了了。

---

## [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

```java
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        if (n < 2) return s;

        boolean[][] dp = new boolean[n][n];
        for (int i=0; i<n; i++) {
            dp[i][i] = true;
        }
        int max = 0;
        int x=0, y=0;
        for (int i=n-2; i>-1; i--) {
            for (int j=i+1; j<n; j++) {
                if (s.charAt(i) == s.charAt(j) && (j-i == 1 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                    if (j-i+1 >= max) {
                        x = i;
                        y = j;
                        max = j-i+1;
                    }
                }
            }
        }
        return s.substring(x, y+1);

    }
}
```

老题新做，本来以为会很吃力，但是画图就行了；转移方程很简单，之后就是如何转移了；另外结果需要对字符串进行切分，既然是最长字符串，就不断更新max以及相应的坐标即可。

## [416. 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

```java
class Solution {
    public boolean canPartition(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        int len = nums.length;
        for (var num : nums) {
            sum += num;
        }
        if (sum % 2 == 1) return false;
        
        int target = sum / 2;
        if (nums[len-1] > target)  return false;

        boolean[][] dp = new boolean[len][target+1];
        dp[0][0] = true;
        dp[0][nums[0]] = true;

        for (int i=1; i<len; i++) {
            for (int j=0; j<target+1; j++) {
                if (j-nums[i] > -1) {
                    dp[i][j] = dp[i-1][j-nums[i]] || dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[len-1][target];

    }
}
```

这题做好几遍了，但是还是有点记不住；首先转化为01背包问题，选取一定数量的数组，拼成总和一半的值，这样就是一个01背包问题了；可以采取措施提前排除一些错误的数组，例如sum为奇数的，长度小于2的，最大值超过sum一半的；之后就是dp定义，`dp[i][j]` 定义为：**遍历到第i个数字时，是否能够凑成值j**。注意这一题是一个 `boolean` 数组，因此转移方程的决定是用或运算控制的，最后返回右下角的值即可；

**注意**：处理边界条件时，我漏掉了 ` dp[0][0] = true;` ，但是在这题的测试用例中，没有错误，但是下一题会出错；这里的0处表示不选这个位置但仍然能凑到0值；

## [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/)

有一堆石头，用整数数组 `stones` 表示。其中 `stones[i]` 表示第 `i` 块石头的重量。

每一回合，从中选出**任意两块石头**，然后将它们一起粉碎。假设石头的重量分别为 `x` 和 `y`，且 `x <= y`。那么粉碎的可能结果如下：

- 如果 `x == y`，那么两块石头都会被完全粉碎；
- 如果 `x != y`，那么重量为 `x` 的石头将会完全粉碎，而重量为 `y` 的石头新重量为 `y-x`。

最后，**最多只会剩下一块** 石头。返回此石头 **最小的可能重量** 。如果没有石头剩下，就返回 `0`

```java
class Solution {
    public int lastStoneWeightII(int[] stones) {
        Arrays.sort(stones);
        int sum = Arrays.stream(stones).sum();
        int target = sum / 2;
        int len = stones.length;

        if (len < 2) return stones[0];

        boolean[][] dp = new boolean[len][target+1];
        dp[0][0] = true;
        dp[0][stones[0]] = true;

        for (int i=1; i<len; i++) {
            for (int j=0; j<target+1; j++) {
                if (j-stones[i] >= 0) {
                    dp[i][j] = dp[i-1][j-stones[i]] || dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        for (int j=target; j>-1; j--) {
            if (dp[len-1][j]) {
                return sum-j-j;
            }
        }
        return 0;
    }
}
```

这个题目的思路是，将石子分成两堆尽量相近的重量，然后他们的差值就应该是最后剩下石子的重量，于是转化为01背包问题，选出一定数量的石子，凑成目标值即可；注意，这里的target需要是较小的那一个，不过Java中默认是地板除，所以没问题；其余的dp过程与上一题无异，只是最后需要从大到小遍历出最大的拼凑值，然后将另外一堆的石子减去这一堆的石子重量；



## [494. 目标和](https://leetcode.cn/problems/target-sum/)

给你一个整数数组 `nums` 和一个整数 `target` 。

向数组中的每个整数前添加 `'+'` 或 `'-'` ，然后串联起所有整数，可以构造一个 **表达式**：

- 例如，`nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。

返回可以通过上述方法构造的、运算结果等于 `target` 的不同 **表达式** 的数目。

```java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        Arrays.sort(nums);
        int sum = Arrays.stream(nums).sum();
        int pos = (sum + target) / 2;
        if ((sum + target) % 2 == 1 || pos < 0) return 0;
        int len = nums.length;

        if (len == 1) {
            if ( (target == nums[0] || target == -nums[0]) && nums[0] != 0) return 1;
            if (target == nums[0] && nums[0] == 0) return 2;
            return 0;
        }

        int[][] dp = new int[len][pos+1];
        dp[0][0] += 1;
        dp[0][nums[0]] += 1;

        for (int i=1; i<len; i++) {
            for (int j=0; j<pos+1; j++) {
                if (j - nums[i] >= 0) {
                    dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[len-1][pos];
    }
}
```

发现了之前Python版本的解题思路，开始的思路都是没有问题的，这次也比较清晰地写出来了，而且没有那么多疑问；需要注意的点是pos的值需要大于零，以及处理一下长度为1的特殊情况；之前在初始化赋值的时候，我们分了0特殊情况，但实际上可以直接使用加法来绕开特殊情况，然后转移方程变为加法，其余没有任何变化；



## [322. 零钱兑换](https://leetcode.cn/problems/coin-change/)

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int len = coins.length;
        int[][] dp = new int[len][amount+1];

        for (var each : dp) {
            Arrays.fill(each, amount+1);
        }  

        for (int k=0; k*coins[0]<=amount; k++) {
            dp[0][k*coins[0]] = k;
        }

        for (int i=1; i<len; i++) {
            for (int j=0; j<=amount; j++) {
                if (j < coins[i])
                    dp[i][j] = dp[i-1][j];
                else {
                    dp[i][j] = Math.min(dp[i-1][j], dp[i][j-coins[i]] + 1);
                }
            }
        }

        return dp[len-1][amount] == amount+1 ? -1 : dp[len-1][amount];
    }
    
    public int coinChange2(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

完全背包问题，上述第一种解法是没有优化过的二维dp，在我查询Python解法的时候，发现python是优化过的一维dp；在这里用标准二维dp来解释；首先建立dp数组，因为是求最小值，因此将所有值都初始化为最大值，这个最大值我选取integer的最大值时发生了越界，因此最好还是使用amount+1这种取不到的值最好；之后对第一行进行赋值，将0-k个第0个硬币组合，然后将个数填入dp；

之后就是正常的dp转移方程了，当j小于当前coin时，则只能从上层转移，也就是无法选取硬币；当j大于coin时，我们可以不选或者可以从同一行的上一个coin取值处跳跃过来，这个时候相当于选择了一枚当前行coin；

而第二种方法就是简单地思考方式的转变，dp[j] 表示组成j的最小个数，那么我们遍历coins，然后在j的基础上求出每个coin相转移过来的之前状态dp[j-coins[i]]+1，那么其中最小的就是dp[j]了



## [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/)

给你一个整数 `n` ，返回 *和为 `n` 的完全平方数的最少数量* 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp, n+1);
        dp[0] = 0;
        for (int i=1; i<n+1; i++) {
            for (int j=1; j*j<=i; j++) {
                dp[i] = Math.min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
}
```

本来想还是按照原计划用二维dp写出来，但是已经神志不清了；因此用最简单地思路来写：首先dp[i]表示最少个完全平方数能凑成i的值，而且需要注意dp[0]这个边界条件，凑不出来，但是我们需要它为0，方便转移状态；然后为每一个dp都赋上一个最大值，比如n+1；

从i=1开始，然后注意枚举的“硬币”，这里是借用上一题的说法，硬币的值就是j*j，如果这个值**小于等于**i（因为我们可以从0开始转移，等于i的时候证明只用一个完全平方数即可凑成），那么就可以进行转移了，转移方程与之前无异，选取最小的取值即可；最后返回倒数第一个dp值；



# 每日一题



## [1798. 你能构造出连续值的最大数目](https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/)

给你一个长度为 `n` 的整数数组 `coins` ，它代表你拥有的 `n` 个硬币。第 `i` 个硬币的值为 `coins[i]` 。如果你从这些硬币中选出一部分硬币，它们的和为 `x` ，那么称，你可以 **构造** 出 `x`。请返回从 `0` 开始（**包括** `0` ），你最多能 **构造** 出多少个连续整数。你可能有多个相同值的硬币。

```java
class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        int maxValue = 0;
        for (int coin : coins) {
            if (coin <= maxValue+1) {
                maxValue += coin;
            } else {
                break;
            }
        }
        return maxValue + 1;
    }
}
```

是一道经典贪心，然后~~并不会做~~，推导思路是，定义当前的可以构造出的范围为 [0, a]。当我们想添加一枚硬币（面值为b）以扩张范围时，可以推理出下一个增加的范围是 [0+b, a+b]。即每一个组合都添加该枚硬币；而题目条件要求连续，则 b <= a + 1，最大就是a+1的面值了。因此直接在循环中进行判断，若超过了该条件，就结束；此外需要注意的是，每次挑选硬币时选择最小的，因此需要排序，返回值则是 [0, a] 的长度（按数组理解）；

---

## [1138. 字母板上的路径](https://leetcode.cn/problems/alphabet-board-path/)

我们从一块字母板上的位置 `(0, 0)` 出发，该坐标对应的字符为 `board[0][0]`。

在本题里，字母板为`board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`，如下所示。

我们可以按下面的指令规则行动：

如果方格存在，`'U'` 意味着将我们的位置上移一行；

如果方格存在，`'D'` 意味着将我们的位置下移一行；

如果方格存在，`'L'` 意味着将我们的位置左移一列；

如果方格存在，`'R'` 意味着将我们的位置右移一列；

`'!'` 会把在我们当前位置 `(r, c)` 的字符 `board[r][c]` 添加到答案中。

返回指令序列，用最小的行动次数让答案和目标 `target` 相同。你可以返回任何达成目标的路径。

```java
class Solution {
    public String alphabetBoardPath(String target) {
        StringBuilder sb = new StringBuilder();
        int x = 0, y = 0;
        for (char c : target.toCharArray()) {
            int nx = (c - 'a') / 5;
            int ny = (c - 'a') % 5;
            String vertical = x < nx ? "D".repeat(nx-x) : "U".repeat(x-nx);
            String horizontal = y < ny ? "R".repeat(ny-y) : "L".repeat(y-ny);
            sb.append(c=='z' ? horizontal+vertical : vertical+horizontal).append("!");
            x = nx;
            y = ny;
        }
        return sb.toString();
    }
}
```

被题目骗了，不需要构造数组进行搜索。事实上最短的路径就是曼哈顿距离，而上面这个解答实行先计算目标位置，接着先垂直移动再水平移动的方式到达目标位置，中间的步骤都是记录移动，添加感叹号；不过因为 `z` 的位置特殊，进入时需要先水平移动，再垂直移动，出去时没有影响；另外和官方题解不同的是这里没有用循环的方式添加路径，这样效率不是很高。

---

## [2341. 数组能形成多少数对](https://leetcode.cn/problems/maximum-number-of-pairs-in-array/)

给你一个下标从 **0** 开始的整数数组 `nums` 。在一步操作中，你可以执行以下步骤：

- 从 `nums` 选出 **两个** **相等的** 整数
- 从 `nums` 中移除这两个整数，形成一个 **数对**

请你在 `nums` 上多次执行此操作直到无法继续执行。

返回一个下标从 **0** 开始、长度为 `2` 的整数数组 `answer` 作为答案，其中 `answer[0]` 是形成的数对数目，`answer[1]` 是对 `nums` 尽可能执行上述操作后剩下的整数数目。

```java
class Solution {
    public int[] numberOfPairs(int[] nums) {
        Arrays.sort(nums);
        int[] res = new int[2];
        int p = 0;
        while (p < nums.length-1) {
            if (nums[p] == nums[p+1]) {
                res[0] += 1;
                p += 2;
            } else {
                res[1] += 1;
                p += 1;
            }
        }
        if (p == nums.length-1) res[1] += 1;
        return res;
    }
}
```

临时想的方法，排序，然后两两比较，相同往右移动两位，否则就移动一位，并分别作对应的处理；



## [2363. 合并相似的物品](https://leetcode.cn/problems/merge-similar-items/)

给你两个二维整数数组 `items1` 和 `items2` ，表示两个物品集合。每个数组 `items` 有以下特质：

- `items[i] = [valuei, weighti]` 其中 `valuei` 表示第 `i` 件物品的 **价值** ，`weighti` 表示第 `i` 件物品的 **重量** 。
- `items` 中每件物品的价值都是 **唯一的** 。

请你返回一个二维数组 `ret`，其中 `ret[i] = [valuei, weighti]`， `weighti` 是所有价值为 `valuei` 物品的 **重量之和** 。

**注意：**`ret` 应该按价值 **升序** 排序后返回。

```java
class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] each : items1) {
            map.put(each[0], map.getOrDefault(each[0], 0)+each[1]);
        }

        for (int[] each : items2) {
             map.put(each[0], map.getOrDefault(each[0], 0)+each[1]);
        }
        
        List<List<Integer>> res = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry: map.entrySet()) {
            List<Integer> pair = new ArrayList<Integer>();
            pair.add(entry.getKey());
            pair.add(entry.getValue());
            res.add(pair);
        }
        Collections.sort(res, (x, y)-> {return x.get(0)-y.get(0);});
        return res;
    }
}
```

相当于复习map的用法了，想要遍历所有元素可以使用map的entry来获取元素，很神秘；
