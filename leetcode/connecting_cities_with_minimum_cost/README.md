# Connecting Cities With Minimum Cost

**Difficulty:** Medium
**Topics:** Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)
**Tags:**

**LeetCode:** [Problem 1135](https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/)

## Problem Description

There are `n` cities labeled from `1` to `n`. You are given the integer `n` and an array `connections` where `connections[i] = [xi, yi, costi]` indicates that the cost of connecting city `xi` and city `yi` (bidirectional connection) is `costi`.

Return _the minimum **cost** to connect all the_ `n` _cities such that there is at least one path between each pair of cities_. If it is impossible to connect all the `n` cities, return `-1`.

The **cost** is the sum of the connections' costs used.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1135.Connecting%20Cities%20With%20Minimum%20Cost/images/1314_ex2.png)

```
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1135.Connecting%20Cities%20With%20Minimum%20Cost/images/1314_ex1.png)

```
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
```

## Constraints

- 1 <= n <= 10^4
- 1 <= connections.length <= 10^4
- connections[i].length == 3
- 1 <= xi, yi <= n
- xi != yi
- 0 <= costi <= 10^5
