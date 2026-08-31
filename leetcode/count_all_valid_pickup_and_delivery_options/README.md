# Count All Valid Pickup and Delivery Options

**Difficulty:** Hard
**Topics:** Math, Dynamic Programming, Combinatorics
**Tags:** neetcode

**LeetCode:** [Problem 1359](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/)

## Problem Description

Given <code>n</code> orders, each order consists of a pickup and a delivery service.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of&nbsp;pickup(i).&nbsp;

Since the answer&nbsp;may be too large,&nbsp;return it modulo<code> 10<sup>9</sup> + 7</code>.

## Examples

### Example 1:

```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

### Example 2:

```
Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

### Example 3:

```
Input: n = 3
Output: 90
```

## Constraints

- 1 <= n <= 500
