# Sum of Subarray Minimums

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming, Stack, Monotonic Stack
**Tags:** neetcode

**LeetCode:** [Problem 907](https://leetcode.com/problems/sum-of-subarray-minimums/description/)

## Problem Description

Given an array of integers <code>arr</code>, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.

## Examples

### Example 1:

```
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum is 17.
```

### Example 2:

```
Input: arr = [50]
Output: 50
```

## Constraints

- 1 <= arr.length <= 3 * 10^4
- 1 <= arr[i] <= 3 * 10^4
