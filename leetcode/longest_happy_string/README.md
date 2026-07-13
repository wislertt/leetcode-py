# Longest Happy String

**Difficulty:** Medium
**Topics:** String, Greedy, Heap (Priority Queue)
**Tags:** neetcode-250

**LeetCode:** [Problem 1405](https://leetcode.com/problems/longest-happy-string/description/)

## Problem Description

A string `s` is called **happy** if it satisfies the following conditions:

- `s` only contains the letters `'a'`, `'b'`, and `'c'`.
- `s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring.
- `s` contains **at most** `a` occurrences of the letter `'a'`.
- `s` contains **at most** `b` occurrences of the letter `'b'`.
- `s` contains **at most** `c` occurrences of the letter `'c'`.

Given three integers `a`, `b`, and `c`, return _the **longest possible happy** string_. If there are multiple longest happy strings, return _any of them_. If there is no such string, return _the empty string_ `""`.

## Examples

### Example 1:

```
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

### Example 2:

```
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
```

## Constraints

- `0 <= a, b, c <= 100`
- `a + b + c > 0`
