# Longest Uncommon Subsequence I

**Difficulty:** Easy
**Topics:** String
**Tags:**

**LeetCode:** [Problem 521](https://leetcode.com/problems/longest-uncommon-subsequence-i/description/)

## Problem Description

Given two strings `a` and `b`, return the length of the **longest uncommon subsequence** between `a` and `b`. If no such uncommon subsequence exists, return `-1`.

An **uncommon subsequence** between two strings is a string that is a subsequence of exactly one of them.

## Examples

### Example 1:

```
Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
```

### Example 2:

```
Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".
```

### Example 3:

```
Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string `a` is also a subsequence of string `b`.
```

## Constraints

- 1 <= a.length, b.length <= 100
- `a` and `b` consist of lower-case English letters.
