# Handshakes That Don't Cross

**Difficulty:** Hard
**Topics:** Math, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1259](https://leetcode.com/problems/handshakes-that-dont-cross/description/)

## Problem Description

You are given an **even** number of people `numPeople` that stand around a circle and each person shakes hands with someone else so that there are `numPeople / 2` handshakes total.

Return _the number of ways these handshakes could occur such that none of the handshakes cross_.

Since the answer could be very large, return it **modulo** `10<sup>9</sup> + 7`.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1259.Handshakes%20That%20Don%27t%20Cross/images/5125_example_2.png)

```
Input: numPeople = 4
Output: 2
```

**Explanation:** There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1259.Handshakes%20That%20Don%27t%20Cross/images/5125_example_3.png)

```
Input: numPeople = 6
Output: 5
```

## Constraints

- `2 <= numPeople <= 1000`
- `numPeople` is even.
