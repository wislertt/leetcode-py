# Wiggle Sort II

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Greedy, Sorting, Quickselect
**Tags:**

**LeetCode:** [Problem 324](https://leetcode.com/problems/wiggle-sort-ii/description/)

## Problem Description

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

You may assume the input array always has a valid answer.

## Examples

### Example 1:

```
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
```

### Example 2:

```
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input `nums`.

**Follow up:** Can you do it in `O(n)` time and/or **in-place** with `O(1)` extra space?
