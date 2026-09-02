# Remove Invalid Parentheses

**Difficulty:** Hard
**Topics:** String, Backtracking, Breadth-First Search
**Tags:**

**LeetCode:** [Problem 301](https://leetcode.com/problems/remove-invalid-parentheses/description/)

## Problem Description

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return _a list of **unique strings**_ that are valid with the minimum number of removals. You may return the answer in **any order**.

## Examples

### Example 1:

```
Input: s = "()())()"
Output: ["(())()","()()()"]
```

### Example 2:

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
```

### Example 3:

```
Input: s = ")("
Output: [""]
```

## Constraints

- `1 <= s.length <= 25`
- `s` consists of lowercase English letters and parentheses `'('` and `')'`.
- There will be at most `20` parentheses in `s`.
