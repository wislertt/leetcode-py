# Minimum Time to Collect All Apples in a Tree

**Difficulty:** Medium
**Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, DP on Trees
**Tags:** neetcode

**LeetCode:** [Problem 1443](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/)

## Problem Description

Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. _Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at **vertex 0** and coming back to this vertex._

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` means that exists an edge connecting the vertices `a<sub>i</sub>` and `b<sub>i</sub>`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, it does not have any apple.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png)

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png)

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 3:

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
```

## Constraints

- 1 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= a<sub>i</sub> < b<sub>i</sub> <= n - 1
- hasApple.length == n
