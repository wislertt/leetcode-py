# Convert Sorted List to Binary Search Tree

**Difficulty:** Medium
**Topics:** Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
**Tags:**

**LeetCode:** [Problem 109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)

## Problem Description

Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

### Example 2:

```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in head is in the range [0, 2 * 10^4].
- -10^5 <= Node.val <= 10^5
