# Divide Array Into Increasing Sequences

**Difficulty:** Hard
**Topics:** Array, Greedy
**Tags:**

**LeetCode:** [Problem 1121](https://leetcode.com/problems/divide-array-into-increasing-sequences/description/)

## Problem Description

Given an integer array `nums` sorted in **non-decreasing** order and an integer `k`, return `true` if this array can be divided into one or more disjoint **increasing** subsequences of length at least `k`, or `false` otherwise.

## Examples

### Example 1:

```
Input: nums = [1,2,2,3,3,4,4], k = 3
Output: true
Explanation: The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
```

### Example 2:

```
Input: nums = [5,6,6,7,8], k = 3
Output: false
Explanation: There is no way to divide the array using the conditions required.
```

## Constraints

- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- nums is sorted in non-decreasing order.
