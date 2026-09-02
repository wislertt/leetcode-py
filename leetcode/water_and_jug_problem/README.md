# Water and Jug Problem

**Difficulty:** Medium
**Topics:** Math, Depth-First Search, Breadth-First Search, Greatest Common Divisor
**Tags:**

**LeetCode:** [Problem 365](https://leetcode.com/problems/water-and-jug-problem/description/)

## Problem Description

You are given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return _whether the total amount of water in both jugs may reach_ `target` _using the following operations_:

- Fill either jug completely with water.
- Completely empty either jug.
- Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

## Examples

### Example 1:

```
Input: x = 3, y = 5, target = 4
Output: true
Explanation:
Fill the 5-liter jug (0, 5). Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2). Empty the 3-liter jug (0, 2). Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0). Fill the 5-liter jug again (2, 5). Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4). Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).
```

### Example 2:

```
Input: x = 2, y = 6, target = 5
Output: false
```

### Example 3:

```
Input: x = 1, y = 2, target = 3
Output: true
Explanation: Fill both jugs. The total amount of water in both jugs is equal to 3 now.
```

## Constraints

- `1 <= x, y, target <= 10^3`
