# Find Leaves of Binary Tree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 366](https://leetcode.com/problems/find-leaves-of-binary-tree/description/)

## Problem Description

Given the `root` of a binary tree, collect a tree's nodes as if you were doing this:

- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0366.Find%20Leaves%20of%20Binary%20Tree/images/remleaves-tree.jpg)

```
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
```

### Example 2:

```
Input: root = [1]
Output: [[1]]
```

## Constraints

- The number of nodes in the tree is in the range `[1, 100]`.
- `-100 <= Node.val <= 100`
