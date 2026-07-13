# Split Array Largest Sum

**Difficulty:** Hard
**Topics:** Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum
**Tags:** neetcode-250

**LeetCode:** [Problem 410](https://leetcode.com/problems/split-array-largest-sum/description/)

## Problem Description

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is **minimized**.

Return _the minimized largest sum of the split_.

A **subarray** is a contiguous part of the array.

## Examples

### Example 1:

```
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
```

### Example 2:

```
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
```

## Constraints

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= k <= min(50, nums.length)
