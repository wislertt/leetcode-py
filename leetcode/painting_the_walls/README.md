# Painting the Walls

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 2742](https://leetcode.com/problems/painting-the-walls/description/)

## Problem Description

You are given two **0-indexed** integer arrays, `cost` and `time`, of size `n` representing the costs and the time taken to paint `n` different walls respectively. There are two painters available:

- A **paid painter** that paints the `i<sup>th</sup>` wall in `time[i]` units of time and takes `cost[i]` units of money.
- A **free painter** that paints **any** wall in `1` unit of time at a cost of `0`. But the free painter can only be used if the paid painter is already **occupied**.

Return _the minimum amount of money required to paint the `n` walls_.

## Examples

### Example 1:

```
Input: cost = [1,2,3,2], time = [1,2,3,2]
Output: 3
Explanation: The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time; meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. Thus, the total cost is 1 + 2 = 3.
```

### Example 2:

```
Input: cost = [2,3,4,2], time = [1,1,1,1]
Output: 4
Explanation: The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. Thus, the total cost is 2 + 2 = 4.
```

## Constraints

- `1 <= cost.length <= 500`
- `cost.length == time.length`
- `1 <= cost[i] <= 10^6`
- `1 <= time[i] <= 500`
