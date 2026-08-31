# Profitable Schemes

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
**Tags:** neetcode

**LeetCode:** [Problem 879](https://leetcode.com/problems/profitable-schemes/description/)

## Problem Description

There is a group of <code>n</code> members, and a list of various crimes they could commit. The <code>ith</code> crime generates a <code>profit[i]</code> and requires <code>group[i]</code> members to participate in it. If a member participates in one crime, that member can't participate in another crime.</p>

<p>Let's call a <em>profitable scheme</em> any subset of these crimes that generates at least <code>minProfit</code> profit, and the total number of members participating in that subset of crimes is at most <code>n</code>.</p>

<p>Return the number of schemes that can be chosen. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.

## Examples

### Example 1:

```
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
```

### Example 2:

```
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: Every subset of the crimes has total members at most 10 and profit at least 5,
and 7 subsets exist, so all of them are profitable schemes.
```

## Constraints

- 1 <= n <= 100
- 0 <= minProfit <= 100
- 1 <= group.length <= 100
- 1 <= group[i] <= 100
- profit.length == group.length
- 0 <= profit[i] <= 100
