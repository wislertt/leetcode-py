# Closest Binary Search Tree Value

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 270](https://leetcode.com/problems/closest-bst-value/description/)

## Problem Description

Given the `root` of a binary search tree and a `target` value, return _the value in the BST that is closest to the_ `target`. If there are multiple answers, print the smallest.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0270.Closest%20Binary%20Search%20Tree%20Value/images/closest1-1-tree.jpg)

```
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
```

### Example 2:

```
Input: root = [1], target = 4.428571
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `0 <= Node.val <= 10^9`
- `-10^9 <= target <= 10^9`
