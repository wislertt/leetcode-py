# Validate Binary Tree Nodes

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Union Find, Graph
**Tags:** neetcode

**LeetCode:** [Problem 1361](https://leetcode.com/problems/validate-binary-tree-nodes/description/)

## Problem Description

You have <code>n</code> binary tree nodes numbered from <code>0</code> to <code>n - 1</code> where node <code>i</code> has two children <code>leftChild[i]</code> and <code>rightChild[i]</code>, return <code>true</code> if and only if all the given nodes form <strong>exactly one valid binary tree</strong>.

If node <code>i</code> has no left child then <code>leftChild[i]</code> will equal <code>-1</code>, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

## Examples

### Example 1:

```
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
```

### Example 2:

```
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
```

### Example 3:

```
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
```

## Constraints

- n == leftChild.length == rightChild.length
- 1 <= n <= 10^4
- -1 <= leftChild[i], rightChild[i] <= n - 1
