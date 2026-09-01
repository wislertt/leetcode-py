# Kth Distinct String in an Array

**Difficulty:** Easy
**Topics:** Array, Hash Table, String, Counting
**Tags:** neetcode

**LeetCode:** [Problem 2053](https://leetcode.com/problems/kth-distinct-string-in-an-array/description/)

## Problem Description

A <strong>distinct string</strong> is a string that is present only <strong>once</strong> in an array.

Given an array of strings <code>arr</code>, and an integer <code>k</code>, return <em>the </em><code>k<sup>th</sup></code><em> <strong>distinct string</strong> present in </em><code>arr</code>. If there are <strong>fewer</strong> than <code>k</code> distinct strings, return <em>an <strong>empty string </strong></em><code>&quot;&quot;</code>.

Note that the strings are considered in the <strong>order in which they appear</strong> in the array.

## Examples

### Example 1:

```
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
```

### Example 2:

```
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
```

### Example 3:

```
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
```

## Constraints

- `1 <= k <= arr.length <= 1000`
- `1 <= arr[i].length <= 5`
- `arr[i]` consists of lowercase English letters.
