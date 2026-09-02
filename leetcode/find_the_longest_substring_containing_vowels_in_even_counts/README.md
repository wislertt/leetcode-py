# Find the Longest Substring Containing Vowels in Even Counts

**Difficulty:** Medium
**Topics:** String, Bit Manipulation, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 1371](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/)

## Problem Description

Given the string <code>s</code>, return the size of the longest substring containing each vowel an even number of times. That is, <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code> must appear an even number of times.

## Examples

### Example 1:

```
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
```

### Example 2:

```
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
```

### Example 3:

```
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
```

## Constraints

- 1 <= s.length <= 5 x 10^5
- s contains only lowercase English letters.
