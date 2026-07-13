# Delete Node in a BST

**Difficulty:** Medium
**Topics:** Tree, Binary Search Tree, Binary Tree
**Tags:** neetcode-250

**LeetCode:** [Problem 450](https://leetcode.com/problems/delete-node-in-a-bst/description/)

## Problem Description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return _the **root node reference** (possibly updated) of the BST_.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

Note: When a node with two children is deleted, replacing it with either its inorder successor or predecessor is accepted.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg)

```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: One valid answer is [5,4,6,2,null,null,7]; [5,2,6,null,4,null,7] is also accepted.
```

### Example 2:

```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

### Example 3:

```
Input: root = [], key = 0
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.
- `root` is a valid binary search tree.
- -10^5 <= key <= 10^5

**Follow up:** Could you solve it with time complexity O(height of tree)?
