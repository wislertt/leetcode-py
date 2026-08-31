# The Earliest Moment When Everyone Become Friends

**Difficulty:** Medium
**Topics:** Array, Union Find, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 1101](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/)

## Problem Description

There are `n` people in a social group labeled from `0` to `n - 1`. You are given an array `logs` where `logs[i] = [timestampi, xi, yi]` indicates that `xi` and `yi` will be friends at the time `timestampi`.

Friendship is **symmetric**. That means if `a` is friends with `b`, then `b` is friends with `a`. Also, person `a` is **acquainted** with a person `b` if `a` is friends with `b`, or `a` is a friend of someone acquainted with `b`.

Return _the earliest time for which every person became acquainted with every other person_. If there is no such earliest time, return `-1`.

## Examples

### Example 1:

```
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: After the event at timestamp 20190301, every person becomes acquainted with every other person.
```

### Example 2:

```
Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
```

## Constraints

- 2 <= n <= 100
- 1 <= logs.length <= 10^4
- logs[i].length == 3
- 0 <= timestampi <= 10^9
- 0 <= xi, yi <= n - 1
- xi != yi
- All the values timestampi are unique.
- All the pairs (xi, yi) occur at most one time in the input.
