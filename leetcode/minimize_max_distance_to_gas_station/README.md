# Minimize Max Distance to Gas Station

**Difficulty:** Hard
**Topics:** Array, Binary Search
**Tags:** neetcode

**LeetCode:** [Problem 774](https://leetcode.com/problems/minimize-max-distance-to-gas-station/description/)

## Problem Description

You are given an integer array `stations` that represents the positions of the gas stations on the x-axis. You are also given an integer `k`.

You should add `k` new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let `penalty()` be the **maximum** distance between adjacent gas stations after adding the `k` new stations.

Return the smallest possible value of `penalty()`. Answers within `10^-6` of the actual answer will be accepted.

## Examples

### Example 1:

```
Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000
```

### Example 2:

```
Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000
```

## Constraints

- 10 <= stations.length <= 2000
- 0 <= stations[i] <= 10^8
- stations is sorted in a strictly increasing order.
- 1 <= k <= 10^6
