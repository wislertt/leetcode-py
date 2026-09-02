# Basic Calculator III

**Difficulty:** Hard
**Topics:** String, Stack, Recursion
**Tags:** neetcode

**LeetCode:** [Problem 772](https://leetcode.com/problems/basic-calculator-iii/description/)

## Problem Description

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `'+'`, `'-'`, `'*'`, `'/'` operators, and open `'('` and closing parentheses `')'`. The integer division should **truncate toward zero**.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Examples

### Example 1:

```
Input: s = "1+1"
Output: 2
```

### Example 2:

```
Input: s = "6-4/2"
Output: 4
```

### Example 3:

```
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

## Constraints

- 1 <= s.length <= 10^4
- s consists of digits, '+', '-', '*', '/', '(', and ')'.
- s is a valid expression.
