# Reachable Nodes In Subdivided Graph

**Difficulty:** Hard
**Topics:** Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm
**Tags:**

**LeetCode:** [Problem 882](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/)

## Problem Description

You are given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to `n - 1`. You decide to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of `edges` where `edges[i] = [u<sub>i</sub>, v<sub>i</sub>, cnt<sub>i</sub>]` indicates that there is an edge between nodes `u<sub>i</sub>` and `v<sub>i</sub>` in the original graph, and `cnt<sub>i</sub>` is the total number of new nodes that you will **subdivide** the edge into. Note that `cnt<sub>i</sub> == 0` means you will not subdivide the edge.

To **subdivide** the edge `[u<sub>i</sub>, v<sub>i</sub>]`, replace it with `(cnt<sub>i</sub> + 1)` new edges and `cnt<sub>i</sub>` new nodes. The new nodes are `x<sub>1</sub>`, `x<sub>2</sub>`, ..., `x<sub>cnt<sub>i</sub></sub>`, and the new edges are `[u<sub>i</sub>, x<sub>1</sub>]`, `[x<sub>1</sub>, x<sub>2</sub>]`, `[x<sub>2</sub>, x<sub>3</sub>]`, ..., `[x<sub>cnt<sub>i</sub>-1</sub>, x<sub>cnt<sub>i</sub></sub>]`, `[x<sub>cnt<sub>i</sub></sub>, v<sub>i</sub>]`.

In this **new graph**, you want to know how many nodes are **reachable** from the node `0`, where a node is **reachable** if the distance is `maxMoves` or less.

Given the original graph and `maxMoves`, return _the number of nodes that are **reachable** from node *`0`* in the new graph_.

## Examples

### Example 1:

![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png)

```
Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.
```

### Example 2:

```
Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23
```

### Example 3:

```
Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.
```

## Constraints

- 0 <= edges.length <= min(n * (n - 1) / 2, 10<sup>4</sup>)
- edges[i].length == 3
- 0 <= u<sub>i</sub> < v<sub>i</sub> < n
- There are no multiple edges in the graph.
- 0 <= cnt<sub>i</sub> <= 10<sup>4</sup>
- 0 <= maxMoves <= 10<sup>9</sup>
- 1 <= n <= 3000
