# Largest Plus Sign

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Tags:**

**LeetCode:** [Problem 764](https://leetcode.com/problems/largest-plus-sign/description/)

## Problem Description

You are given an integer `n`. You have an `n x n` binary grid `grid` with all values initially `1`'s except for some indices given in the array `mines`. The `i^th` element of the array `mines` is defined as `mines[i] = [x_i, y_i]` where `grid[x_i][y_i] == 0`.

Return _the order of the largest **axis-aligned** plus sign of_ 1*'s contained in* `grid`. If there is none, return `0`.

An **axis-aligned plus sign** of `1`'s of order `k` has some center `grid[r][c] == 1` along with four arms of length `k - 1` going up, down, left, and right, and made of `1`'s. Note that there could be `0`'s or `1`'s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `1`'s.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg)

```
Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg)

```
Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
```

## Constraints

- 1 <= n <= 500
- 1 <= mines.length <= 5000
- 0 <= xi, yi < n
- All the pairs (xi, yi) are unique.
