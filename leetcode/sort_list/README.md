# Sort List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
**Tags:** grind

**LeetCode:** [Problem 148](https://leetcode.com/problems/sort-list/description/)

## Problem Description

Given the `head` of a linked list, return _the list after sorting it in ascending order_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

### Example 3:

```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5

**Follow up:** Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?
