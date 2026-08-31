# Range Sum of BST

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 938](https://leetcode.com/problems/range-sum-of-bst/description/)

## Problem Description

<p>Given the <code>root</code> node of a binary search tree and two integers <code>low</code> and <code>high</code>, return <em>the sum of values of all nodes with a value in the <strong>inclusive</strong> range </em><code>[low, high]</code>.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg)

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

## Constraints

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2 * 10^4]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10^5</code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 10^5</code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
</ul>
