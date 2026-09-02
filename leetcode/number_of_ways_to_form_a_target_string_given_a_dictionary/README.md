# Number of Ways to Form a Target String Given a Dictionary

**Difficulty:** Hard
**Topics:** Array, String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1639](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/)

## Problem Description

You are given a list of strings of the same length `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

- `target` should be formed from left to right.
- To form the `i`th character (0-indexed) of `target`, you can choose the `k`th character of the `j`th string in `words` if `target[i] = words[j][k]`.
- Once you use the `k`th character of the `j`th string of `words`, you can no longer use the `x`th character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string.
- Repeat the process until you form the string `target`.

Notice that you can use multiple characters from the same string in `words` provided the conditions above are met.

Return the number of ways to form `target` from `words`. Since the answer may be too large, return it modulo `10^9 + 7`.

## Examples

### Example 1:

```
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
- index 0 (acca), index 1 (bbbb), index 3 (caca)
- index 0 (acca), index 2 (bbbb), index 3 (caca)
- index 0 (acca), index 1 (bbbb), index 3 (acca)
- index 0 (acca), index 2 (bbbb), index 3 (acca)
- index 1 (caca), index 2 (bbbb), index 3 (acca)
- index 1 (caca), index 2 (bbbb), index 3 (caca)
```

### Example 2:

```
Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
- index 0 (baab), index 1 (baab), index 2 (abba)
- index 0 (baab), index 1 (baab), index 3 (baab)
- index 0 (baab), index 2 (baab), index 3 (baab)
- index 1 (abba), index 2 (baab), index 3 (baab)
```

## Constraints

- 1 <= words.length <= 1000
- 1 <= words[i].length <= 1000
- All strings in `words` have the same length.
- 1 <= target.length <= 1000
- `words[i]` and `target` consist of only lowercase English letters.
