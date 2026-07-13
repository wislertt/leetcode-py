# Verifying an Alien Dictionary

**Difficulty:** Easy
**Topics:** Array, Hash Table, String
**Tags:** neetcode-250

**LeetCode:** [Problem 953](https://leetcode.com/problems/verifying-an-alien-dictionary/description/)

## Problem Description

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

## Examples

### Example 1:

```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

### Example 2:

```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

### Example 3:

```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app".
```

## Constraints

- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- `order.length == 26`
- All characters in `words[i]` and `order` are English lowercase letters.
