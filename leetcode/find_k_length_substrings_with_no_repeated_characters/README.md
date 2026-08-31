# Find K-Length Substrings With No Repeated Characters

**Difficulty:** Medium
**Topics:** Hash Table, String, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 1100](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/)

## Problem Description

Given a string `s` and an integer `k`, return _the number of substrings in_ `s` _of length_ `k` _with no repeated characters_.

## Examples

### Example 1:

```
Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
```

### Example 2:

```
Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
```

## Constraints

- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
- 1 <= k <= 10^4
