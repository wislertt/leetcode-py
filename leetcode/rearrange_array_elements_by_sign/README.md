# Rearrange Array Elements by Sign

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 2149](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/)

## Problem Description

You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in nums is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

## Examples

### Example 1:

```
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
```

**Explanation:** The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4]. The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

### Example 2:

```
Input: nums = [-1,1]
Output: [1,-1]
```

**Explanation:** 1 is the only positive integer and -1 the only negative integer in nums. So nums is rearranged to [1,-1].

## Constraints

- 2 <= nums.length <= 2 * 10^5
- nums.length is even
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers.

It is not required to do the modifications in-place.
