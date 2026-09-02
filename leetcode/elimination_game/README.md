# Elimination Game

**Difficulty:** Medium
**Topics:** Math, Recursion
**Tags:**

**LeetCode:** [Problem 390](https://leetcode.com/problems/elimination-game/description/)

## Problem Description

You have a list <code>arr</code> of all integers in the range <code>[1, n]</code> sorted in a strictly increasing order. Apply the following algorithm on <code>arr</code>:

<ul>
	<li>Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.</li>
	<li>Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.</li>
	<li>Keep repeating the steps again, alternating left to right and right to left, until a single number remains.</li>
</ul>

<p>Given the integer <code>n</code>, return <em>the last number that remains in</em> <code>arr</code>.</p>

## Examples

### Example 1:

```
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
```

### Example 2:

```
Input: n = 1
Output: 1
```

## Constraints

- 1 <= n <= 10<sup>9</sup>
