# Find Mode in Binary Search Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree
**Tags:**

**LeetCode:** [Problem 501](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/)

## Problem Description

Given the `root` of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in **any order**.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
- The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
- Both the left and right subtrees must also be binary search trees.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg)

```
Input: root = [1,null,2,2]
Output: [2]
```

### Example 2:

```
Input: root = [0]
Output: [0]
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count.)
