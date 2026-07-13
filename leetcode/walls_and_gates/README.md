# Walls And Gates

**Difficulty:** Medium
**Topics:** Array, Breadth-First Search, Matrix
**Tags:** neetcode-150, neetcode-250

**LeetCode:** [Problem 286](https://leetcode.com/problems/walls-and-gates/description/)

## Problem Description

You are given a `m × n` 2D grid initialized with these three possible values:

- `-1` - A wall or obstacle that can not be traversed.
- `0` - A gate.
- `INF` - Infinity an empty room. We use the value `2^31 - 1 = 2147483647` to represent `INF`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.

**Follow up:** Can you solve it in-place and in O(m × n) time complexity?

## Examples

### Example 1:

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
**Explanation:** the 2D grid is:
```

INF -1 0 INF
INF INF INF -1
INF -1 INF -1
0 -1 INF INF

```
the result is:
```

3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4

```
explanation: the gate is located at (0,2), (3,0), (3,3). the room at (0,0) is distance 3 from the nearest gate at (3,0).`

### Example 2:

```

Input: rooms = [[0,-1],[2147483647,2147483647]]
Output: [[0,-1],[1,2]]

```

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 100`
- `rooms[i][j]` is one of `-1`, `0`, or `2147483647`.


```
