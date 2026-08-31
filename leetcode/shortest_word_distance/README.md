# Shortest Word Distance

**Difficulty:** Easy
**Topics:** Array, String
**Tags:** neetcode

**LeetCode:** [Problem 243](https://leetcode.com/problems/shortest-word-distance/description/)

## Problem Description

Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return _the shortest distance between these two words in the list_.

## Examples

### Example 1:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
```

### Example 2:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

## Constraints

- `2 <= wordsDict.length <= 3 * 10^4`
- `1 <= wordsDict[i].length <= 10`
- `wordsDict[i]` consists of lowercase English letters.
- `word1` and `word2` are in `wordsDict`.
- `word1 != word2`
