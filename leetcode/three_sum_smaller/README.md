# 3Sum Smaller

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 259](https://leetcode.com/problems/three-sum-smaller/description/)

## Problem Description

Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

## Examples

### Example 1:

```
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
```

### Example 2:

```
Input: nums = [], target = 0
Output: 0
```

### Example 3:

```
Input: nums = [0], target = 0
Output: 0
```

## Constraints

- `n == nums.length`
- `0 <= n <= 3500`
- `-100 <= nums[i] <= 100`
- `-100 <= target <= 100`
- The input is generated such that the answer is less than or equal to `10^9`.
