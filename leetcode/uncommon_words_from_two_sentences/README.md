# Uncommon Words from Two Sentences

**Difficulty:** Easy
**Topics:** Hash Table, String, Counting
**Tags:** neetcode

**LeetCode:** [Problem 884](https://leetcode.com/problems/uncommon-words-from-two-sentences/description/)

## Problem Description

A <strong>sentence</strong> is a string of single-space separated words where each word consists only of lowercase English letters.</p>

<p>A word is <strong>uncommon</strong> if it appears exactly once in one of the sentences, and <strong>does not appear</strong> in the other sentence.</p>

<p>Given two sentences <code>s1</code> and <code>s2</code>, return <em>a list of all the <strong>uncommon words</strong></em>. You may return the answer in any order.

## Examples

### Example 1:

```
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
```

### Example 2:

```
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
```

## Constraints

- 1 <= s1.length, s2.length <= 200
- s1 and s2 consist of lowercase English letters and spaces.
- s1 and s2 do not have leading or trailing spaces.
- All the words in s1 and s2 are separated by a single space.
