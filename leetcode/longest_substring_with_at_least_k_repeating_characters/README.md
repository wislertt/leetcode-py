# Longest Substring with At Least K Repeating Characters

**Difficulty:** Medium
**Topics:** Hash Table, String, Divide and Conquer, Sliding Window
**Tags:**

**LeetCode:** [Problem 395](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/)

## Problem Description

Given a string `s` and an integer `k`, return _the length of the longest substring of_ `s` _such that the frequency of each character in this substring is greater than or equal to_ `k`.

## Examples

### Example 1:

```
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
```

### Example 2:

```
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of only lowercase English letters.
- `1 <= k <= 10^5`
