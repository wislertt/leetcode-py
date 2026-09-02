# Shortest Word Distance III

**Difficulty:** Medium
**Topics:** Array, String
**Tags:**

**LeetCode:** [Problem 245](https://leetcode.com/problems/shortest-word-distance-iii/description/)

## Problem Description

Given an array of strings `wordsDict` and two strings that already exist in the array `word1` and `word2`, return _the shortest distance between the occurrence of these two words in the list_.

**Note** that `word1` and `word2` may be the same. It is guaranteed that they represent **two individual words** in the list.

## Examples

### Example 1:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

### Example 2:

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
```

## Constraints

- `1 <= wordsDict.length <= 10^5`
- `1 <= wordsDict[i].length <= 10`
- `wordsDict[i]` consists of lowercase English letters.
- `word1` and `word2` are in `wordsDict`.
