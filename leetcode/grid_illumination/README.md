# Grid Illumination

**Difficulty:** Hard
**Topics:** Array, Hash Table
**Tags:**

**LeetCode:** [Problem 1001](https://leetcode.com/problems/grid-illumination/description/)

## Problem Description

There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially **turned off**.

You are given a 2D array of lamp positions `lamps`, where `lamps[i] = [row_i, col_i]` indicates that the lamp at `grid[row_i][col_i]` is **turned on**. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it **illuminates its cell** and **all other cells** in the same **row, column, or diagonal**.

You are also given another 2D array `queries`, where `queries[j] = [row_j, col_j]`. For the `j<sup>th</sup>` query, determine whether `grid[row_j][col_j]` is illuminated or not. After answering the `j<sup>th</sup>` query, **turn off** the lamp at `grid[row_j][col_j]` and its **8 adjacent lamps** if they exist. A lamp is adjacent if its cell shares either a side or corner with `grid[row_j][col_j]`.

Return _an array of integers_ `ans`,* where `ans[j]` should be `1` if the cell in the `j<sup>th</sup>` query was illuminated, or `0` if the lamp was not.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg)

```
Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
```

### Example 2:

```
Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]
```

### Example 3:

```
Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]
```

## Constraints

- 1 <= n <= 10^9
- 0 <= lamps.length <= 20000
- 0 <= queries.length <= 20000
- lamps[i].length == 2
- 0 <= row_i, col_i < n
- queries[j].length == 2
- 0 <= row_j, col_j < n
