# Create Binary Tree From Descriptions

**Difficulty:** Medium
**Topics:** Array, Hash Table, Tree, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 2196](https://leetcode.com/problems/create-binary-tree-from-descriptions/description/)

## Problem Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent<sub>i</sub>, child<sub>i</sub>, isLeft<sub>i</sub>]` indicates that `parent<sub>i</sub>` is the **parent** of `child<sub>i</sub>` in a **binary** tree of **unique** values. Furthermore,

- If `isLeft<sub>i</sub> == 1`, then `child<sub>i</sub>` is the left child of `parent<sub>i</sub>`.
- If `isLeft<sub>i</sub> == 0`, then `child<sub>i</sub>` is the right child of `parent<sub>i</sub>`.

Construct the binary tree described by `descriptions` and return its **root**.

The test cases will be generated such that the binary tree is **valid**.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png)

```
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png)

```
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
```

## Constraints

- 1 <= descriptions.length <= 10^4
- descriptions[i].length == 3
- 1 <= parent<sub>i</sub>, child<sub>i</sub> <= 10^5
- 0 <= isLeft<sub>i</sub> <= 1
- The binary tree described by descriptions is valid.
