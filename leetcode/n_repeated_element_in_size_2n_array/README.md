# N-Repeated Element in Size 2N Array

**Difficulty:** Easy
**Topics:** Array, Hash Table
**Tags:**

**LeetCode:** [Problem 961](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/)

## Problem Description

You are given an integer array `nums` with the following properties:

- `nums.length == 2 * n`.
- `nums` contains `n + 1` **unique** values, `n` of which occur **exactly once** in the array.
- Exactly one element of `nums` is repeated `n` times.

Return the element that is repeated `n` times.

## Examples

### Example 1:

```
Input: nums = [1,2,3,3]
Output: 3
```

### Example 2:

```
Input: nums = [2,1,2,5,3,2]
Output: 2
```

### Example 3:

```
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
```

## Constraints

- 2 <= n <= 5000
- nums.length == 2 * n
- 0 <= nums[i] <= 10^4
- nums contains n + 1 unique elements and one of them is repeated exactly n times.

**Follow-up:** Can you solve it without a hash table, in O(1) extra space?
