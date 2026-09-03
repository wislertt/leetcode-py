# Card Flipping Game

**Difficulty:** Medium
**Topics:** Array, Hash Table
**Tags:**

**LeetCode:** [Problem 822](https://leetcode.com/problems/card-flipping-game/description/)

## Problem Description

You are given two <strong>0-indexed</strong> integer arrays <code>fronts</code> and <code>backs</code> of length <code>n</code>, where the <code>i<sup>th</sup></code> card has the positive integer <code>fronts[i]</code> printed on the front and <code>backs[i]</code> printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

After flipping the cards, an integer is considered <strong>good</strong> if it is facing down on some card and <strong>not</strong> facing up on any card.

Return <em>the minimum possible good integer after flipping the cards</em>. If there are no good integers, return <code>0</code>.

## Examples

### Example 1:

```
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation:
If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
2 is the minimum good integer as it appears facing down but not facing up.
It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.
```

### Example 2:

```
Input: fronts = [1], backs = [1]
Output: 0
Explanation:
There are no good integers no matter how we flip the cards, so we return 0.
```

## Constraints

- n == fronts.length == backs.length
- 1 <= n <= 1000
- 1 <= fronts[i], backs[i] <= 2000
