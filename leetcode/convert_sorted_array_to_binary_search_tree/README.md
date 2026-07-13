# Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy
**Topics:** Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
**Tags:** grind

**LeetCode:** [Problem 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

## Problem Description

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a **height-balanced** binary search tree.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

![Alt](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in a strictly increasing order.
