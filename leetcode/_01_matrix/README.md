# 01 Matrix

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Breadth-First Search, Matrix
**Tags:** grind-75

**LeetCode:** [Problem 542](https://leetcode.com/problems/-01-matrix/description/)


## Problem Description

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

&nbsp;
Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]


Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


&nbsp;
Constraints:


	m == mat.length
	n == mat[i].length
	1 &lt;= m, n &lt;= 104
	1 &lt;= m * n &lt;= 104
	mat[i][j] is either 0 or 1.
	There is at least one 0 in mat.


&nbsp;
Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

## Examples

## Constraints

- m == mat.length
- n == mat[i].length
- 1 &lt;= m, n &lt;= 104
- 1 &lt;= m * n &lt;= 104
- mat[i][j] is either 0 or 1.
- There is at least one 0 in mat.


