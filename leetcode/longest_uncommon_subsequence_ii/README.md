# Longest Uncommon Subsequence II

**Difficulty:** Medium
**Topics:** Array, Hash Table, Two Pointers, String, Sorting
**Tags:**

**LeetCode:** [Problem 522](https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/)

## Problem Description

Given an array of strings <code>strs</code>, return <em>the length of the <strong>longest uncommon subsequence</strong> between them</em>. If the longest uncommon subsequence does not exist, return <code>-1</code>.

An <strong>uncommon subsequence</strong> between an array of strings is a string that is a <strong>subsequence of one string but not the others</strong>.

A <strong>subsequence</strong> of a string <code>s</code> is a string that can be obtained after deleting any number of characters from <code>s</code>.

<ul>
<li>For example, <code>&quot;abc&quot;</code> is a subsequence of <code>&quot;aebdc&quot;</code> because you can delete the underlined characters in <code>&quot;a<u>e</u>b<u>d</u>c&quot;</code> to get <code>&quot;abc&quot;</code>. Other subsequences of <code>&quot;aebdc&quot;</code> include <code>&quot;aebdc&quot;</code>, <code>&quot;aeb&quot;</code>, and <code>&quot;&quot;</code> (empty string).</li>
</ul>

## Examples

### Example 1:

```
Input: strs = ["aba","cdc","eae"]
Output: 3
```

### Example 2:

```
Input: strs = ["aaa","aaa","aa"]
Output: -1
```

## Constraints

- 2 <= strs.length <= 50
- 1 <= strs[i].length <= 10
- strs[i] consists of lowercase English letters.
