# Path with Maximum Probability

**Difficulty:** Medium
**Topics:** Array, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm
**Tags:** neetcode

**LeetCode:** [Problem 1514](https://leetcode.com/problems/path-with-maximum-probability/description/)

## Problem Description

You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` is an undirected edge connecting the nodes `a<sub>i</sub>` and `b<sub>i</sub>` with a probability of success of traversing that edge `succProb[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

If there is no path from `start` to `end`, return `0`. Your answer will be accepted if it differs from the correct answer by at most **10<sup>-5</sup>**.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/09/20/1558_ex1.png)

```
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png)

```
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2019/09/20/1558_ex3.png)

```
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
```

## Constraints

- 2 <= n <= 10^4
- 0 <= start, end < n
- start != end
- 0 <= a<sub>i</sub>, b<sub>i</sub> < n
- a<sub>i</sub> != b<sub>i</sub>
- 0 <= succProb.length == edges.length <= 2 * 10^4
- 0 <= succProb[i] <= 1
- There is at most one edge between every two nodes.
