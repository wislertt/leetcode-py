# Valid Square

**Difficulty:** Medium
**Topics:** Math, Geometry
**Tags:**

**LeetCode:** [Problem 593](https://leetcode.com/problems/valid-square/description/)

## Problem Description

Given the coordinates of four points in 2D space <code>p1</code>, <code>p2</code>, <code>p3</code> and <code>p4</code>, return <code>true</code> <em>if the four points construct a square</em>.

<p>The coordinate of a point <code>p<sub>i</sub></code> is represented as <code>[x<sub>i</sub>, y<sub>i</sub>]</code>. The input is <strong>not</strong> given in any order.</p>

<p>A <strong>valid square</strong> has four equal sides with positive length and four equal angles (90-degree angles).</p>

## Examples

### Example 1:

```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
```

### Example 2:

```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
```

### Example 3:

```
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
```

## Constraints

- p1.length == p2.length == p3.length == p4.length == 2
- -10^4 <= xi, yi <= 10^4
