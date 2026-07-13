# N-Queens

**Difficulty:** Hard
**Topics:** Array, Backtracking
**Tags:** grind, neetcode-150, neetcode-250

**LeetCode:** [Problem 51](https://leetcode.com/problems/n-queens/description/)

## Problem Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

### Example 2:

```
Input: n = 1
Output: [["Q"]]
```

## Constraints

- 1 <= n <= 9
