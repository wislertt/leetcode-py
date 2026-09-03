# Equal Tree Partition

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:**

**LeetCode:** [Problem 663](https://leetcode.com/problems/equal-tree-partition/description/)

## Problem Description

Given the root of a binary tree, return true if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0663.Equal%20Tree%20Partition/images/split1-tree.jpg)

```
Input: root = [5,10,10,null,null,2,3]
Output: true
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0663.Equal%20Tree%20Partition/images/split2-tree.jpg)

```
Input: root = [1,2,10,null,null,2,20]
Output: false
Explanation: You cannot split the tree into two trees with equal sums after removing exactly one edge on the tree.
```

## Constraints

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
