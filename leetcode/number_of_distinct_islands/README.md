# Number of Distinct Islands

**Difficulty:** Medium
**Topics:** Hash Table, Depth-First Search, Breadth-First Search, Union Find, Hash Function
**Tags:** neetcode

**LeetCode:** [Problem 694](https://leetcode.com/problems/number-of-distinct-islands/description/)

## Problem Description

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of **distinct** islands.

## Examples

### Example 1:

```
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
Explanation: Islands are all the same by translation.
```

### Example 2:

```
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
Explanation: Islands are all different.
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

**Follow up:** Could you generalize this to allow rotations and reflections?
