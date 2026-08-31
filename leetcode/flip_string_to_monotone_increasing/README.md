# Flip String to Monotone Increasing

**Difficulty:** Medium
**Topics:** String, Dynamic Programming, Greedy
**Tags:** neetcode

**LeetCode:** [Problem 926](https://leetcode.com/problems/flip-string-to-monotone-increasing/description/)

## Problem Description

<p>A binary string is monotone increasing if it consists of some number of <code>0</code>&#39;s (possibly none), followed by some number of <code>1</code>&#39;s (also possibly none).</p>

<p>You are given a binary string <code>s</code>. You can flip <code>s[i]</code> changing it from <code>0</code> to <code>1</code> or from <code>1</code> to <code>0</code>.</p>

<p>Return <em>the minimum number of flips to make </em><code>s</code><em> monotone increasing</em>.</p>

## Examples

### Example 1:

```
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
```

### Example 2:

```
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
```

### Example 3:

```
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
```

## Constraints

- 1 &lt;= s.length &lt;= 10^5
- s[i] is either &#39;0&#39; or &#39;1&#39;.
