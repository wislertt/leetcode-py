# Find the Longest Valid Obstacle Course at Each Position

**Difficulty:** Hard
**Topics:** Array, Binary Search, Binary Indexed Tree, Longest Increasing Subsequence
**Tags:** neetcode

**LeetCode:** [Problem 1964](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/)

## Problem Description

You want to build some obstacle courses. You are given a <strong>0-indexed</strong> integer array <code>obstacles</code> of length <code>n</code>, where <code>obstacles[i]</code> describes the height of the <code>i<sup>th</sup></code> obstacle.

For every index <code>i</code> between <code>0</code> and <code>n - 1</code> (<strong>inclusive</strong>), find the length of the <strong>longest obstacle course</strong> in <code>obstacles</code> such that:

<ul>
<li>You choose any number of obstacles between <code>0</code> and <code>i</code> <strong>inclusive</strong>.</li>
<li>You must include the <code>i<sup>th</sup></code> obstacle in the course.</li>
<li>You must put the chosen obstacles in the <strong>same order</strong> as they appear in <code>obstacles</code>.</li>
<li>Every obstacle (except the first) is <strong>taller</strong> than or the <strong>same height</strong> as the obstacle immediately before it.</li>
</ul>

Return <em>an array</em> <code>ans</code> <em>of length</em> <code>n</code>, <em>where</em> <code>ans[i]</code> <em>is the length of the <strong>longest obstacle course</strong> for index</em> <code>i</code><em> as described above</em>.

## Examples

### Example 1:

```
Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.
```

### Example 2:

```
Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.
```

### Example 3:

```
Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.
```

## Constraints

- n == obstacles.length
- 1 <= n <= 10^5
- 1 <= obstacles[i] <= 10^7
