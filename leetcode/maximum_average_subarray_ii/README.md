# Maximum Average Subarray II

**Difficulty:** Hard
**Topics:** Array, Binary Search, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 644](https://leetcode.com/problems/maximum-average-subarray-ii/description/)

## Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is greater than or equal to** `k` that has the maximum average value and return _this value_. Any answer with a calculation error less than `10^-5` will be accepted.

## Examples

### Example 1:

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum average is 12.75. We do not consider subarrays of length < 4.
```

### Example 2:

```
Input: nums = [5], k = 1
Output: 5.00000
```

## Constraints

- n == nums.length
- 1 <= k <= n <= 10^4
- -10^4 <= nums[i] <= 10^4
