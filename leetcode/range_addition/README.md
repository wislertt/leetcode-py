# Range Addition

**Difficulty:** Medium
**Topics:** Array, Prefix Sum
**Tags:**

**LeetCode:** [Problem 370](https://leetcode.com/problems/range-addition/description/)

## Problem Description

You are given an integer `length` and an array `updates` where `updates[i] = [startIdx_i, endIdx_i, inc_i]`.

You have an array `arr` of length `length` with all zeros, and you have some operation to apply on `arr`. In the `i^th` operation, you should increment all the elements `arr[startIdx_i], arr[startIdx_i + 1], ..., arr[endIdx_i]` by `inc_i`.

Return `arr` _after applying all the_ `updates`.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0370.Range%20Addition/images/rangeadd-grid.jpg)

```
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
```

### Example 2:

```
Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]
```

## Constraints

- `1 <= length <= 10^5`
- `0 <= updates.length <= 10^4`
- `0 <= startIdx_i <= endIdx_i < length`
- `-1000 <= inc_i <= 1000`
