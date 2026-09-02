# Heaters

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Sorting
**Tags:**

**LeetCode:** [Problem 475](https://leetcode.com/problems/heaters/description/)

## Problem Description

Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of `houses` and `heaters` on a horizontal line, return _the minimum radius standard of heaters so that those heaters could cover all houses._

**Notice** that all the `heaters` follow your radius standard, and the warm radius will be the same.

## Examples

### Example 1:

```
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
```

### Example 2:

```
Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heaters were placed at positions 1 and 4. We need to use a radius 1 standard, then all the houses can be warmed.
```

### Example 3:

```
Input: houses = [1,5], heaters = [2]
Output: 3
```

## Constraints

- `1 <= houses.length, heaters.length <= 3 * 10^4`
- `1 <= houses[i], heaters[i] <= 10^9`
