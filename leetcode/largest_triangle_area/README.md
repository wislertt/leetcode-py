# Largest Triangle Area

**Difficulty:** Easy
**Topics:** Array, Math, Geometry, Polygons
**Tags:**

**LeetCode:** [Problem 812](https://leetcode.com/problems/largest-triangle-area/description/)

## Problem Description

Given an array of points on the X-Y plane `points` where `points[i] = [xi, yi]`, return _the area of the largest triangle that can be formed by any three different points_. Answers within `10^-5` of the actual answer will be accepted.

## Examples

### Example 1:

![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

```
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
```

### Example 2:

```
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
```

## Constraints

- 3 <= points.length <= 50
- -50 <= xi, yi <= 50
- All the given points are unique.
