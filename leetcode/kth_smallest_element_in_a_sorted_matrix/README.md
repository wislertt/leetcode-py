# Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium
**Topics:** Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
**Tags:**

**LeetCode:** [Problem 378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

## Problem Description

Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

## Examples

### Example 1:

```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

### Example 2:

```
Input: matrix = [[-5]], k = 1
Output: -5
```

## Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
- 1 <= k <= n2

**Follow up:**

- Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
- Could you solve the problem in O(n) time complexity?
