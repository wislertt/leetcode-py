# Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium
**Topics:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

## Problem Description

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return _the binary tree_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

### Example 2:

```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

## Constraints

- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of **unique** values
- Each value of postorder also appears in inorder
- inorder is **guaranteed** to be the inorder traversal of the tree
- postorder is **guaranteed** to be the postorder traversal of the tree
