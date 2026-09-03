# Sum of Even Numbers After Queries

**Difficulty:** Medium
**Topics:** Array, Simulation
**Tags:**

**LeetCode:** [Problem 985](https://leetcode.com/problems/sum-even-after-queries/description/)

## Problem Description

You are given an integer array `nums` and an array `queries` where `queries[i] = [val_i, index_i]`.

For each query `i`, first, apply `nums[index_i] = nums[index_i] + val_i`, then print the sum of the even values of `nums`.

Return an integer array `answer` where `answer[i]` is the answer to the `i-th` query.

## Examples

### Example 1:

```
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
```

### Example 2:

```
Input: nums = [1], queries = [[4,0]]
Output: [0]
```

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- 1 <= queries.length <= 10^4
- -10^4 <= val_i <= 10^4
- 0 <= index_i < nums.length
