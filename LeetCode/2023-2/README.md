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
