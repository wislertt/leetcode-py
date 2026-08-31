# Check Completeness of a Binary Tree

**Difficulty:** Medium
**Topics:** Tree, Breadth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 958](https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/)

## Problem Description

<p>Given the <code>root</code> of a binary tree, determine if it is a <em>complete binary tree</em>.</p>

<p>In a <strong><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">complete binary tree</a></strong>, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
```

## Constraints

- The number of nodes in the tree is in the range [1, 100].
- 1 &lt;= Node.val &lt;= 1000
