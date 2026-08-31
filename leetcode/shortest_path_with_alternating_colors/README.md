# Shortest Path with Alternating Colors

**Difficulty:** Medium
**Topics:** Breadth-First Search, Graph
**Tags:** neetcode

**LeetCode:** [Problem 1129](https://leetcode.com/problems/shortest-path-with-alternating-colors/description/)

## Problem Description

You are given an integer <code>n</code>, the number of nodes in a directed graph where the nodes are labeled from <code>0</code> to <code>n - 1</code>. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays <code>redEdges</code> and <code>blueEdges</code> where:

- <code>redEdges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is a directed red edge from node <code>a<sub>i</sub></code> to node <code>b<sub>i</sub></code> in the graph, and
- <code>blueEdges[j] = [u<sub>j</sub>, v<sub>j</sub>]</code> indicates that there is a directed blue edge from node <code>u<sub>j</sub></code> to node <code>v<sub>j</sub></code> in the graph.

Return an array <code>answer</code> of length <code>n</code>, where each <code>answer[x]</code> is the length of the shortest path from node <code>0</code> to node <code>x</code> such that the edge colors alternate along the path, or <code>-1</code> if such a path does not exist.

## Examples

### Example 1:

```
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
```

### Example 2:

```
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
```

## Constraints

- <code>1 &lt;= n &lt;= 100</code>
- <code>0 &lt;= redEdges.length,&nbsp;blueEdges.length &lt;= 400</code>
- <code>redEdges[i].length == blueEdges[j].length == 2</code>
- <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub>, u<sub>j</sub>, v<sub>j</sub> &lt; n</code>
