# Knight Dialer

**Difficulty:** Medium
**Topics:** Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 935](https://leetcode.com/problems/knight-dialer/description/)

## Problem Description

<p>The chess knight has a <strong>unique movement</strong>&nbsp;,it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an <strong>L</strong>). The possible movements of chess knight are shown in this diagram:</p>

<p>A chess knight can move as indicated in the chess diagram below:</p>

<p>We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell&nbsp;(i.e. blue cell).</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="width: 402px; height: 402px;" /></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="width: 282px; height: 302px;" /></p>

<p>Given an integer <code>n</code>, return how many distinct phone numbers of length <code>n</code> we can dial.</p>

<p>You are allowed to place the knight on any numeric cell initially and then you should perform <code>n - 1</code> jumps to dial a number of length <code>n</code>. All jumps should be valid knight jumps.</p>

<p>As the answer may be very large, return the answer modulo <code>10<sup>9</sup> + 7</code>.</p>

## Examples

### Example 1:

```
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
```

### Example 2:

```
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
```

### Example 3:

```
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
```

## Constraints

- 1 &lt;= n &lt;= 5000
