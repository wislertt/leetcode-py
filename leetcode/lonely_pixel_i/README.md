# Lonely Pixel I

**Difficulty:** Medium
**Topics:** Array, Hash Table, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 531](https://leetcode.com/problems/lonely-pixel-i/description/)

## Problem Description

Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels, return the number of **black** lonely pixels.

A black lonely pixel is a character `'B'` located at a specific position where the same row and same column don't have **any other** black pixels.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0531.Lonely%20Pixel%20I/images/pixel1.jpg)

```
Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
```

### Example 2:

```
Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
Output: 0
```

## Constraints

- `m == picture.length`
- `n == picture[i].length`
- `1 <= m, n <= 500`
- `picture[i][j]` is `'W'` or `'B'`.
