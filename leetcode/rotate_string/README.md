# Rotate String

**Difficulty:** Easy
**Topics:** String, String Matching
**Tags:**

**LeetCode:** [Problem 796](https://leetcode.com/problems/rotate-string/description/)

## Problem Description

Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` after some number of **shifts** on `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

## Examples

### Example 1:

```
Input: s = "abcde", goal = "cdeab"
Output: true
```

### Example 2:

```
Input: s = "abcde", goal = "abced"
Output: false
```

## Constraints

- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.
