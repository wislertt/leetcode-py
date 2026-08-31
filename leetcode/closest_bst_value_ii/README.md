# Closest Binary Search Tree Value II

**Difficulty:** Hard
**Topics:** Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Tree, Heap (Priority Queue)
**Tags:** neetcode

**LeetCode:** [Problem 272](https://leetcode.com/problems/closest-bst-value-ii/description/)

## Problem Description

Given the `root` of a binary search tree, a `target` value, and an integer `k`, return _the_ `k` _values in the BST that are closest to the_ `target`. You may return the answer in **any order**.

You are **guaranteed** to have only one unique set of `k` values in the BST that are closest to the `target`.

**Follow up:** Assume that the BST is balanced. Could you solve it in less than `O(n)` runtime (where `n = total nodes`)?

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0272.Closest%20Binary%20Search%20Tree%20Value%20II/images/closest1-1-tree.jpg)

```
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
```

### Example 2:

```
Input: root = [1], target = 0.000000, k = 1
Output: [1]
```

## Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`.
- `0 <= Node.val <= 10^9`
- `-10^9 <= target <= 10^9`
