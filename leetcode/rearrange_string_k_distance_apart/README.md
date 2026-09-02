# Rearrange String k Distance Apart

**Difficulty:** Hard
**Topics:** Greedy, Hash Table, String, Counting, Sorting, Heap (Priority Queue)
**Tags:** neetcode

**LeetCode:** [Problem 358](https://leetcode.com/problems/rearrange-string-k-distance-apart/description/)

## Problem Description

Given a string `s` and an integer `k`, rearrange `s` such that the same characters are **at least** distance `k` from each other. If it is not possible to rearrange the string, return an empty string `""`.

## Examples

### Example 1:

```
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
```

### Example 2:

```
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
```

### Example 3:

```
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of only lowercase English letters.
- `0 <= k <= s.length`
