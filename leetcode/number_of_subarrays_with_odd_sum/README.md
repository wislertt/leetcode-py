# Number of Sub-arrays With Odd Sum

**Difficulty:** Medium
**Topics:** Array, Math, Dynamic Programming, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 1524](https://leetcode.com/problems/number-of-subarrays-with-odd-sum/description/)

## Problem Description

<p>Given an array of integers <code>arr</code>, return <em>the number of subarrays with an <strong>odd</strong> sum</em>.</p>

<p>Since the answer can be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

## Examples

### Example 1:

```
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
```

### Example 2:

```
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
```

### Example 3:

```
Input: arr = [1,2,3,4,5,6,7]
Output: 16
```

## Constraints

- 1 &lt;= arr.length &lt;= 10^5
- 1 &lt;= arr[i] &lt;= 100
