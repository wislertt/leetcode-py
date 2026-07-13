# Path Sum III

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** algo-master-75, grind

**LeetCode:** [Problem 437](https://leetcode.com/problems/path-sum-iii/description/)

## Problem Description

Given the `root` of a binary tree and an integer `targetSum`, return _the number of paths where the sum of the values along the path equals_ `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

```
Input: root = [10,5,-3,3,2,None,11,3,-2,None,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```

### Example 2:

```
Input: root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
Output: 3
```

## Constraints

- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
