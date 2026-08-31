# Remove Linked List Elements

**Difficulty:** Easy
**Topics:** Linked List, Recursion
**Tags:** neetcode

**LeetCode:** [Problem 203](https://leetcode.com/problems/remove-linked-list-elements/description/)

## Problem Description

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return _the new head_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

### Example 2:

```
Input: head = [], val = 1
Output: []
```

### Example 3:

```
Input: head = [7,7,7,7], val = 7
Output: []
```

## Constraints

- The number of nodes in the list is in the range [0, 10<sup>4</sup>]
- 1 <= Node.val <= 50
- 0 <= val <= 50
