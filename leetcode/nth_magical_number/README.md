# Nth Magical Number

**Difficulty:** Hard
**Topics:** Math, Binary Search, Number Theory
**Tags:**

**LeetCode:** [Problem 878](https://leetcode.com/problems/nth-magical-number/description/)

## Problem Description

A positive integer is magical if it is divisible by either `a` or `b`.

Given the three integers `n`, `a`, and `b`, return the nth magical number. Since the answer may be very large, return it modulo `10^9 + 7`.

## Examples

### Example 1:

```
Input: n = 1, a = 2, b = 3
Output: 2
```

### Example 2:

```
Input: n = 4, a = 2, b = 3
Output: 6
```

## Constraints

- 1 <= n <= 10^9
- 2 <= a, b <= 4 * 10^4

**Follow up:** Could you solve the problem in `O(log(n * min(a, b)))` time complexity?
