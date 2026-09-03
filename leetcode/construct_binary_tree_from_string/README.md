# Construct Binary Tree from String

**Difficulty:** Medium
**Topics:** Stack, Tree, Depth-First Search, String, Binary Tree
**Tags:**

**LeetCode:** [Problem 536](https://leetcode.com/problems/construct-binary-tree-from-string/description/)

## Problem Description

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the **left** child node of the parent first if it exists.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0536.Construct%20Binary%20Tree%20from%20String/images/butree.jpg)

```
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
```

### Example 2:

```
Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
```

### Example 3:

```
Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
```

## Constraints

- 0 <= s.length <= 3 * 10^4
- s consists of digits, '(', ')', and '-' only.
- All numbers in the tree have value at most than 2^30.
