# Minimum Number of Operations to Move All Balls to Each Box

**Difficulty:** Medium
**Topics:** Array, String, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 1769](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/)

## Problem Description

<p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>'0'</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>'1'</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

## Examples

### Example 1:

```
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
```

### Example 2:

```
Input: boxes = "001011"
Output: [11,8,5,4,3,4]
```

## Constraints

- n == boxes.length
- 1 <= n <= 2000
- boxes[i] is either '0' or '1'.
