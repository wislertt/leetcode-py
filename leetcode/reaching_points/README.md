# Reaching Points

**Difficulty:** Hard
**Topics:** Math, Euclidean Algorithm, Greatest Common Divisor
**Tags:**

**LeetCode:** [Problem 780](https://leetcode.com/problems/reaching-points/description/)

## Problem Description

Given four integers `sx`, `sy`, `tx`, and `ty`, return `true` if it is possible to convert the point `(sx, sy)` to the point `(tx, ty)` through some operations, or `false` otherwise.

The allowed operation on some point `(x, y)` is to convert it to either `(x, x + y)` or `(x + y, y)`.

## Examples

### Example 1:

```
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

### Example 2:

```
Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
```

### Example 3:

```
Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
```

## Constraints

- 1 <= sx, sy, tx, ty <= 10^9
