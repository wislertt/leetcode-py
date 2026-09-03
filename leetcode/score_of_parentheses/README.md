# Score of Parentheses

**Difficulty:** Medium
**Topics:** String, Stack, Bracket Sequences
**Tags:**

**LeetCode:** [Problem 856](https://leetcode.com/problems/score-of-parentheses/description/)

## Problem Description

Given a balanced parentheses string `s`, return _the **score** of the string_.

The **score** of a balanced parentheses string is based on the following rule:

- `"()"` has score `1`.
- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

## Examples

### Example 1:

```
Input: s = "()"
Output: 1
```

### Example 2:

```
Input: s = "(())"
Output: 2
```

### Example 3:

```
Input: s = "()()"
Output: 2
```

## Constraints

- 2 <= s.length <= 50
- s consists of only `'('` and `')'`.
- s is a balanced parentheses string.
