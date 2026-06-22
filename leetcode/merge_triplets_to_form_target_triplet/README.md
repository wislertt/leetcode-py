# Merge Triplets to Form Target Triplet

**Difficulty:** Medium
**Topics:** Array, Greedy
**Tags:** neetcode-150

**LeetCode:** [Problem 1899](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/)

## Problem Description

A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [a_i, b_i, c_i]` describes the `i^th` **triplet**. You are also given an integer array `target = [x, y, z]` that describes the **triplet** you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):

- Choose two indices (**0-indexed**) `i` and `j` (`i != j`) and **update** `triplets[j]` to become `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

Return `true` _if it is possible to obtain the_ `target` _ **triplet** `[x, y, z]` as an **element** of_ `triplets`, or `false` otherwise.

## Examples

### Example 1:

```
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]].
The target triplet [2,7,5] is now an element of triplets.
```

### Example 2:

```
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
```

### Example 3:

```
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
```

## Constraints

- 1 <= triplets.length <= 10^5
- `triplets[i].length == target.length == 3`
- 1 <= a_i, b_i, c_i, x, y, z <= 1000
