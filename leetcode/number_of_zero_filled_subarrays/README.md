# Number of Zero-Filled Subarrays

**Difficulty:** Medium
**Topics:** Array, Math
**Tags:** neetcode

**LeetCode:** [Problem 2348](https://leetcode.com/problems/number-of-zero-filled-subarrays/description/)

## Problem Description

<p>Given an integer array <code>nums</code>, return <em>the number of <strong>subarrays</strong> filled with </em><code>0</code>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

## Examples

### Example 1:

```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

### Example 2:

```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
```

### Example 3:

```
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
```

## Constraints

- 1 &lt;= nums.length &lt;= 10^5
- -10^9 &lt;= nums[i] &lt;= 10^9
