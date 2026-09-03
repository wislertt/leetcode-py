# Vowel Spellchecker

**Difficulty:** Medium
**Topics:** Array, Hash Table, String
**Tags:**

**LeetCode:** [Problem 966](https://leetcode.com/problems/vowel-spellchecker/description/)

## Problem Description

Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

- Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
- Vowel Errors: If after replacing the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.

In addition, the spell checker operates under the following precedence rules:

- When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
- When the query matches a word up to capitalization, you should return the first such match in the wordlist.
- When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
- If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.

## Examples

### Example 1:

```
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

### Example 2:

```
Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
```

## Constraints

- 1 <= wordlist.length, queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7
- wordlist[i] and queries[i] consist only of English letters.
