# Kth Smallest Number in Multiplication Table

**Difficulty:** Hard
**Topics:** Math, Binary Search
**Tags:**

**LeetCode:** [Problem 668](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/)

## Problem Description

Nearly everyone has used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (1-indexed).

Given three integers `m`, `n`, and `k`, return the kth smallest element in the `m x n` multiplication table.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg)

```
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg)

```
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
```

## Constraints

- 1 <= m, n <= 3 * 10^4
- 1 <= k <= m * n
