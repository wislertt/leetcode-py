# Count Prefix and Suffix Pairs II

**Difficulty:** Hard
**Topics:** Array, String, Trie, Rolling Hash, String Matching, Hash Function, Z Algorithm
**Tags:** neetcode

**LeetCode:** [Problem 3045](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/description/)

## Problem Description

You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

- isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.

For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

## Examples

### Example 1:

```
Input: words = ["a","aba","ababa","aa"]
Output: 4
```

**Explanation:** The counted index pairs are (0, 1), (0, 2), (0, 3) and (1, 2).

### Example 2:

```
Input: words = ["pa","papa","ma","mama"]
Output: 2
```

**Explanation:** The counted index pairs are (0, 1) and (2, 3).

### Example 3:

```
Input: words = ["abab","ab"]
Output: 0
```

## Constraints

- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 10^5
- words[i] consists only of lowercase English letters.
- The sum of the lengths of all words[i] does not exceed 5 * 10^5.
