# Redundant Connection II

**Difficulty:** Hard
**Topics:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
**Tags:**

**LeetCode:** [Problem 685](https://leetcode.com/problems/redundant-connection-ii/description/)

## Problem Description

In this problem, a rooted tree is a **directed** graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with `n` nodes (with distinct values from `1` to `n`), with one additional directed edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair [u<sub>i</sub>, v<sub>i</sub>] that represents a **directed** edge connecting nodes u<sub>i</sub> and v<sub>i</sub>, where u<sub>i</sub> is a parent of child v<sub>i</sub>.

Return _an edge that can be removed so that the resulting graph is a rooted tree of_ `n` _nodes_. If there are multiple answers, return the answer that occurs last in the given 2D-array.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg)

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg)

```
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
```

## Constraints

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= u<sub>i</sub>, v<sub>i</sub> <= n
- u<sub>i</sub> != v<sub>i</sub>
