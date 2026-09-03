# Most Common Word

**Difficulty:** Easy
**Topics:** Array, Hash Table, String, Counting
**Tags:**

**LeetCode:** [Problem 819](https://leetcode.com/problems/most-common-word/description/)

## Problem Description

Given a string `paragraph` and a string array of the banned words `banned`, return _the most frequent word that is not banned_. It is **guaranteed** there is **at least one word** that is not banned, and that the answer is **unique**.

The words in `paragraph` are **case-insensitive** and the answer should be returned in **lowercase**.

**Note** that words can not contain punctuation symbols.

## Examples

### Example 1:

```
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: "hit" occurs 3 times, but it is a banned word. "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
```

### Example 2:

```
Input: paragraph = "a.", banned = []
Output: "a"
```

## Constraints

- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters.
