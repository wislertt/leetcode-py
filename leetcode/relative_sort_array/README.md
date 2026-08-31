# Relative Sort Array

**Difficulty:** Easy
**Topics:** Array, Hash Table, Counting Sort, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 1122](https://leetcode.com/problems/relative-sort-array/description/)

## Problem Description

Given two arrays <code>arr1</code> and <code>arr2</code>, the elements of <code>arr2</code> are distinct, and all elements in <code>arr2</code> are also in <code>arr1</code>.

Sort the elements of <code>arr1</code> such that the relative ordering of items in <code>arr1</code> are the same as in <code>arr2</code>. Elements that do not appear in <code>arr2</code> should be placed at the end of <code>arr1</code> in <strong>ascending</strong> order.

## Examples

### Example 1:

```
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
```

### Example 2:

```
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
```

## Constraints

- <code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code>
- <code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code>
- All the elements of <code>arr2</code> are <strong>distinct</strong>.
- Each&nbsp;<code>arr2[i]</code> is in <code>arr1</code>.
