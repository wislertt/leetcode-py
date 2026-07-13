# Minimum Knight Moves

**Difficulty:** Medium
**Topics:** Breadth-First Search
**Tags:** grind

**LeetCode:** [Problem 1197](https://leetcode.com/problems/minimum-knight-moves/description/)

## Problem Description

In an **infinite** chess board with coordinates from `-infinity` to `+infinity`, you have a **knight** at square `[0, 0]`.

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return _the minimum number of steps needed to move the knight to the square_ `[x, y]`. It is guaranteed the answer exists.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/10/12/knight.png)

```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

### Example 2:

```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
```

## Constraints

- `-300 <= x, y <= 300`
- `0 <= |x| + |y| <= 300`
