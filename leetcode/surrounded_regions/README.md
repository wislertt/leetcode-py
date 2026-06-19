# Surrounded Regions

**Difficulty:** Medium
**Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
**Tags:** neetcode-150

**LeetCode:** [Problem 130](https://leetcode.com/problems/surrounded-regions/description/)

## Problem Description

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.
- **Region**: To form a region connect every `'O'` cell.
- **Surround**: A region is surrounded if none of the `'O'` cells in the region are on the edge of the `board`. Such regions are completely enclosed by `'X'` cells.

To capture a surrounded region, replace all `'O'`s with `'X'`s **in-place** within the original `board`. You do not need to return anything.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if it is on the border of the board.
```

### Example 2:

```
Input: board = [["X"]]
Output: [["X"]]
```

## Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.
