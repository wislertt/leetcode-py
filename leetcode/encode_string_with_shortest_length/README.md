# Encode String with Shortest Length

**Difficulty:** Hard
**Topics:** String, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 471](https://leetcode.com/problems/encode-string-with-shortest-length/description/)

## Problem Description

Given a string `s`, encode the string such that its encoded length is the shortest.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. `k` should be a positive integer.

If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return **any of them**.

## Examples

### Example 1:

```
Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
```

### Example 2:

```
Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
```

### Example 3:

```
Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
```

## Constraints

- `1 <= s.length <= 150`
- `s` consists of only lowercase English letters.
