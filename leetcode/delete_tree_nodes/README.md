# Delete Tree Nodes

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Array, Tree DP
**Tags:**

**LeetCode:** [Problem 1273](https://leetcode.com/problems/delete-tree-nodes/description/)

## Problem Description

A tree rooted at node 0 is given as follows:

<ul>
	<li>The number of nodes is <code>nodes</code>;</li>
	<li>The value of the <code>i<sup>th</sup></code> node is <code>value[i]</code>;</li>
	<li>The parent of the <code>i<sup>th</sup></code> node is <code>parent[i]</code>.</li>
</ul>

<p>Remove every subtree whose sum of values of nodes is zero.</p>

<p>Return <em>the number of the remaining nodes in the tree</em>.</p>

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1273.Delete%20Tree%20Nodes/images/1421_sample_1.png)

```
Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
```

### Example 2:

```
Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
Output: 6
```

## Constraints

- 1 <= nodes <= 10^4
- parent.length == nodes
- 0 <= parent[i] <= nodes - 1
- parent[0] == -1 which indicates that 0 is the root.
- value.length == nodes
- -10^5 <= value[i] <= 10^5
- The given input is <strong>guaranteed</strong> to represent a <strong>valid tree</strong>.
