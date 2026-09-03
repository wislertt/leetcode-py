# Path Sum IV

**Difficulty:** Medium
**Topics:** Array, Hash Table, Tree, Depth-First Search, Binary Tree
**Tags:**

**LeetCode:** [Problem 666](https://leetcode.com/problems/path-sum-iv/description/)

## Problem Description

If the depth of a tree is smaller than `5`, then this tree can be represented by an array of three-digit integers. You are given an **ascending** array `nums` consisting of three-digit integers representing a binary tree with a depth smaller than `5`, where for each integer:

- The hundreds digit represents the depth `d` of this node, where `1 <= d <= 4`.
- The tens digit represents the position `p` of this node within its level, where `1 <= p <= 8`, corresponding to its position in a **full binary tree**.
- The units digit represents the value `v` of this node, where `0 <= v <= 9`.

Return the **sum** of all **paths** from the **root** towards the **leaves**.

It is **guaranteed** that the given array represents a valid connected binary tree.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0666.Path%20Sum%20IV/images/pathsum4-1-tree.jpg)

```
Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown. The path sum is (3 + 5) + (3 + 1) = 12.
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0666.Path%20Sum%20IV/images/pathsum4-2-tree.jpg)

```
Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown. The path sum is (3 + 1) = 4.
```

## Constraints

- 1 <= nums.length <= 15
- 110 <= nums[i] <= 489
- nums represents a valid binary tree with depth less than 5.
- nums is sorted in ascending order.
