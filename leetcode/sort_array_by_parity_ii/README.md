# Sort Array By Parity II

**Difficulty:** Easy
**Topics:** Array, Two Pointers, Sorting
**Tags:**

**LeetCode:** [Problem 922](https://leetcode.com/problems/sort-array-by-parity-ii/description/)

## Problem Description

<p>Given an array of integers <code>nums</code>, half of the integers in <code>nums</code> are <strong>odd</strong>, and the other half are <strong>even</strong>.</p>

<p>Sort the array so that whenever <code>nums[i]</code> is odd, <code>i</code> is <strong>odd</strong>, and whenever <code>nums[i]</code> is even, <code>i</code> is <strong>even</strong>.</p>

<p>Return <em>any answer array that satisfies this condition</em>.</p>

## Examples

### Example 1:

```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

### Example 2:

```
Input: nums = [2,3]
Output: [2,3]
```

## Constraints

- 2 <= nums.length <= 2 * 10^4
- nums.length is even.
- Half of the integers in nums are even.
- 0 <= nums[i] <= 1000

**Follow up:** Could you solve it in-place?
