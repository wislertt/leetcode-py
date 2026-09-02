# Create Maximum Number

**Difficulty:** Hard
**Topics:** Array, Two Pointers, Stack, Greedy, Monotonic Stack
**Tags:**

**LeetCode:** [Problem 321](https://leetcode.com/problems/create-maximum-number/description/)

## Problem Description

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. `nums1` and `nums2` represent the digits of two numbers. You are also given an integer `k`.

Create the maximum number of length `k <= m + n` from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the `k` digits representing the answer.

## Examples

### Example 1:

```
Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
```

### Example 2:

```
Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]
```

### Example 3:

```
Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]
```

## Constraints

- `m == nums1.length`
- `n == nums2.length`
- `1 <= m, n <= 500`
- `0 <= nums1[i], nums2[i] <= 9`
- `1 <= k <= m + n`
- `nums1` and `nums2` do not have leading zeros.
