# Remove Duplicate Letters

**Difficulty:** Medium
**Topics:** String, Stack, Greedy, Monotonic Stack
**Tags:**

**LeetCode:** [Problem 316](https://leetcode.com/problems/remove-duplicate-letters/description/)

## Problem Description

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

## Examples

### Example 1:

```
Input: s = "bcabc"
Output: "abc"
Explanation: The possible results are "abc", "bac", "bca", "cab", and "cba". The smallest is "abc".
```

### Example 2:

```
Input: s = "cbacdcbc"
Output: "acdb"
Explanation: Removing duplicates while keeping the result smallest gives "acdb".
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

**Note:** This question is the same as 1081: [Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/).
