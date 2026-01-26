# Binary Tree Inorder Traversal

**Difficulty:** Easy
**Topics:** Stack, Tree, Depth-First Search, Binary Tree
**Tags:** algo-master-75

**LeetCode:** [Problem 94](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

## Problem Description

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
```

### Example 3:

```
Input: root = []
Output: []
```

### Example 4:

```
Input: root = [1]
Output: [1]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?
