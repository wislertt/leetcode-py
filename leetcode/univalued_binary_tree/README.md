# Univalued Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Tags:**

**LeetCode:** [Problem 965](https://leetcode.com/problems/univalued-binary-tree/description/)

## Problem Description

A binary tree is <strong>uni-valued</strong> if every node in the tree has the same value.

Given the <code>root</code> of a binary tree, return <code>true</code> if the given tree is <strong>uni-valued</strong>, or <code>false</code> otherwise.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

```
Input: root = [1,1,1,1,1,null,1]
Output: true
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

```
Input: root = [2,2,2,5,2]
Output: false
```

## Constraints

- The number of nodes in the tree is in the range [1, 100]
- 0 <= Node.val < 100
