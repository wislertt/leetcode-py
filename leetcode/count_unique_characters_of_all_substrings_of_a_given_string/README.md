# Count Unique Characters of All Substrings of a Given String

**Difficulty:** Hard
**Topics:** Hash Table, String, Dynamic Programming
**Tags:**

**LeetCode:** [Problem 828](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/)

## Problem Description

<p>Let's define a function <code>countUniqueChars(s)</code> that returns the number of unique characters in <code>s</code>.</p>

<ul>
	<li>For example, calling <code>countUniqueChars(s)</code> if <code>s = "LEETCODE"</code> then <code>"L"</code>, <code>"T"</code>, <code>"C"</code>, <code>"O"</code>, <code>"D"</code> are the unique characters since they appear only once in <code>s</code>, therefore <code>countUniqueChars(s) = 5</code>.</li>
</ul>

<p>Given a string <code>s</code>, return the sum of <code>countUniqueChars(t)</code> where <code>t</code> is a substring of <code>s</code>. The test cases are generated such that the answer fits in a 32-bit integer.</p>

<p>Notice that some substrings can be repeated so in this case you have to count the repeated ones too.</p>

## Examples

### Example 1:

```
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
```

### Example 2:

```
Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
```

### Example 3:

```
Input: s = "LEETCODE"
Output: 92
```

## Constraints

- 1 <= s.length <= 10^5
- s consists of uppercase English letters only.
