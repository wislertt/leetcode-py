# Capacity To Ship Packages Within D Days

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Tags:** neetcode-250

**LeetCode:** [Problem 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)

## Problem Description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i^th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

## Examples

### Example 1:

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
```

### Example 2:

```
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

### Example 3:

```
Input: weights = [1,2,3,1,1], days = 4
Output: 3
```

## Constraints

- 1 <= days <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500
