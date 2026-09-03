# Minimum Area Rectangle

**Difficulty:** Medium
**Topics:** Array, Hash Table, Math, Geometry, Sorting
**Tags:**

**LeetCode:** [Problem 939](https://leetcode.com/problems/minimum-area-rectangle/description/)

## Problem Description

You are given an array of points in the **X-Y** plane `points` where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]`.

Return _the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes_. If there is not any such rectangle, return `0`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Explanation: The minimum area rectangle is shown in the image, with an area of 2 * 2 = 4.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
Explanation: The minimum area rectangle is shown in the image, with an area of 1 * 2 = 2.
```

## Constraints

- 1 <= points.length <= 500
- points[i].length == 2
- 0 <= xi, yi <= 4 * 10^4
- All the given points are unique.
