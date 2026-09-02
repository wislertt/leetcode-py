# Check if Grid can be Cut into Sections

**Difficulty:** Medium
**Topics:** Array, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 3394](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/)

## Problem Description

You are given an integer <code>n</code> representing the dimensions of an <code>n x n</code> grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates <code>rectangles</code>, where <code>rectangles[i]</code> is in the form <code>[start<sub>x</sub>, start<sub>y</sub>, end<sub>x</sub>, end<sub>y</sub>]</code>, representing a rectangle on the grid. Each rectangle is defined as follows:

- <code>(start<sub>x</sub>, start<sub>y</sub>)</code>: The bottom-left corner of the rectangle.
- <code>(end<sub>x</sub>, end<sub>y</sub>)</code>: The top-right corner of the rectangle.

<strong>Note </strong>that the rectangles do not overlap. Your task is to determine if it is possible to make <strong>either two horizontal or two vertical cuts</strong> on the grid such that:

- Each of the three resulting sections formed by the cuts contains <strong>at least</strong> one rectangle.
- Every rectangle belongs to <strong>exactly</strong> one section.

Return <code>true</code> if such cuts can be made; otherwise, return <code>false</code>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/10/23/tt1drawio.png)

```
Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
Output: true
```

**Explanation:** The grid is shown in the diagram. We can make horizontal cuts at <code>y = 2</code> and <code>y = 4</code>. Hence, the output is true.

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/10/23/tc2drawio.png)

```
Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
Output: true
```

**Explanation:** We can make vertical cuts at <code>x = 2</code> and <code>x = 3</code>. Hence, the output is true.

### Example 3:

```
Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
Output: false
```

**Explanation:** We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, the output is false.

## Constraints

- 3 <= n <= 10^9
- 3 <= rectangles.length <= 10^5
- 0 <= rectangles[i][0] < rectangles[i][2] <= n
- 0 <= rectangles[i][1] < rectangles[i][3] <= n
- No two rectangles overlap.
