# Smallest Rectangle Enclosing Black Pixels

**Difficulty:** Hard
**Topics:** Depth-First Search, Breadth-First Search, Array, Binary Search, Matrix
**Tags:**

**LeetCode:** [Problem 302](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/)

## Problem Description

You are given an `m x n` binary matrix `image` where `0` represents a white pixel and `1` represents a black pixel.

The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

Given two integers `x` and `y` that represents the location of one of the black pixels, return _the area of the smallest (axis-aligned) rectangle that encloses all black pixels_.

You must write an algorithm with less than `O(mn)` runtime complexity.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0302.Smallest%20Rectangle%20Enclosing%20Black%20Pixels/images/pixel-grid.jpg)

```
Input: image = [["0010"],["0110"],["0100"]], x = 0, y = 2
Output: 6
```

### Example 2:

```
Input: image = [["1"]], x = 0, y = 0
Output: 1
```

## Constraints

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 100`
- `image[i][j]` is either `'0'` or `'1'`.
- `0 <= x < m`
- `0 <= y < n`
- `image[x][y] == '1'`.
- The black pixels in the `image` only form **one component**.
