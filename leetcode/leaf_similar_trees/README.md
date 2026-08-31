# Leaf-Similar Trees

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 872](https://leetcode.com/problems/leaf-similar-trees/description/)

## Problem Description

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a <strong>leaf value sequence</strong>.</p>

<p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

<p>Two binary trees are considered <em>leaf-similar</em> if their leaf value sequence is the same.</p>

<p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

## Constraints

- The number of nodes in each tree will be in the range [1, 200].
- Both of the given trees will have values in the range [0, 200].
