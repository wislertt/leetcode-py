# Broken Calculator

**Difficulty:** Medium
**Topics:** Math, Greedy
**Tags:**

**LeetCode:** [Problem 991](https://leetcode.com/problems/broken-calculator/description/)

## Problem Description

There is a broken calculator that has the integer `startValue` on its display initially. In one operation, you can:

- multiply the number on display by `2`, or
- subtract `1` from the number on display.

Given two integers `startValue` and `target`, return the minimum number of operations needed to display `target` on the calculator.

## Examples

### Example 1:

```
Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
```

### Example 2:

```
Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
```

### Example 3:

```
Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
```

## Constraints

- 1 <= startValue, target <= 10^9
