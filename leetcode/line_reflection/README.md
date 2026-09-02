# Line Reflection

**Difficulty:** Medium
**Topics:** Array, Hash Table, Math
**Tags:** neetcode

**LeetCode:** [Problem 356](https://leetcode.com/problems/line-reflection/description/)

## Problem Description

Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

**Note** that there can be repeated points.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0356.Line%20Reflection/images/356_example_1.png)

```
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0356.Line%20Reflection/images/356_example_2.png)

```
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.
```

## Constraints

- `n == points.length`
- `1 <= n <= 10^4`
- `-10^8 <= points[i][j] <= 10^8`

**Follow up:** Could you do better than `O(n^2)`?
