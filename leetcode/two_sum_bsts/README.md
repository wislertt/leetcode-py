# Two Sum BSTs

**Difficulty:** Medium
**Topics:** Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Search, Binary Tree
**Tags:** neetcode

**LeetCode:** [Problem 1214](https://leetcode.com/problems/two-sum-bsts/description/)

## Problem Description

<p>Given the roots of two binary search trees, <code>root1</code> and <code>root2</code>, return <code>true</code> if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer <code>target</code>.</p>

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex1.png)

```
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1214.Two%20Sum%20BSTs/images/ex2.png)

```
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
```

## Constraints

- The number of nodes in each tree is in the range [1, 5000].
- -10^9 <= Node.val, target <= 10^9.
