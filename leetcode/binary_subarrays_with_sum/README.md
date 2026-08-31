# Binary Subarrays With Sum

**Difficulty:** Medium
**Topics:** Array, Hash Table, Sliding Window, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 930](https://leetcode.com/problems/binary-subarrays-with-sum/description/)

## Problem Description

<p>Given a binary array <code>nums</code> and an integer <code>goal</code>, return <em>the number of non-empty <strong>subarrays</strong> with a sum</em> <code>goal</code>.</p>

<p>A <strong>subarray</b> is a contiguous part of the array.</p>

## Examples

### Example 1:

```
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```

### Example 2:

```
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
```

## Constraints

- 1 &lt;= nums.length &lt;= 3 * 10^4
- nums[i] is either 0 or 1.
- 0 &lt;= goal &lt;= nums.length
