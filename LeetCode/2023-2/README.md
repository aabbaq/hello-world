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
