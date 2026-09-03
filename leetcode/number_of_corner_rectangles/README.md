# Number Of Corner Rectangles

**Difficulty:** Medium
**Topics:** Array, Math, Dynamic Programming, Matrix
**Tags:**

**LeetCode:** [Problem 750](https://leetcode.com/problems/number-of-corner-rectangles/description/)

## Problem Description

Given an `m x n` integer matrix `grid` where each entry is only `0` or `1`, return the number of **corner rectangles**.

A **corner rectangle** is four distinct `1`'s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value `1`. Also, all four `1`'s used must be distinct.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec1-grid.jpg)

```
Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec2-grid.jpg)

```
Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
```

### Example 3:

![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0750.Number%20Of%20Corner%20Rectangles/images/cornerrec3-grid.jpg)

```
Input: grid = [[1,1,1,1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is either 0 or 1.
- The number of 1's in the grid is in the range [1, 6000].
