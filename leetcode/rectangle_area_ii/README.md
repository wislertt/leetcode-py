# Rectangle Area II

**Difficulty:** Hard
**Topics:** Array, Segment Tree, Sweep Line, Ordered Set
**Tags:**

**LeetCode:** [Problem 850](https://leetcode.com/problems/rectangle-area-ii/description/)

## Problem Description

You are given a 2D array of axis-aligned rectangles. Each `rectangle[i] = [xi1, yi1, xi2, yi2]` denotes the ith rectangle where `(xi1, yi1)` are the coordinates of the bottom-left corner, and `(xi2, yi2)` are the coordinates of the top-right corner.

Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

Return the total area. Since the answer may be too large, return it modulo `10^9 + 7`.

## Examples

### Example 1:

![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)

```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
```

### Example 2:

```
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.
```

## Constraints

- 1 <= rectangles.length <= 200
- rectangles[i].length == 4
- 0 <= xi1, yi1, xi2, yi2 <= 10^9
- xi1 <= xi2
- yi1 <= yi2
- All rectangles have non zero area.
