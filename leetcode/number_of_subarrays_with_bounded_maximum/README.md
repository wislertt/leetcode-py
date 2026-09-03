# Number of Subarrays with Bounded Maximum

**Difficulty:** Medium
**Topics:** Array, Two Pointers
**Tags:**

**LeetCode:** [Problem 795](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/)

## Problem Description

Given an integer array <code>nums</code> and two integers <code>left</code> and <code>right</code>, return <em>the number of contiguous non-empty <strong>subarrays</strong> such that the value of the maximum array element in that subarray is in the range</em> <code>[left, right]</code>.

The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.

## Examples

### Example 1:

```
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

### Example 2:

```
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= left <= right <= 10^9`
