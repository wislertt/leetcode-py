# Valid Palindrome III

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1216](https://leetcode.com/problems/valid-palindrome-iii/description/)

## Problem Description

Given a string `s` and an integer `k`, return `true` if `s` is a `k`**-palindrome**.

A string is `k`**-palindrome** if it can be transformed into a palindrome by removing at most `k` characters from it.

## Examples

### Example 1:

```
Input: s = "abcdeca", k = 2
Output: true
```

**Explanation:** Remove 'b' and 'e' characters.

### Example 2:

```
Input: s = "abbababa", k = 1
Output: true
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only lowercase English letters.
- `1 <= k <= s.length`
