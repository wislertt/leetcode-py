# Minimum Falling Path Sum

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 931](https://leetcode.com/problems/minimum-falling-path-sum/description/)

## Problem Description

<p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the minimum sum of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
```

## Constraints

- n == matrix.length == matrix[i].length
- 1 &lt;= n &lt;= 100
- -100 &lt;= matrix[i][j] &lt;= 100
