# Shortest Subarray with Sum at Least K

**Difficulty:** Hard
**Topics:** Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue
**Tags:** neetcode

**LeetCode:** [Problem 862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/)

## Problem Description

Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the length of the shortest non-empty <strong>subarray</strong> of </em><code>nums</code><em> with a sum of at least </em><code>k</code>. If there is no such <strong>subarray</strong>, return <code>-1</code>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.

## Examples

### Example 1:

```
Input: nums = [1], k = 1
Output: 1
```

### Example 2:

```
Input: nums = [1,2], k = 4
Output: -1
```

### Example 3:

```
Input: nums = [2,-1,2], k = 3
Output: 3
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9
