# Convex Polygon

**Difficulty:** Medium
**Topics:** Geometry, Array, Math, Polygon
**Tags:**

**LeetCode:** [Problem 469](https://leetcode.com/problems/convex-polygon/description/)

## Problem Description

You are given an array of points on the **X-Y** plane `points` where `points[i] = [x_i, y_i]`. The points form a polygon when joined sequentially.

Return `true` if this polygon is [convex](http://en.wikipedia.org/wiki/Convex_polygon) and `false` otherwise.

You may assume the polygon formed by given points is always a [simple polygon](http://en.wikipedia.org/wiki/Simple_polygon). In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0469.Convex%20Polygon/images/covpoly1-plane.jpg)

```
Input: points = [[0,0],[0,5],[5,5],[5,0]]
Output: true
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0469.Convex%20Polygon/images/covpoly2-plane.jpg)

```
Input: points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
Output: false
```

## Constraints

- `3 <= points.length <= 10^4`
- `points[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- All the given points are **unique**.
