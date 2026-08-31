# Maximum Average Subtree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 1120](https://leetcode.com/problems/maximum-average-subtree/description/)

## Problem Description

Given the `root` of a binary tree, return _the maximum **average** value of a subtree of that tree_. Answers within `10^-5` of the actual answer will be accepted.

A **subtree** of a tree is any node of that tree plus all its descendants.

The **average** value of a tree is the sum of its values, divided by the number of nodes.

## Examples

### Example 1:

```
Input: root = [5,6,1]
Output: 6.00000
Explanation: For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4. For the node with value = 6 we have an average of 6 / 1 = 6. So the answer is 6 which is the maximum.
```

### Example 2:

```
Input: root = [0,null,1]
Output: 1.00000
```

## Constraints

- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^5
