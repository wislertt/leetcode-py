# Largest Color Value in a Directed Graph

**Difficulty:** Hard
**Topics:** Hash Table, String, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Counting, Directed Acyclic Graph
**Tags:** neetcode

**LeetCode:** [Problem 1857](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/)

## Problem Description

There is a <strong>directed graph</strong> of <code>n</code> colored nodes and <code>m</code> edges. The nodes are numbered from <code>0</code> to <code>n - 1</code>.

You are given a string <code>colors</code> where <code>colors[i]</code> is a lowercase English letter representing the <strong>color</strong> of the <code>i<sup>th</sup></code> node in this graph (<strong>0-indexed</strong>). You are also given a 2D array <code>edges</code> where <code>edges[j] = [a<sub>j</sub>, b<sub>j</sub>]</code> indicates that there is a <strong>directed edge</strong> from node <code>a<sub>j</sub></code> to node <code>b<sub>j</sub></code>.

A valid <strong>path</strong> in the graph is a sequence of nodes <code>x<sub>1</sub> -&gt; x<sub>2</sub> -&gt; x<sub>3</sub> -&gt; ... -&gt; x<sub>k</sub></code> such that there is a directed edge from <code>x<sub>i</sub></code> to <code>x<sub>i+1</sub></code> for every <code>1 &lt;= i &lt; k</code>. The <strong>color value</strong> of the path is the number of nodes that are colored the <strong>most frequently</strong> occurring color along that path.

Return <em>the <strong>largest color value</strong> of any valid path in the given graph, or </em><code>-1</code><em> if the graph contains a cycle</em>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/21/leet1.png)

```
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
```

**Explanation:** The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored `"a" (red in the above image)`.

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/04/21/leet2.png)

```
Input: colors = "a", edges = [[0,0]]
Output: -1
```

**Explanation:** There is a cycle from 0 to 0.

## Constraints

- `n == colors.length`
- `m == edges.length`
- `1 <= n <= 10^5`
- `0 <= m <= 10^5`
- `colors` consists of lowercase English letters.
- `0 <= aj, bj < n`
