# Contains Duplicate II

**Difficulty:** Easy
**Topics:** Array, Hash Table, Sliding Window
**Tags:** neetcode-250

**LeetCode:** [Problem 219](https://leetcode.com/problems/contains-duplicate-ii/description/)

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** * `i` _and_ `j` _in the array such that_ `nums[i] == nums[j]` _and_ `abs(i - j) <= k`.

## Examples

### Example 1:

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

### Example 2:

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

### Example 3:

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
