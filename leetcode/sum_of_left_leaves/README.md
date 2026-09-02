# Sum of Left Leaves

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Tags:**

**LeetCode:** [Problem 404](https://leetcode.com/problems/sum-of-left-leaves/description/)

## Problem Description

Given the `root` of a binary tree, return _the sum of all left leaves_.

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
```

### Example 2:

```
Input: root = [1]
Output: 0
```

## Constraints

- The number of nodes in the tree is in the range [1, 1000]
- -1000 <= Node.val <= 1000
