# Strobogrammatic Number III

**Difficulty:** Hard
**Topics:** Recursion, Array, String
**Tags:**

**LeetCode:** [Problem 248](https://leetcode.com/problems/strobogrammatic-number-iii/description/)

## Problem Description

Given two strings low and high that represent two integers `low` and `high` where `low <= high`, return _the number of **strobogrammatic numbers** in the range_ `[low, high]`.

A **strobogrammatic number** is a number that looks the same when rotated `180` degrees (looked at upside down).

## Examples

### Example 1:

```
Input: low = "50", high = "100"
Output: 3
```

### Example 2:

```
Input: low = "0", high = "0"
Output: 1
```

## Constraints

- `1 <= low.length, high.length <= 15`
- `low` and `high` consist of only digits.
- `low <= high`
- `low` and `high` do not contain any leading zeros except for zero itself.
