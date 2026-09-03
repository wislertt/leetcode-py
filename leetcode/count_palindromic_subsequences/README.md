# Count Different Palindromic Subsequences

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:**

**LeetCode:** [Problem 730](https://leetcode.com/problems/count-palindromic-subsequences/description/)

## Problem Description

Given a string `s`, return _the number of different non-empty palindromic subsequences in_ `s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `a1, a2, ...` and `b1, b2, ...` are different if there is some `i` for which `ai != bi`.

## Examples

### Example 1:

```
Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
```

### Example 2:

```
Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
```

## Constraints

- `1 <= s.length <= 1000`
- `s[i]` is either `'a'`, `'b'`, `'c'`, or `'d'`.
