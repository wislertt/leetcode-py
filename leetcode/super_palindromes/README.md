# Super Palindromes

**Difficulty:** Hard
**Topics:** Math, String, Enumeration
**Tags:**

**LeetCode:** [Problem 906](https://leetcode.com/problems/super-palindromes/description/)

## Problem Description

Let's say a positive integer is a **super-palindrome** if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers <code>left</code> and <code>right</code> represented as strings, return <em>the number of <strong>super-palindromes</strong> integers in the inclusive range</em> <code>[left, right]</code>.

## Examples

### Example 1:

```
Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
```

### Example 2:

```
Input: left = "1", right = "2"
Output: 1
```

## Constraints

- 1 &lt;= left.length, right.length &lt;= 18
- left and right consist of only digits.
- left and right cannot have leading zeros.
- left and right represent integers in the range [1, 10<sup>18</sup> - 1].
- left is less than or equal to right.
