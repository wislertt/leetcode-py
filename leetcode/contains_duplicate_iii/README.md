# Contains Duplicate III

**Difficulty:** Hard
**Topics:** Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
**Tags:**

**LeetCode:** [Problem 220](https://leetcode.com/problems/contains-duplicate-iii/description/)

## Problem Description

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.

Find a pair of indices `(i, j)` such that:

- `i != j`,
- `abs(i - j) <= indexDiff`, and
- `abs(nums[i] - nums[j]) <= valueDiff`.

Return `true` _if such pair exists or_ `false` _otherwise_.

## Examples

### Example 1:

```
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
i != j, abs(i - j) <= indexDiff, abs(nums[i] - nums[j]) <= valueDiff
```

### Example 2:

```
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: No pair of indices satisfies all three conditions.
```

## Constraints

- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= indexDiff <= nums.length
- 0 <= valueDiff <= 10^9
