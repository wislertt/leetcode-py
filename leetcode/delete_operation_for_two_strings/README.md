# Delete Operation for Two Strings

**Difficulty:** Medium
**Topics:** String, Dynamic Programming, Longest Common Subsequence
**Tags:**

**LeetCode:** [Problem 583](https://leetcode.com/problems/delete-operation-for-two-strings/description/)

## Problem Description

Given two strings `word1` and `word2`, return _the minimum number of steps_ required to make `word1` and `word2` the same.

In one step, you can delete exactly one character in either string.

## Examples

### Example 1:

```
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

### Example 2:

```
Input: word1 = "leetcode", word2 = "etco"
Output: 4
```

## Constraints

- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.
