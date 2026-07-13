# IPO

**Difficulty:** Hard
**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)
**Tags:** neetcode-250

**LeetCode:** [Problem 502](https://leetcode.com/problems/ipo/description/)

## Problem Description

Suppose LeetCode will start its IPO soon. To sell a good price of its shares, it can only finish at most `k` distinct projects before the IPO. Help LeetCode maximize its total capital.

You are given `n` projects where the `ith` project has a pure profit `profits[i]` and a minimum capital `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you obtain its pure profit, which is added to your total capital.

Pick a list of **at most** `k` distinct projects to **maximize your final capital**, and return the final maximized capital.

## Examples

### Example 1:

```
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Start with capital 0, only project 0 is affordable. Finish it -> capital 1. Now projects 1 and 2 are affordable; finish project 2 -> capital 4.
```

### Example 2:

```
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
```

## Constraints

- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profits.length
- n == capital.length
- 1 <= n <= 10^5
- 0 <= profits[i] <= 10^4
- 0 <= capital[i] <= 10^9
