# Number of Flowers in Full Bloom

**Difficulty:** Hard
**Topics:** Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set
**Tags:** neetcode

**LeetCode:** [Problem 2251](https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/)

## Problem Description

You are given a **0-indexed** 2D integer array `flowers`, where `flowers[i] = [starti, endi]` means the `ith` flower will be in **full bloom** from `starti` to `endi` (**inclusive**). You are also given a **0-indexed** integer array `people` of size `n`, where `people[i]` is the time that the `ith` person will arrive to see the flowers.

Return an integer array `answer` of size `n`, where `answer[i]` is the **number** of flowers that are in full bloom when the `ith` person arrives.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg)

```
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
Output: [1,2,2,2]
```

**Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive. For each person, we return the number of flowers in full bloom during their arrival.

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg)

```
Input: flowers = [[1,10],[3,3]], people = [3,3,2]
Output: [2,2,1]
```

**Explanation:** The figure above shows the times when the flowers are in full bloom and when the people arrive. For each person, we return the number of flowers in full bloom during their arrival.

## Constraints

- `1 <= flowers.length <= 5 * 10^4`
- `flowers[i].length == 2`
- `1 <= starti <= endi <= 10^9`
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= 10^9`
