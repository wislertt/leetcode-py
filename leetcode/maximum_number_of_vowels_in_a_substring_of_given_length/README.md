# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium
**Topics:** String, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)

## Problem Description

Given a string `s` and an integer `k`, return _the maximum number of vowel letters in any substring of_ `s` _with length_ `k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Examples

### Example 1:

```
Input: s = "abciiidef", k = 3
Output: 3
```

**Explanation:** The substring "iii" contains 3 vowel letters.

### Example 2:

```
Input: s = "aeiou", k = 2
Output: 2
```

**Explanation:** Any substring of length 2 contains 2 vowels.

### Example 3:

```
Input: s = "leetcode", k = 3
Output: 2
```

**Explanation:** "lee", "eet" and "ode" contain 2 vowels.

## Constraints

- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length
