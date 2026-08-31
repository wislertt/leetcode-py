# Repeated DNA Sequences

**Difficulty:** Medium
**Topics:** Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function
**Tags:** neetcode

**LeetCode:** [Problem 187](https://leetcode.com/problems/repeated-dna-sequences/description/)

## Problem Description

The **DNA sequence** is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`.

- For example, `"ACGAATTCCG"` is a **DNA sequence**.

When studying **DNA**, it is useful to identify repeated sequences within the DNA.

Given a string `s` that represents a DNA sequence, return all the **10-letter-long sequences** (substrings) that occur more than once in a DNA molecule. You may return the answer in **any order**.

## Examples

### Example 1:

```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
```

### Example 2:

```
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```

## Constraints

- 1 <= s.length <= 10<sup>5</sup>
- `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.
