# Sentence Screen Fitting

**Difficulty:** Medium
**Topics:** Array, String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 418](https://leetcode.com/problems/sentence-screen-fitting/description/)

## Problem Description

Given a `rows x cols` screen and a `sentence` represented as a list of strings, return _the number of times the given sentence can be fitted on the screen_.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

## Examples

### Example 1:

```
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
```

### Example 2:

```
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
```

### Example 3:

```
Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
```

## Constraints

- `1 <= sentence.length`
- `1 <= rows, cols <= 4 * 10^4`
- `1 <= sentence[i].length <= 10`
- `sentence[i]` consists of only lower-case English letters.
