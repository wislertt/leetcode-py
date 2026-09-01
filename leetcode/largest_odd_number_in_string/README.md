# Largest Odd Number in String

**Difficulty:** Easy
**Topics:** Math, String, Greedy
**Tags:** neetcode

**LeetCode:** [Problem 1903](https://leetcode.com/problems/largest-odd-number-in-string/description/)

## Problem Description

You are given a string `num`, representing a large integer. Return _the **largest-valued odd** integer (as a string) that is a **non-empty substring** of_ `num`_, or an empty string_ `""` _if no odd integer exists_.

A **substring** is a contiguous sequence of characters within a string.

## Examples

### Example 1:

```
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
```

### Example 2:

```
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
```

### Example 3:

```
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
```

## Constraints

- 1 <= num.length <= 10^5
- num only consists of digits and does not contain any leading zeros.
