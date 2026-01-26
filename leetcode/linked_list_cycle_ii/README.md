# Linked List Cycle II

**Difficulty:** Medium
**Topics:** Hash Table, Linked List, Two Pointers
**Tags:** algo-master-75

**LeetCode:** [Problem 142](https://leetcode.com/problems/linked-list-cycle-ii/description/)

## Problem Description

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

## Constraints

- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

**Follow up:** Can you solve it using O(1) (i.e. constant) memory?
