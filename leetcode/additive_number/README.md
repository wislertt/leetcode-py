# Additive Number

**Difficulty:** Medium
**Topics:** String, Backtracking
**Tags:**

**LeetCode:** [Problem 306](https://leetcode.com/problems/additive-number/description/)

## Problem Description

An <strong>additive number</strong> is a string whose digits can form an <strong>additive sequence</strong>.

<p>A valid <strong>additive sequence</strong> should contain <strong>at least</strong> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

<p>Given a string containing only digits, return <code>true</code> if it is an <strong>additive number</strong> or <code>false</code> otherwise.</p>

## Examples

### Example 1:

```
Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

### Example 2:

```
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
```

### Example 3:

```
Input: "1023"
Output: false
Explanation: No valid additive sequence exists.
```

## Constraints

- `1 <= num.length <= 35`
- `num` consists only of digits.

<p><strong>Note:</strong> Numbers in the additive sequence <strong>cannot</strong> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

**Follow up:** How would you handle overflow for very large input integers?
