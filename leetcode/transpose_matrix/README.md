# Transpose Matrix

**Difficulty:** Easy
**Topics:** Array, Matrix, Simulation
**Tags:** neetcode-250

**LeetCode:** [Problem 867](https://leetcode.com/problems/transpose-matrix/description/)

## Problem Description

Given a 2D integer array `matrix`, return _the **transpose** of_ `matrix`.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

## Examples

### Example 1:

![Transpose hint](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

### Example 2:

```
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 10^5
- -10^9 <= matrix[i][j] <= 10^9
