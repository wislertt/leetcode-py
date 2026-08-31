# Delete Nodes And Return Forest

**Difficulty:** Medium
**Topics:** Array, Hash Table, Tree, Depth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 1110](https://leetcode.com/problems/delete-nodes-and-return-forest/description/)

## Problem Description

Given the <code>root</code> of a binary tree, each node in the tree has a <strong>distinct</strong> value.

After deleting all nodes with a value in <code>to_delete</code>, we are left with a forest (a&nbsp;disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return them in any order.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)

```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

### Example 2:

```
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
```

## Constraints

- The number of nodes in the given tree is at most <code>1000</code>.
- Each node has a <strong>distinct</strong> value between <code>1</code> and <code>1000</code>.
- <code>to_delete.length &lt;= 1000</code>
- <code>to_delete</code> contains distinct values between <code>1</code> and <code>1000</code>.
