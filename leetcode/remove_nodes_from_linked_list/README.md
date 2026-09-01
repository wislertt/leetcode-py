# Remove Nodes From Linked List

**Difficulty:** Medium
**Topics:** Linked List, Stack, Recursion, Monotonic Stack
**Tags:** neetcode

**LeetCode:** [Problem 2487](https://leetcode.com/problems/remove-nodes-from-linked-list/description/)

## Problem Description

You are given the <code>head</code> of a linked list.

Remove every node which has a node with a <strong>greater</strong> value anywhere to the <strong>right</strong> side of it.

Return <em>the head of the modified linked list</em>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/10/02/drawio.png)

```
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
```

### Example 2:

```
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
```

## Constraints

- The number of the nodes in the given list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
