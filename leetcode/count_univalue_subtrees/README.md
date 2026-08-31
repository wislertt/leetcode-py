# Count Univalue Subtrees

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 250](https://leetcode.com/problems/count-univalue-subtrees/description/)

## Problem Description

Given the `root` of a binary tree, return _the number of **uni-value**_ _subtrees_.

A **uni-value subtree** means all nodes of the subtree have the same value.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0250.Count%20Univalue%20Subtrees/images/unival_e1.jpg)

```
Input: root = [5,1,5,5,5,null,5]
Output: 4
```

### Example 2:

```
Input: root = []
Output: 0
```

### Example 3:

```
Input: root = [5,5,5,5,5,null,5]
Output: 6
```

## Constraints

- The number of nodes in the tree will be in the range `[0, 1000]`.
- `-1000 <= Node.val <= 1000`
