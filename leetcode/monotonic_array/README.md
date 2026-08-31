# Monotonic Array

**Difficulty:** Easy
**Topics:** Array
**Tags:** neetcode

**LeetCode:** [Problem 896](https://leetcode.com/problems/monotonic-array/description/)

## Problem Description

An array is <strong>monotonic</strong> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>nums</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>nums[i] &lt;= nums[j]</code>. An array <code>nums</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>nums[i] &gt;= nums[j]</code>.</p>

<p>Given an integer array <code>nums</code>, return <code>true</code> <em>if the given array is monotonic, or</em> <code>false</code> <em>otherwise</em>.</p>

## Examples

### Example 1:

```
Input: nums = [1,2,2,3]
Output: true
```

### Example 2:

```
Input: nums = [6,5,4,4]
Output: true
```

### Example 3:

```
Input: nums = [1,3,2]
Output: false
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
