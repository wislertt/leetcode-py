# Synonymous Sentences

**Difficulty:** Medium
**Topics:** Sort, Union Find, Array, Hash Table, String, Backtracking
**Tags:** neetcode

**LeetCode:** [Problem 1258](https://leetcode.com/problems/synonymous-sentences/description/)

## Problem Description

You are given a list of equivalent string pairs `synonyms` where `synonyms[i] = [s<sub>i</sub>, t<sub>i</sub>]` indicates that `s<sub>i</sub>` and `t<sub>i</sub>` are equivalent strings. You are also given a sentence `text`.

Return all possible synonymous sentences **sorted lexicographically**.

## Examples

### Example 1:

```
Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
Explanation: From the synonyms, happy, joy and cheerful are equivalent, and sad and sorrow are equivalent. Replacing each synonymous word independently gives 2 * 3 = 6 sentences.
```

### Example 2:

```
Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
```

## Constraints

- `0 <= synonyms.length <= 10`
- `synonyms[i].length == 2`
- `1 <= s<sub>i</sub>.length, t<sub>i</sub>.length <= 10`
- `s<sub>i</sub> != t<sub>i</sub>`
- `text` consists of at most `10` words.
- All the pairs of `synonyms` are **unique**.
- The words of `text` are separated by single spaces.
