# Maximum Total Importance of Roads

**Difficulty:** Medium
**Topics:** Greedy, Graph Theory, Sorting, Heap (Priority Queue)
**Tags:** neetcode

**LeetCode:** [Problem 2285](https://leetcode.com/problems/maximum-total-importance-of-roads/description/)

## Problem Description

You are given an integer `n` denoting the number of cities in a country. The cities are numbered from `0` to `n - 1`.

You are also given a 2D integer array `roads` where `roads[i] = [a<sub>i</sub>, b<sub>i</sub>]` denotes that there exists a **bidirectional** road connecting cities `a<sub>i</sub>` and `b<sub>i</sub>`.

You need to assign each city with an integer value from `1` to `n`, where each value can only be used **once**. The **importance** of a road is then defined as the **sum** of the values of the two cities it connects.

Return _the **maximum total importance** of all roads possible after assigning the values optimally._

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/04/07/ex1drawio.png)

```
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The assigned values are [2,4,5,3,1].
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2022/04/07/ex2drawio.png)

```
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The assigned values are [4,3,2,5,1].
The total importance of all roads is 9 + 3 + 8 = 20.
```

## Constraints

- 2 <= n <= 5 * 10<sup>4</sup>
- 1 <= roads.length <= 5 * 10<sup>4</sup>
- roads[i].length == 2
- 0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1
- a<sub>i</sub> != b<sub>i</sub>
- There are no duplicate roads.
