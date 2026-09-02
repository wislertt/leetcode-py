# Minimum Length of String After Deleting Similar Ends

**Difficulty:** Medium
**Topics:** Two Pointers, String
**Tags:** neetcode

**LeetCode:** [Problem 1750](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/)

## Problem Description

<p>Given a string <code>s</code> consisting only of characters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code>. You are asked to apply the following algorithm on the string any number of times:</p>

<ol>
	<li>Pick a <strong>non-empty</strong> prefix from the string <code>s</code> where all the characters in the prefix are equal.</li>
	<li>Pick a <strong>non-empty</strong> suffix from the string <code>s</code> where all the characters in this suffix are equal.</li>
	<li>The prefix and the suffix should not intersect at any index.</li>
	<li>The characters from the prefix and suffix must be the same.</li>
	<li>Delete both the prefix and the suffix.</li>
</ol>

<p>Return <em>the <strong>minimum length</strong> of </em><code>s</code> <em>after performing the above operation any number of times (possibly zero times)</em>.</p>

## Examples

### Example 1:

```
Input: s = "ca"
Output: 2
```

**Explanation:** You can't remove any characters, so the string stays as is.

### Example 2:

```
Input: s = "cabaabac"
Output: 0
```

**Explanation:** An optimal sequence of operations is:

- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

### Example 3:

```
Input: s = "aabccabba"
Output: 3
```

**Explanation:** An optimal sequence of operations is:

- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists only of characters `'a'`, `'b'`, and `'c'`.
