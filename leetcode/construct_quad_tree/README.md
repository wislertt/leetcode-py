# Construct Quad Tree

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Tree, Matrix
**Tags:** neetcode-250

**LeetCode:** [Problem 427](https://leetcode.com/problems/construct-quad-tree/description/)

## Problem Description

Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent `grid` with a Quad-Tree.

Return _the root of the Quad-Tree representing `grid`_.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

- `val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the `val` to True or False when `isLeaf` is False, and both are accepted in the answer.
- `isLeaf`: True if the node is a leaf node on the tree or False if the node has four children.

```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

We can construct a Quad-Tree from a two-dimensional area using the following steps:

1. If the current grid has the same value (i.e all `1's` or all `0's`) set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.

**Quad-Tree format:** The output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below. The node is represented as a list `[isLeaf, val]`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/02/11/grid1.png)

```
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The root is not a leaf. Its four children (top-left, top-right, bottom-left, bottom-right) are leaves.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2020/02/12/e2mat.png)

```
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
```

## Constraints

- n == grid.length == grid[i].length
- n == 2^x where 0 <= x <= 6
