# Distinct Subsequences

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:** neetcode-150

**LeetCode:** [Problem 115](https://leetcode.com/problems/distinct-subsequences/description/)

## Problem Description

Given two strings `s` and `t`, return _the number of distinct subsequences of_ `s` _which equals_ `t`.

The test cases are generated so that the answer fits on a **32-bit** signed integer.

## Examples

### Example 1:

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

### Example 2:

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

## Constraints

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
