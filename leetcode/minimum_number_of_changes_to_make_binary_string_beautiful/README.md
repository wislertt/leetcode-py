# Minimum Number of Changes to Make Binary String Beautiful

**Difficulty:** Medium
**Topics:** String
**Tags:** neetcode

**LeetCode:** [Problem 2914](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/)

## Problem Description

<p>You are given a <strong>0-indexed</strong> binary string <code>s</code> having an even length.</p>

<p>A string is <strong>beautiful</strong> if it&#39;s possible to partition it into one or more substrings such that:</p>

<ul>
	<li>Each substring has an <strong>even length</strong>.</li>
	<li>Each substring contains <strong>only</strong> <code>1</code>&#39;s or <strong>only</strong> <code>0</code>&#39;s.</li>
</ul>

<p>You can change any character in <code>s</code> to <code>0</code> or <code>1</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of changes required to make the string </em><code>s</code> <em>beautiful</em>.</p>

## Examples

### Example 1:

```
Input: s = "1001"
Output: 2
```

**Explanation:** We change s[1] to 1 and s[3] to 0 to get string "1100".
It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

### Example 2:

```
Input: s = "10"
Output: 1
```

**Explanation:** We change s[1] to 1 to get string "11".
It can be seen that the string "11" is beautiful because we can partition it into "11".
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.

### Example 3:

```
Input: s = "0000"
Output: 0
```

**Explanation:** We don&#39;t need to make any changes as the string "0000" is beautiful already.

## Constraints

- `2 <= s.length <= 10^5`
- `s` has an even length.
- `s[i]` is either `'0'` or `'1'`.
