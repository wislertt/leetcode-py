# Minimum Number of Increments on Subarrays to Form a Target Array

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming, Stack, Greedy, Monotonic Stack
**Tags:** neetcode

**LeetCode:** [Problem 1526](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/)

## Problem Description

You are given an integer array <code>target</code>. You have an integer array <code>initial</code> of the same size as <code>target</code> with all elements initially zeros.

In one operation you can choose <strong>any</strong> subarray from <code>initial</code> and increment each value by one.

Return <em>the minimum number of operations to form a </em><code>target</code><em> array from </em><code>initial</code>.

The test cases are generated so that the answer fits in a 32-bit integer.

## Examples

### Example 1:

```
Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
```

### Example 2:

```
Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
```

### Example 3:

```
Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2]
```

## Constraints

- 1 <= target.length <= 10^5
- 1 <= target[i] <= 10^5
- The input is generated such that the answer fits inside a 32 bit integer.
