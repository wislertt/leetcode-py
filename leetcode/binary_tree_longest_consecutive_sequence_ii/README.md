# Binary Tree Longest Consecutive Sequence II

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree, Tree DP
**Tags:** neetcode

**LeetCode:** [Problem 549](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/)

## Problem Description

Given the `root` of a binary tree, return the length of the longest consecutive path in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

- For example, `[1,2,3,4]` and `[4,3,2,1]` are both considered valid, but the path `[1,2,4,3]` is not valid.

On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0549.Binary%20Tree%20Longest%20Consecutive%20Sequence%20II/images/consec2-1-tree.jpg)

```
Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0549.Binary%20Tree%20Longest%20Consecutive%20Sequence%20II/images/consec2-2-tree.jpg)

```
Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
```

## Constraints

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-3 * 10^4 <= Node.val <= 3 * 10^4`
