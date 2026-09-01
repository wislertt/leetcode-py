# String Compression II

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1531](https://leetcode.com/problems/string-compression-ii/description/)

## Problem Description

<a href="http://en.wikipedia.org/wiki/Run-length_encoding">Run-length encoding</a> is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string <code>"aabccc"</code> we replace <code>"aa"</code> by <code>"a2"</code> and replace <code>"ccc"</code> by <code>"c3"</code>. Thus the compressed string becomes <code>"a2bc3"</code>.

Notice that in this problem, we are not adding <code>'1'</code> after single characters.

Given a string <code>s</code> and an integer <code>k</code>. You need to delete <strong>at most</strong> <code>k</code> characters from <code>s</code> such that the run-length encoded version of <code>s</code> has minimum length.

Find the <em>minimum length of the run-length encoded version of </em><code>s</code><em> after deleting at most </em><code>k</code><em> characters</em>.

## Examples

### Example 1:

```
Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
```

### Example 2:

```
Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
```

### Example 3:

```
Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
```

## Constraints

- `1 <= s.length <= 100`
- `0 <= k <= s.length`
- `s` contains only lowercase English letters.
