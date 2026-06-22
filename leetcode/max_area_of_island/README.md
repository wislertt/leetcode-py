# Max Area of Island

**Difficulty:** Medium
**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
**Tags:** neetcode-150

**LeetCode:** [Problem 695](https://leetcode.com/problems/max-area-of-island/description/)

## Problem Description

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

### Example 2:

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.
