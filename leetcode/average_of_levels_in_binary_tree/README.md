# Average of Levels in Binary Tree

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Tags:**

**LeetCode:** [Problem 637](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)

## Problem Description

Given the `root` of a binary tree, return <em>the average value of the nodes on each level in the form of an array</em>. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

## Constraints

- The number of nodes in the tree is in the range [1, 10<sup>4</sup>]
- -2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1
