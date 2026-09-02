# Encode N-ary Tree to Binary Tree

**Difficulty:** Hard
**Topics:** Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 431](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description/)

## Problem Description

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-ary tree structure.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.

For example, you may encode the following `3-ary` tree to a binary tree in this way: `Input: root = [1,null,3,2,4,null,5,6]`. Note that the above is just an example which _might or might not_ work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0431.Encode%20N-ary%20Tree%20to%20Binary%20Tree/images/narytreebinarytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

### Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

### Example 3:

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `0 <= Node.val <= 10^4`.
- The height of the n-ary tree is less than or equal to `1000`.
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
