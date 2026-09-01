# Maximum Candies Allocated to K Children

**Difficulty:** Medium
**Topics:** Array, Binary Search
**Tags:** neetcode

**LeetCode:** [Problem 2226](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/)

## Problem Description

You are given a <strong>0-indexed</strong> integer array <code>candies</code>. Each element in the array denotes a pile of candies of size <code>candies[i]</code>. You can divide each pile into any number of <strong>sub piles</strong>, but you <strong>cannot</strong> merge two piles together.

You are also given an integer <code>k</code>. You should allocate piles of candies to <code>k</code> children such that each child gets the <strong>same</strong> number of candies. Each child can be allocated candies from <strong>only one</strong> pile of candies and some piles of candies may go unused.

Return <em>the <strong>maximum number of candies</strong> each child can get.</em>

## Examples

### Example 1:

```
Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
```

### Example 2:

```
Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
```

## Constraints

- 1 <= candies.length <= 10<sup>5</sup>
- 1 <= candies[i] <= 10<sup>7</sup>
- 1 <= k <= 10<sup>12</sup>
