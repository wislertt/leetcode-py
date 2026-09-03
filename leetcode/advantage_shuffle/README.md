# Advantage Shuffle

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Greedy, Sorting
**Tags:**

**LeetCode:** [Problem 870](https://leetcode.com/problems/advantage-shuffle/description/)

## Problem Description

You are given two integer arrays `nums1` and `nums2` both of the same length. The **advantage** of `nums1` with respect to `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`.

Return _any_ permutation of `nums1` that maximizes its **advantage** with respect to `nums2`.

## Examples

### Example 1:

```
Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]
```

### Example 2:

```
Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
```

## Constraints

- `1 <= nums1.length <= 10^5`
- `nums2.length == nums1.length`
- `0 <= nums1[i], nums2[i] <= 10^9`

**Note:** Multiple permutations can achieve the maximum advantage, so any valid one is accepted. The tests assert that the result is a permutation of `nums1` that reaches the maximum possible advantage count.
