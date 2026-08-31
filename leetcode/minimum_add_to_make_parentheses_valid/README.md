# Minimum Add to Make Parentheses Valid

**Difficulty:** Medium
**Topics:** String, Stack, Greedy
**Tags:** neetcode

**LeetCode:** [Problem 921](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)

## Problem Description

<p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = &quot;()))&quot;</code>, you can insert an opening parenthesis to be <code>&quot;(()))&quot;</code> or a closing parenthesis to be <code>&quot;())))&quot;</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

## Examples

### Example 1:

```
Input: s = "())"
Output: 1
```

### Example 2:

```
Input: s = "((("
Output: 3
```

## Constraints

- 1 &lt;= s.length &lt;= 1000
- s[i] is either &#39;(&#39; or &#39;)&#39;.
