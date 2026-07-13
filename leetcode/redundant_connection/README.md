# Redundant Connection

**Difficulty:** Medium
**Topics:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
**Tags:** neetcode-150, neetcode-250

**LeetCode:** [Problem 684](https://leetcode.com/problems/redundant-connection/description/)

## Problem Description

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the graph.

Return _an edge that can be removed so that the resulting graph is a tree of_ `n` _nodes_. If there are multiple answers, return the answer that occurs last in the input.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg)

```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Constraints

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= a<sub>i</sub> < b<sub>i</sub> <= edges.length
- a<sub>i</sub> != b<sub>i</sub>
- There are no repeated edges.
- The given graph is connected.
