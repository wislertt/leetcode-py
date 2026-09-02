# Minimum Moves to Equal Array Elements II

**Difficulty:** Medium
**Topics:** Array, Math, Sorting
**Tags:**

**LeetCode:** [Problem 462](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

## Problem Description

Given an integer array `nums` of size `n`, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

## Examples

### Example 1:

```
Input: nums = [1,2,3]
Output: 2
Explanation: Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

### Example 2:

```
Input: nums = [1,10,2,9]
Output: 16
```

## Constraints

- n == nums.length
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- The answer is guaranteed to fit in a 32-bit integer.
