# Minimum Increment to Make Array Unique

**Difficulty:** Medium
**Topics:** Array, Greedy, Sorting, Counting
**Tags:** neetcode

**LeetCode:** [Problem 945](https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/)

## Problem Description

<p>You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; nums.length</code> and increment <code>nums[i]</code> by <code>1</code>.</p>

<p>Return <em>the minimum number of moves to make every value in </em><code>nums</code><em> <strong>unique</strong></em>.</p>

<p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

## Examples

### Example 1:

```
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
```

### Example 2:

```
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
```

## Constraints

- 1 &lt;= nums.length &lt;= 10^5
- 0 &lt;= nums[i] &lt;= 10^5
