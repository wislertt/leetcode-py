# Android Unlock Patterns

**Difficulty:** Medium
**Topics:** Bit Manipulation, Dynamic Programming, Backtracking, Bitmask
**Tags:** neetcode

**LeetCode:** [Problem 351](https://leetcode.com/problems/android-unlock-patterns/description/)

## Problem Description

Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of `k` dots is a **valid** unlock pattern if both of the following are true:

- All the dots in the sequence are **distinct**.
- If the line segment connecting two consecutive dots in the sequence passes through the **center** of any other dot, the other dot **must have previously appeared** in the sequence. No jumps through the center non-selected dots are allowed.
    - For example, connecting dots `2` and `9` without dots `5` or `6` appearing beforehand is valid because the line from dot `2` to dot `9` does not pass through the center of either dot `5` or `6`.
    - However, connecting dots `1` and `3` without dot `2` appearing beforehand is invalid because the line from dot `1` to dot `3` passes through the center of dot `2`.

Given two integers `m` and `n`, return _the **number of unique and valid unlock patterns** of the Android grid lock screen that consist of **at least**_ `m` _keys and **at most**_ `n` _keys_.

Two unlock patterns are considered **unique** if there is a dot in one sequence that is not in the other, or the order of the dots is different.

## Examples

### Example 1:

![Unlock patterns](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0351.Android%20Unlock%20Patterns/images/android-unlock.png)

```
Input: m = 1, n = 1
Output: 9
```

### Example 2:

```
Input: m = 1, n = 2
Output: 65
```

## Constraints

- `1 <= m, n <= 9`
- `m <= n`
