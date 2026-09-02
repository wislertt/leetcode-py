# Construct K Palindrome Strings

**Difficulty:** Medium
**Topics:** Hash Table, String, Greedy, Counting
**Tags:** neetcode

**LeetCode:** [Problem 1400](https://leetcode.com/problems/construct-k-palindrome-strings/description/)

## Problem Description

Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct **non-empty** `k` palindrome strings or `false` otherwise.

## Examples

### Example 1:

```
Input: s = "annabelle", k = 2
Output: true
```

**Explanation:** You can construct two palindromes using all characters in `s`. Some possible constructions `"anna" + "elble"`, `"anbna" + "elle"`, `"anellena" + "b"`.

### Example 2:

```
Input: s = "leetcode", k = 3
Output: false
```

**Explanation:** It is impossible to construct 3 palindromes using all the characters of `s`.

### Example 3:

```
Input: s = "true", k = 4
Output: true
```

**Explanation:** The only possible solution is to put each character in a separate string.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= 10^5`
