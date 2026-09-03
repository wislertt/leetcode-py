# Most Stones Removed with Same Row or Column

**Difficulty:** Medium
**Topics:** Hash Table, Depth-First Search, Union-Find, Graph Theory, Bipartite Graph
**Tags:**

**LeetCode:** [Problem 947](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/)

## Problem Description

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [x<sub>i</sub>, y<sub>i</sub>]` represents the location of the `i<sup>th</sup>` stone, return _the largest possible number of stones that can be removed_.

## Examples

### Example 1:

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

### Example 2:

```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```

### Example 3:

```
Input: stones = [[0,0]]
Output: 0
```

## Constraints

- 1 <= stones.length <= 1000
- 0 <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup>
- No two stones are at the same coordinate point.
