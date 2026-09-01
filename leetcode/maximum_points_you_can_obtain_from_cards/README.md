# Maximum Points You Can Obtain from Cards

**Difficulty:** Medium
**Topics:** Array, Sliding Window, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/)

## Problem Description

There are several cards <strong>arranged in a row</strong>, and each card has an associated number of points. The points are given in the integer array <code>cardPoints</code>.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly <code>k</code> cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array <code>cardPoints</code> and the integer <code>k</code>, return the <em>maximum score</em> you can obtain.

## Examples

### Example 1:

```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
```

**Explanation:** After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

### Example 2:

```
Input: cardPoints = [2,2,2], k = 2
Output: 4
```

**Explanation:** Regardless of which two cards you take, your score will always be 4.

### Example 3:

```
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
```

**Explanation:** You have to take all the cards. Your score is the sum of points of all cards.

## Constraints

- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`
