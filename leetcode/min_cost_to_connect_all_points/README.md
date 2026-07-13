# Min Cost to Connect All Points

**Difficulty:** Medium
**Topics:** Array, Union-Find, Graph Theory, Minimum Spanning Tree
**Tags:** algo-master-75, neetcode-150, neetcode-250

**LeetCode:** [Problem 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

## Problem Description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected_. All points are connected if there is **exactly one** simple path between any two points.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
![Example 1 solution](https://assets.leetcode.com/uploads/2020/08/26/c.png)
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

### Example 2:

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.
