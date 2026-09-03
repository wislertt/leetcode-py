# Partition Array into Disjoint Intervals

**Difficulty:** Medium
**Topics:** Array
**Tags:**

**LeetCode:** [Problem 915](https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/)

## Problem Description

<p>Given an integer array <code>nums</code>, partition it into two (contiguous) subarrays <code>left</code> and <code>right</code> so that:</p>

<ul>
	<li>Every element in <code>left</code> is less than or equal to every element in <code>right</code>.</li>
	<li><code>left</code> and <code>right</code> are non-empty.</li>
	<li><code>left</code> has the smallest possible size.</li>
</ul>

<p>Return <em>the length of </em><code>left</code><em> after such a partitioning</em>.</p>

<p>Test cases are generated such that partitioning exists.</p>

## Examples

### Example 1:

```
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

### Example 2:

```
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```

## Constraints

- 2 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6
- There is at least one valid answer for the given input.
