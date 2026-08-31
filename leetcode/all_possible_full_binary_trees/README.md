# All Possible Full Binary Trees

**Difficulty:** Medium
**Topics:** Dynamic Programming, Tree, Recursion, Memoization, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 894](https://leetcode.com/problems/all-possible-full-binary-trees/description/)

## Problem Description

Given an integer <code>n</code>, return <em>a list of all possible <strong>full binary trees</strong> with</em> <code>n</code> <em>nodes</em>. Each node of each tree in the answer must have <code>Node.val == 0</code>.</p>

<p>Each element of the answer is the root node of one possible tree. You may return the final list of trees in <strong>any order</strong>.</p>

<p>A <strong>full binary tree</strong> is a binary tree where each node has exactly <code>0</code> or <code>2</code> children.</p>

## Examples

### Example 1:

```
Input: n = 7
Output: [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,0,0,None,None,0,0],[0,0,0,0,0,None,None,0,0],[0,0,0,0,0,0,0]]
```

### Example 2:

```
Input: n = 3
Output: [[0,0,0]]
```

## Constraints

- 1 <= n <= 20
