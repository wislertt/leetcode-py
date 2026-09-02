# Swapping Nodes in a Linked List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Tags:** neetcode

**LeetCode:** [Problem 1721](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)

## Problem Description

You are given the `head` of a linked list, and an integer `k`.

Return _the head of the linked list after **swapping** the values of the `k<sup>th</sup>` node from the beginning and the `k<sup>th</sup>` node from the end (the list is **1-indexed**)_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

### Example 2:

```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

## Constraints

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 10^5`
- `0 <= Node.val <= 100`

**Follow up:** Could you do this in one pass?
