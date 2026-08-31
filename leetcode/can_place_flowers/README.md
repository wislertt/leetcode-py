# Can Place Flowers

**Difficulty:** Easy
**Topics:** Array, Greedy
**Tags:** neetcode

**LeetCode:** [Problem 605](https://leetcode.com/problems/can-place-flowers/description/)

## Problem Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` _if_ `n` _new flowers can be planted in the_ `flowerbed` _without violating the no-adjacent-flowers rule and_ `false` _otherwise_.

## Examples

### Example 1:

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

### Example 2:

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

## Constraints

- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length
