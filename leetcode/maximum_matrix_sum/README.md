# Maximum Matrix Sum

**Difficulty:** Medium
**Topics:** Array, Greedy, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 1975](https://leetcode.com/problems/maximum-matrix-sum/description/)

## Problem Description

You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:

- Choose any two **adjacent** elements of `matrix` and **multiply** each of them by `-1`.

Two elements are considered **adjacent** if and only if they share a **border**.

Your goal is to **maximize** the summation of the matrix's elements. Return _the **maximum** sum of the matrix's elements using the operation mentioned above._

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png)

```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png)

```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `2 <= n <= 250`
- `-10^5 <= matrix[i][j] <= 10^5`
