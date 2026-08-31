# Arranging Coins

**Difficulty:** Easy
**Topics:** Math, Binary Search
**Tags:** neetcode

**LeetCode:** [Problem 441](https://leetcode.com/problems/arranging-coins/description/)

## Problem Description

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `i^th` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return _the number of **complete rows** of the staircase you will build_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)

```
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)

```
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
```

## Constraints

- `1 <= n <= 2^31 - 1`
