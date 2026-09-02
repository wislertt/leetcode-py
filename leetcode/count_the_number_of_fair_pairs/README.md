# Count the Number of Fair Pairs

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 2563](https://leetcode.com/problems/count-the-number-of-fair-pairs/description/)

## Problem Description

Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code> and two integers <code>lower</code> and <code>upper</code>, return <em>the number of <strong>fair pairs</strong></em>.

A pair <code>(i, j)</code> is <strong>fair</strong> if:

<ul>
<li><code>0 &lt;= i &lt; j &lt; n</code>, and</li>
<li><code>lower &lt;= nums[i] + nums[j] &lt;= upper</code></li>
</ul>

## Examples

### Example 1:

```
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
```

**Explanation:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

### Example 2:

```
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
```

**Explanation:** There is a single fair pair: (2,3).

## Constraints

- 1 <= nums.length <= 10^5
- nums.length == n
- -10^9 <= nums[i] <= 10^9
- -10^9 <= lower <= upper <= 10^9
