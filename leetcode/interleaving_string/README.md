# Interleaving String

**Difficulty:** Medium
**Topics:** String, Dynamic Programming
**Tags:** neetcode-150, neetcode-250

**LeetCode:** [Problem 97](https://leetcode.com/problems/interleaving-string/description/)

## Problem Description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

**Note:** `a + b` is the concatenation of strings `a` and `b`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aadbbcbcac".
```

### Example 2:

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is hard to find a viable interleaving because s3 must preserve the character order of s1 and s2.
```

### Example 3:

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints

- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters.
