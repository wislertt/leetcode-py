# Russian Doll Envelopes

**Difficulty:** Hard
**Topics:** Array, Binary Search, Dynamic Programming, Sorting, Longest Increasing Subsequence
**Tags:** neetcode

**LeetCode:** [Problem 354](https://leetcode.com/problems/russian-doll-envelopes/description/)

## Problem Description

You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return _the maximum number of envelopes you can Russian doll (i.e., put one inside the other)_.

**Note:** You cannot rotate an envelope.

## Examples

### Example 1:

```
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

### Example 2:

```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
```

## Constraints

- 1 <= envelopes.length <= 10<sup>5</sup>
- `envelopes[i].length == 2`
- 1 <= w<sub>i</sub>, h<sub>i</sub> <= 10<sup>5</sup>
