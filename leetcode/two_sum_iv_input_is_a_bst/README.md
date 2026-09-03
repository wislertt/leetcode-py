# Two Sum IV - Input is a BST

**Difficulty:** Easy
**Topics:** Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
**Tags:**

**LeetCode:** [Problem 653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)

## Problem Description

<p>Given the <code>root</code> of a binary search tree and an integer <code>k</code>, return <code>true</code> <em>if there exist two elements in the BST such that their sum is equal to</em> <code>k</code>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```

## Constraints

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10^4]</code>.</li>
	<li><code>-10^4 &lt;= Node.val &lt;= 10^4</code></li>
	<li><code>root</code> is guaranteed to be a <strong>valid</strong> binary search tree.</li>
	<li><code>-10^5 &lt;= k &lt;= 10^5</code></li>
</ul>
