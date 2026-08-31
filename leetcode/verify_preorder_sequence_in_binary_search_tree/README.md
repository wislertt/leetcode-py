# Verify Preorder Sequence in Binary Search Tree

**Difficulty:** Medium
**Topics:** Stack, Tree, Binary Search Tree, Recursion, Array, Binary Tree, Monotonic Stack
**Tags:** neetcode

**LeetCode:** [Problem 255](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/)

## Problem Description

Given an array of **unique** integers `preorder`, return `true` _if it is the correct preorder traversal sequence of a binary search tree_.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0255.Verify%20Preorder%20Sequence%20in%20Binary%20Search%20Tree/images/preorder-tree.jpg)

```
Input: preorder = [5,2,1,3,6]
Output: true
```

### Example 2:

```
Input: preorder = [5,2,6,1,3]
Output: false
```

## Constraints

- `1 <= preorder.length <= 10^4`
- `1 <= preorder[i] <= 10^4`
- All the elements of `preorder` are **unique**.

**Follow up:** Could you do it using only constant space complexity?
