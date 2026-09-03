# Longest Line of Consecutive One in Matrix

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Matrix
**Tags:**

**LeetCode:** [Problem 562](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/)

## Problem Description

Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the length of the longest line of consecutive one in the matrix</em>.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0562.Longest%20Line%20of%20Consecutive%20One%20in%20Matrix/images/long1-grid.jpg)

```
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0562.Longest%20Line%20of%20Consecutive%20One%20in%20Matrix/images/long2-grid.jpg)

```
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
