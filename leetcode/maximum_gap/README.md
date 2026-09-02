# Maximum Gap

**Difficulty:** Medium
**Topics:** Array, Sorting, Bucket Sort, Radix Sort, Pigeonhole Principle
**Tags:**

**LeetCode:** [Problem 164](https://leetcode.com/problems/maximum-gap/description/)

## Problem Description

Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.

You must write an algorithm that runs in linear time and uses linear extra space.

## Examples

### Example 1:

```
Input: nums = [3,6,9,1]
Output: 3
```

**Explanation:** The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

### Example 2:

```
Input: nums = [10]
Output: 0
```

**Explanation:** The array contains less than 2 elements, therefore return 0.

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

**Follow up:** Could you solve it without using any built-in sorting function?
