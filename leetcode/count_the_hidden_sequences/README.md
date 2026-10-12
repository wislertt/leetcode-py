# Count the Hidden Sequences

**Difficulty:** Medium
**Topics:** Array, Prefix Sum
**Tags:**

**LeetCode:** [Problem 2145](https://leetcode.com/problems/count-the-hidden-sequences/description/)

## Problem Description

You are given a 0-indexed array `differences` of `n` integers, which describes the differences between each pair of consecutive integers of a hidden sequence of length `n + 1`. You are also given two integers `lower` and `upper` that describe the inclusive range of values that the hidden sequence can contain. Return the number of possible hidden sequences. If there are no possible sequences, return 0.

## Examples

### Example 1:

```text
Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
```

### Example 2:

```text
Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
```

### Example 3:

```text
Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
```

## Constraints

- `n == differences.length`
- `1 <= n <= 10^5`
- `-10^5 <= differences[i] <= 10^5`
- `-10^5 <= lower <= upper <= 10^5`
