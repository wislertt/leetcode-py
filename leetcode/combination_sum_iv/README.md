# Combination Sum IV

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Tags:** grind, neetcode-150, neetcode-250

**LeetCode:** [Problem 377](https://leetcode.com/problems/combination-sum-iv/description/)

## Problem Description

Given an array of **distinct** integers `nums` and a target integer `target`, return the number of possible combinations that add up to `target`.

The test cases are generated so that the answer can fit in a 32-bit integer.

Note that different sequences are counted as different combinations.

## Examples

### Example 1:

```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

### Example 2:

```
Input: nums = [9], target = 3
Output: 0
```

## Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of `nums` are **unique**.
- 1 <= target <= 1000

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
