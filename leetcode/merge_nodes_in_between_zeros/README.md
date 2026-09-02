# Merge Nodes in Between Zeros

**Difficulty:** Medium
**Topics:** Linked List, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 2181](https://leetcode.com/problems/merge-nodes-in-between-zeros/description/)

## Problem Description

You are given the <code>head</code> of a linked list, which contains a series of integers <strong>separated</strong> by <code>0</code>'s. The <strong>beginning</strong> and <strong>end</strong> of the linked list will have <code>Node.val == 0</code>.

For <strong>every</strong> two consecutive <code>0</code>'s, <strong>merge</strong> all the nodes lying in between them into a single node whose value is the <strong>sum</strong> of all the merged nodes. The modified list should not contain any <code>0</code>'s.

Return <em>the head of the modified linked list</em>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png)

```
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: The modified list contains the sum of the nodes marked in green: 3 + 1 = 4, and the sum of the nodes marked in red: 4 + 5 + 2 = 11.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png)

```
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: The modified list contains the sum of the nodes marked in green: 1 = 1, the sum of the nodes marked in red: 3 = 3, and the sum of the nodes marked in yellow: 2 + 2 = 4.
```

## Constraints

- The number of nodes in the list is in the range `[3, 2 * 10^5]`.
- `0 <= Node.val <= 1000`
- There are no two consecutive nodes with `Node.val == 0`.
- The beginning and end of the linked list have `Node.val == 0`.
