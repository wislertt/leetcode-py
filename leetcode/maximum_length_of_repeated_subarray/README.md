# Maximum Length of Repeated Subarray

**Difficulty:** Medium
**Topics:** Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function
**Tags:**

**LeetCode:** [Problem 718](https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/)

## Problem Description

Given two integer arrays `nums1` and `nums2`, return _the maximum length of a subarray that appears in **both** arrays_.

## Examples

### Example 1:

```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

### Example 2:

```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
```

## Constraints

- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100
