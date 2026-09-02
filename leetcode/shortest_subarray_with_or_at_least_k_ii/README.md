# Shortest Subarray With OR at Least K II

**Difficulty:** Medium
**Topics:** Array, Bit Manipulation, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 3097](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/)

## Problem Description

You are given an array <code>nums</code> of <strong>non-negative</strong> integers and an integer <code>k</code>.</p>

<p>An array is called <strong>special</strong> if the bitwise <code>OR</code> of all of its elements is <strong>at least</strong> <code>k</code>.</p>

<p>Return <em>the length of the <strong>shortest</strong> <strong>special</strong> <strong>non-empty</strong> <span data-keyword="subarray-nonempty">subarray</span> of</em> <code>nums</code>, <em>or return</em> <code>-1</code> <em>if no special subarray exists</em>.</p>

## Examples

### Example 1:

```
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.
```

### Example 2:

```
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.
```

### Example 3:

```
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.
```

## Constraints

- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9
