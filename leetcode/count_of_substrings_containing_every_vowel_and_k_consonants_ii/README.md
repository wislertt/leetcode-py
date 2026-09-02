# Count of Substrings Containing Every Vowel and K Consonants II

**Difficulty:** Medium
**Topics:** Hash Table, String, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 3306](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/)

## Problem Description

You are given a string <code>word</code> and a <strong>non-negative</strong> integer <code>k</code>.

Return the total number of <span data-keyword="substring-nonempty">substrings</span> of <code>word</code> that contain every vowel (<code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>) <strong>at least</strong> once and <strong>exactly</strong> <code>k</code> consonants.

## Examples

### Example 1:

```
Input: word = "aeioqq", k = 1
Output: 0
Explanation: There is no substring with every vowel.
```

### Example 2:

```
Input: word = "aeiou", k = 0
Output: 1
Explanation: The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
```

### Example 3:

```
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation: The substrings with every vowel and one consonant are:
- word[0..5], which is "ieaouq".
- word[6..11], which is "qieaou".
- word[7..12], which is "ieaouq".
```

## Constraints

- 5 <= word.length <= 2 * 10^5
- word consists only of lowercase English letters.
- 0 <= k <= word.length - 5
