# Dota2 Senate

**Difficulty:** Medium
**Topics:** String, Greedy, Queue
**Tags:** neetcode-250

**LeetCode:** [Problem 649](https://leetcode.com/problems/dota2-senate/description/)

## Problem Description

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators from both parties. Voting is a round-based procedure. In each round, each senator (in order) can exercise one right:

- **Ban one senator's right:** make another senator lose all rights in this and all following rounds.
- **Announce the victory:** if all senators who still have rights are from the same party, announce victory.

Given a string `senate` where `'R'` is Radiant and `'D'` is Dire, predict which party announces victory. Output `"Radiant"` or `"Dire"`. Every senator plays optimally for their own party.

## Examples

### Example 1:

```
Input: senate = "RD"
Output: "Radiant"
Explanation: The first senator (Radiant) bans the next senator's right in round 1. In round 2, the first senator announces victory.
```

### Example 2:

```
Input: senate = "RDD"
Output: "Dire"
Explanation: The first senator (Radiant) bans the second senator's right. The third senator (Dire) bans the first senator's right. In round 2, the third senator announces victory.
```

## Constraints

- n == senate.length
- 1 <= n <= 10^4
- senate[i] is either 'R' or 'D'.
