# Sum of Distances in Tree

**Difficulty:** Hard
**Topics:** Dynamic Programming, Tree, Depth-First Search, Graph Theory, DP on Trees
**Tags:**

**LeetCode:** [Problem 834](https://leetcode.com/problems/sum-of-distances-in-tree/description/)

## Problem Description

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `i<sup>th</sup>` node in the tree and all other nodes.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

```
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg)

```
Input: n = 1, edges = []
Output: [0]
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)

```
Input: n = 2, edges = [[1,0]]
Output: [1,1]
```

## Constraints

- 1 <= n <= 3 * 10^4
- edges.length == n - 1
- edges[i].length == 2
- 0 <= a<sub>i</sub>, b<sub>i</sub> < n
- a<sub>i</sub> != b<sub>i</sub>
- The given input represents a valid tree.
