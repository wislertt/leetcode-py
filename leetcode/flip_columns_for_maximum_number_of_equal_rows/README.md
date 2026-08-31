# Flip Columns For Maximum Number of Equal Rows

**Difficulty:** Medium
**Topics:** Array, Hash Table, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 1072](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/)

## Problem Description

You are given an <code>m x n</code> binary matrix <code>matrix</code>.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from <code>0</code> to <code>1</code> or vice versa).

Return <em>the maximum number of rows that have all values equal after some number of flips</em>.

## Examples

### Example 1:

```
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
```

### Example 2:

```
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
```

### Example 3:

```
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
```

## Constraints

- <code>m == matrix.length</code>
- <code>n == matrix[i].length</code>
- <code>1 &lt;= m, n &lt;= 300</code>
- <code>matrix[i][j]</code> is either <code>0</code> or <code>1</code>.
