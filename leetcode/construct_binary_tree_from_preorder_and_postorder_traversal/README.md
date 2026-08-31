# Construct Binary Tree from Preorder and Postorder Traversal

**Difficulty:** Medium
**Topics:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 889](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/)

## Problem Description

Given two integer arrays, <code>preorder</code> and <code>postorder</code> where <code>preorder</code> is the preorder traversal of a binary tree of <strong>distinct</strong> values and <code>postorder</code> is the postorder traversal of the same tree, reconstruct and return the binary tree.</p>

<p>If there exist multiple answers, you can return <strong>any</strong> of them.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg)

```
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

### Example 2:

```
Input: preorder = [1], postorder = [1]
Output: [1]
```

## Constraints

- 1 <= preorder.length <= 30
- 1 <= preorder[i] <= preorder.length
- All the values of preorder are unique.
- postorder.length == preorder.length
- 1 <= postorder[i] <= postorder.length
- All the values of postorder are unique.
- It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
