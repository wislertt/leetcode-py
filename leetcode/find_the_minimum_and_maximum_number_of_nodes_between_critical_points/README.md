# Find the Minimum and Maximum Number of Nodes Between Critical Points

**Difficulty:** Medium
**Topics:** Linked List
**Tags:** neetcode

**LeetCode:** [Problem 2058](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/)

## Problem Description

A **critical point** in a linked list is defined as **either** a **local maxima** or a **local minima**.

A node is a **local maxima** if the current node has a value **strictly greater** than the previous node and the next node.

A node is a **local minima** if the current node has a value **strictly smaller** than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists **both** a previous node and a next node.

Given a linked list `head`, return _an array of length 2 containing_ `[minDistance, maxDistance]` _where_ `minDistance` _is the_ _**minimum distance**_ _between_ _**any two distinct**_ _critical points and_ `maxDistance` _is the_ _**maximum distance**_ _between_ _**any two distinct**_ _critical points. If there are_ _**fewer**_ _than two critical points, return_ `[-1, -1]`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/10/13/a1.png)

```
Input: head = [3,1]
Output: [-1,-1]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/10/13/a2.png)

```
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2021/10/14/a5.png)

```
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
```

## Constraints

- The number of nodes in the list is in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`
