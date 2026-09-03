# Self Dividing Numbers

**Difficulty:** Easy
**Topics:** Math
**Tags:**

**LeetCode:** [Problem 728](https://leetcode.com/problems/self-dividing-numbers/description/)

## Problem Description

A **self-dividing number** is a number that is divisible by every digit it contains.

- For example, `128` is **a self-dividing number** because `128 % 1 == 0`, `128 % 2 == 0`, and `128 % 8 == 0`.

A **self-dividing number** is not allowed to contain the digit zero.

Given two integers `left` and `right`, return _a list of all the **self-dividing numbers** in the range_ `[left, right]` _(both **inclusive**)_.

## Examples

### Example 1:

```
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
```

### Example 2:

```
Input: left = 47, right = 85
Output: [48,55,66,77]
```

## Constraints

- `1 <= left <= right <= 10^4`
