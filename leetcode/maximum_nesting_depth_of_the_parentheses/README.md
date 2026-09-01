# Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy
**Topics:** String, Stack, Bracket Sequences
**Tags:** neetcode

**LeetCode:** [Problem 1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/)

## Problem Description

Given a valid parentheses string `s`, return the nesting depth of `s`. The nesting depth is the maximum number of nested parentheses.

## Examples

### Example 1:

```
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
```

### Example 2:

```
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation: Digit 3 is inside of 3 nested parentheses in the string.
```

### Example 3:

```
Input: s = "()(())((()()))"
Output: 3
```

## Constraints

- `1 <= s.length <= 100`
- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
- It is guaranteed that parentheses expression `s` is a VPS.
