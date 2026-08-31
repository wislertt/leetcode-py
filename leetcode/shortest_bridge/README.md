# Shortest Bridge

**Difficulty:** Medium
**Topics:** Array, Depth-First Search, Breadth-First Search, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 934](https://leetcode.com/problems/shortest-bridge/description/)

## Problem Description

<p>You are given an <code>n x n</code> binary matrix <code>grid</code> where <code>1</code> represents land and <code>0</code> represents water.</p>

<p>An island is a 4-directionally connected group of <code>1</code>&#39;s not connected to any other <code>1</code>&#39;s. There are <strong>exactly two islands</strong> in <code>grid</code>.</p>

<p>You may change <code>0</code>&#39;s to <code>1</code>&#39;s to connect the two islands to form <strong>one island</strong>.</p>

<p>Return <em>the smallest number of </em><code>0</code><em>&#39;s you must flip to connect the two islands</em>.</p>

## Examples

### Example 1:

```
Input: grid = [[0,1],[1,0]]
Output: 1
```

### Example 2:

```
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

### Example 3:

```
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

## Constraints

- n == grid.length == grid[i].length
- 2 &lt;= n &lt;= 100
- grid[i][j] is either 0 or 1.
- There are exactly two islands in grid.
