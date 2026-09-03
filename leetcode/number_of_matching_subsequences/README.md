# Number of Matching Subsequences

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Binary Search, Dynamic Programming, Trie, Sorting
**Tags:**

**LeetCode:** [Problem 792](https://leetcode.com/problems/number-of-matching-subsequences/description/)

## Problem Description

Given a string `s` and an array of strings `words`, return _the number of_ `words[i]` _that is a subsequence of_ `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Examples

### Example 1:

```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

### Example 2:

```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

## Constraints

- 1 <= s.length <= 5 * 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 50
- s and words[i] consist of only lowercase English letters.
