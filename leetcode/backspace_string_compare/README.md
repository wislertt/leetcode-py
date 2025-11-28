# Backspace String Compare

**Difficulty:** Easy
**Topics:** Two Pointers, String, Stack, Simulation
**Tags:** grind-75

**LeetCode:** [Problem 844](https://leetcode.com/problems/backspace-string-compare/description/)


## Problem Description

Given two strings s and t, return true if they are equal when both are typed into empty text editors. &#39;#&#39; means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

&nbsp;
Example 1:


Input: s = &quot;ab#c&quot;, t = &quot;ad#c&quot;
Output: true
Explanation: Both s and t become &quot;ac&quot;.


Example 2:


Input: s = &quot;ab##&quot;, t = &quot;c#d#&quot;
Output: true
Explanation: Both s and t become &quot;&quot;.


Example 3:


Input: s = &quot;a#c&quot;, t = &quot;b&quot;
Output: false
Explanation: s becomes &quot;c&quot; while t becomes &quot;b&quot;.


&nbsp;
Constraints:


	1 &lt;= s.length, t.length &lt;= 200
	s and t only contain lowercase letters and &#39;#&#39; characters.


&nbsp;
Follow up: Can you solve it in O(n) time and O(1) space?

## Examples

### Example 1:

Input: s = &quot;ab#c&quot;, t = &quot;ad#c&quot;
Output: true
Explanation: Both s and t become &quot;ac&quot;.


Example 2:


Input: s = &quot;ab##&quot;, t = &quot;c#d#&quot;
Output: true
Explanation: Both s and t become &quot;&quot;.


Example 3:


Input: s = &quot;a#c&quot;, t = &quot;b&quot;
Output: false
Explanation: s becomes &quot;c&quot; while t becomes &quot;b&quot;.

## Constraints

- 1 &lt;= s.length, t.length &lt;= 200
- s and t only contain lowercase letters and &#39;#&#39; characters.


