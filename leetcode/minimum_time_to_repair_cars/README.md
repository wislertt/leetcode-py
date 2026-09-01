# Minimum Time to Repair Cars

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Tags:** neetcode

**LeetCode:** [Problem 2594](https://leetcode.com/problems/minimum-time-to-repair-cars/description/)

## Problem Description

You are given an integer array <code>ranks</code> representing the <strong>ranks</strong> of some mechanics. <code>ranks[i]</code> is the rank of the <code>i<sup>th</sup></code> mechanic. A mechanic with a rank <code>r</code> can repair <code>n</code> cars in <code>r * n<sup>2</sup></code> minutes.

You are also given an integer <code>cars</code> representing the total number of cars waiting in the garage to be repaired.

Return <em>the <strong>minimum</strong> time taken to repair all the cars.</em>

<strong>Note:</strong> All the mechanics can repair the cars simultaneously.

## Examples

### Example 1:

```
Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.
```

### Example 2:

```
Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation:
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.
```

## Constraints

- 1 <= ranks.length <= 10<sup>5</sup>
- 1 <= ranks[i] <= 100
- 1 <= cars <= 10<sup>6</sup>
