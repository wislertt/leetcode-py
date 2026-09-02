# Maximal Rectangle

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
**Tags:**

**LeetCode:** [Problem 85](https://leetcode.com/problems/maximal-rectangle/description/)

## Problem Description

Given a <code>rows x cols</code> binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and return <em>its area</em>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

### Example 2:

```
Input: matrix = [["0"]]
Output: 0
```

### Example 3:

```
Input: matrix = [["1"]]
Output: 1
```

## Constraints

- rows == matrix.length
- cols == matrix[i].length
- 1 <= rows, cols <= 200
- matrix[i][j] is '0' or '1'.
