# Perfect Rectangle

**Difficulty:** Hard
**Topics:** Array, Hash Table, Math, Geometry, Sweep Line
**Tags:**

**LeetCode:** [Problem 391](https://leetcode.com/problems/perfect-rectangle/description/)

## Problem Description

Given an array `rectangles` where `rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]` represents an axis-aligned rectangle. The bottom-left point of the rectangle is `(x<sub>i</sub>, y<sub>i</sub>)` and the top-right point of it is `(a<sub>i</sub>, b<sub>i</sub>)`.

Return `true` _if all the rectangles together form an exact cover of a rectangular region_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg)

```
Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg)

```
Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg)

```
Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.
```

## Constraints

- 1 <= rectangles.length <= 2 * 10^4
- rectangles[i].length == 4
- -10^5 <= xi < ai <= 10^5
- -10^5 <= yi < bi <= 10^5
