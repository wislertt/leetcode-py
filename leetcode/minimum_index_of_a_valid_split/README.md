# Minimum Index of a Valid Split

**Difficulty:** Medium
**Topics:** Array, Hash Table, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 2780](https://leetcode.com/problems/minimum-index-of-a-valid-split/description/)

## Problem Description

An element <code>x</code> of an integer array <code>arr</code> of length <code>m</code> is <strong>dominant</strong> if <strong>more than half</strong> the elements of <code>arr</code> have a value of <code>x</code>.</p>

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code> with one <strong>dominant</strong> element.</p>

<p>You can split <code>nums</code> at an index <code>i</code> into two arrays <code>nums[0, ..., i]</code> and <code>nums[i + 1, ..., n - 1]</code>, but the split is only <strong>valid</strong> if:</p>

<ul>
	<li><code>0 &lt;= i &lt; n - 1</code></li>
	<li><code>nums[0, ..., i]</code>, and <code>nums[i + 1, ..., n - 1]</code> have the same dominant element.</li>
</ul>

<p>Here, <code>nums[i, ..., j]</code> denotes the subarray of <code>nums</code> starting at index <code>i</code> and ending at index <code>j</code>, both ends being inclusive. Particularly, if <code>j &lt; i</code> then <code>nums[i, ..., j]</code> denotes an empty subarray.</p>

<p>Return <em>the <strong>minimum</strong> index of a <strong>valid split</strong></em>. If no valid split exists, return <code>-1</code>.</p>

## Examples

### Example 1:

```
Input: nums = [1,2,2,2]
Output: 2
Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2].
In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3.
In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split.
It can be shown that index 2 is the minimum index of a valid split.
```

### Example 2:

```
Input: nums = [2,1,3,1,1,1,7,1,2,1]
Output: 4
Explanation: We can split the array at index 4 to obtain arrays [2,1,3,1,1] and [1,7,1,2,1].
In array [2,1,3,1,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
In array [1,7,1,2,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
Both [2,1,3,1,1] and [1,7,1,2,1] have the same dominant element as nums, so this is a valid split.
It can be shown that index 4 is the minimum index of a valid split.
```

### Example 3:

```
Input: nums = [3,3,3,3,7,2,2]
Output: -1
Explanation: It can be shown that there is no valid split.
```

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- nums has exactly one dominant element.
