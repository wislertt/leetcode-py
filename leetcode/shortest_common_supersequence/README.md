# Shortest Common Supersequence

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1092](https://leetcode.com/problems/shortest-common-supersequence/description/)

## Problem Description

Given two strings <code>str1</code> and <code>str2</code>, return <em>the shortest string that has both </em><code>str1</code><em> and </em><code>str2</code><em> as <strong>subsequences</strong></em>. If there are multiple valid strings, return <strong>any</strong> of them.

A string <code>s</code> is a <strong>subsequence</strong> of string <code>t</code> if deleting some number of characters from <code>t</code> (possibly <code>0</code>) results in the string <code>s</code>.

## Examples

### Example 1:

```
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: str1 = "abac" is a subsequence of "cabac" because we can delete the first "c". str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac". The answer provided is the shortest such string that satisfies these properties.
```

### Example 2:

```
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
```

## Constraints

- <code>1 &lt;= str1.length, str2.length &lt;= 1000</code>
- <code>str1</code> and <code>str2</code> consist of lowercase English letters.
