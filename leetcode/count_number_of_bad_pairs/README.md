# Count Number of Bad Pairs

**Difficulty:** Medium
**Topics:** Array, Hash Table, Math, Counting
**Tags:** neetcode

**LeetCode:** [Problem 2364](https://leetcode.com/problems/count-number-of-bad-pairs/description/)

## Problem Description

You are given a <strong>0-indexed</strong> integer array <code>nums</code>. A pair of indices <code>(i, j)</code> is a <strong>bad pair</strong> if <code>i &lt; j</code> and <code>j - i != nums[j] - nums[i]</code>.

Return <em>the total number of <strong>bad pairs</strong> in </em><code>nums</code>.

## Examples

### Example 1:

```
Input: nums = [4,1,3,3]
Output: 5
```

**Explanation:** The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

### Example 2:

```
Input: nums = [1,2,3,4,5]
Output: 0
```

**Explanation:** There are no bad pairs.

## Constraints

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
