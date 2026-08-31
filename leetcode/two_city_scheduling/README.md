# Two City Scheduling

**Difficulty:** Medium
**Topics:** Array, Greedy, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 1029](https://leetcode.com/problems/two-city-scheduling/description/)

## Problem Description

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `ith` person to city `a` is `aCosti`, and the cost of flying the `ith` person to city `b` is `bCosti`.

Return _the minimum cost to fly every person to a city_ such that exactly `n` people arrive in each city.

## Examples

### Example 1:

```
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

### Example 2:

```
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Explanation: For example, the way to achieve the minimum of 1859 is:
- Fly the 1st person (259, 770) to city A for 259.
- Fly the 2nd person (448, 54) to city B for 54.
- Fly the 3rd person (926, 667) to city B for 667.
- Fly the 4th person (184, 139) to city B for 139.
- Fly the 5th person (840, 118) to city B for 118.
- Fly the 6th person (577, 469) to city A for 577.
The total minimum cost is 1859.
```

### Example 3:

```
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
Explanation: The total minimum cost is 3086.
```

## Constraints

- `2 * n == costs.length`
- `2 <= costs.length <= 100`
- `costs.length` is even.
- `1 <= aCosti, bCosti <= 1000`
