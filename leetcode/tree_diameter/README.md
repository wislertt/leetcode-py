# Tree Diameter

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Graph, Topological Sort
**Tags:** neetcode

**LeetCode:** [Problem 1245](https://leetcode.com/problems/tree-diameter/description/)

## Problem Description

The **diameter** of a tree is **the number of edges** in the longest path in that tree.

There is an undirected tree of `n` nodes labeled from `0` to `n - 1`. You are given a 2D array `edges` where `edges.length == n - 1` and `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the tree.

Return **the diameter** of the tree.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1245.Tree%20Diameter/images/tree1.jpg)

```
Input: edges = [[0,1],[0,2]]
Output: 2
```

**Explanation:** The longest path of the tree is the path 1 - 0 - 2.

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1245.Tree%20Diameter/images/tree2.jpg)

```
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
```

**Explanation:** The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

## Constraints

- `n == edges.length + 1`
- `1 <= n <= 10^4`
- `0 <= ai, bi < n`
- `ai != bi`
