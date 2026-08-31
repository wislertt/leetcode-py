# Find All Duplicates in an Array

**Difficulty:** Medium
**Topics:** Array, Hash Table, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 442](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)

## Problem Description

Given an integer array `nums` of length `n` where all the integers of `nums` are in the range `[1, n]` and each integer appears **at most** **twice**, return _an array of all the integers that appears **twice**_.

You must write an algorithm that runs in `O(n)` time and uses only _constant_ auxiliary space, excluding the space needed to store the output

## Examples

### Example 1:

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

### Example 2:

```
Input: nums = [1,1,2]
Output: [1]
```

### Example 3:

```
Input: nums = [1]
Output: []
```

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`
- Each element in `nums` appears **once** or **twice**.
