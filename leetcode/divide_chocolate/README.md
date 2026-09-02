# Divide Chocolate

**Difficulty:** Hard
**Topics:** Array, Binary Search
**Tags:** neetcode

**LeetCode:** [Problem 1231](https://leetcode.com/problems/divide-chocolate/description/)

## Problem Description

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array `sweetness`.

You want to share the chocolate with your `k` friends so you start cutting the chocolate bar into `k + 1` pieces using `k` cuts, each piece consists of some <strong>consecutive</strong> chunks.

Being generous, you will eat the piece with the <strong>minimum total sweetness</strong> and give the other pieces to your friends.

Find the <strong>maximum total sweetness</strong> of the piece you can get by cutting the chocolate bar optimally.

## Examples

### Example 1:

```
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
```

### Example 2:

```
Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
```

### Example 3:

```
Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
```

## Constraints

- 0 <= k < sweetness.length <= 10<sup>4</sup>
- 1 <= sweetness[i] <= 10<sup>5</sup>
