# Largest Sum of Averages

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Prefix Sum
**Tags:**

**LeetCode:** [Problem 813](https://leetcode.com/problems/largest-sum-of-averages/description/)

## Problem Description

You are given an integer array `nums` and an integer `k`. You can partition the array into at most `k` non-empty adjacent subarrays. The **score** of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in `nums`, and that the score is not necessarily an integer.

Return the maximum **score** you can achieve of all the possible partitions. Answers within `10^-6` of the actual answer will be accepted.

## Examples

### Example 1:

```
Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation: The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
```

### Example 2:

```
Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000
```

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`
