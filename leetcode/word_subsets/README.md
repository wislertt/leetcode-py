# Word Subsets

**Difficulty:** Medium
**Topics:** Array, Hash Table, String
**Tags:** neetcode

**LeetCode:** [Problem 916](https://leetcode.com/problems/word-subsets/description/)

## Problem Description

You are given two string arrays <code>words1</code> and <code>words2</code>.</p>

<p>A string <code>b</code> is a <strong>subset</strong> of string <code>a</code> if every letter in <code>b</code> occurs in <code>a</code> including multiplicity.</p>

<ul>
	<li>For example, <code>"wrr"</code> is a subset of <code>"warrior"</code> but is not a subset of <code>"world"</code>.</li>
</ul>

<p>A string <code>a</code> from <code>words1</code> is <strong>universal</strong> if for every string <code>b</code> in <code>words2</code>, <code>b</code> is a subset of <code>a</code>.</p>

<p>Return an array of all the <strong>universal</strong> strings in <code>words1</code>. You may return the answer in <strong>any order</strong>.</p>

## Examples

### Example 1:

```
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
```

### Example 2:

```
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","o"]
Output: ["google","leetcode"]
```

## Constraints

- 1 <= words1.length, words2.length <= 10^4
- 1 <= words1[i].length, words2[i].length <= 10
- words1[i] and words2[i] consist only of lowercase English letters.
- All the strings of words1 are unique.
