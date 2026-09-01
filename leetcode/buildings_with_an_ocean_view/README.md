# Buildings With an Ocean View

**Difficulty:** Medium
**Topics:** Array, Stack, Monotonic Stack
**Tags:** neetcode

**LeetCode:** [Problem 1762](https://leetcode.com/problems/buildings-with-an-ocean-view/description/)

## Problem Description

<p>There are <code>n</code> buildings in a line. You are given an integer array <code>heights</code> of size <code>n</code> that represents the heights of the buildings in the line.</p>

<p>The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a <strong>smaller</strong> height.</p>

<p>Return a list of indices <strong>(0-indexed)</strong> of buildings that have an ocean view, sorted in increasing order.</p>

## Examples

### Example 1:

```
Input: heights = [4,2,3,1]
Output: [0,2,3]
```

**Explanation:** Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

### Example 2:

```
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
```

**Explanation:** All the buildings have an ocean view.

### Example 3:

```
Input: heights = [1,3,2,4]
Output: [3]
```

**Explanation:** Only building 3 has an ocean view.

## Constraints

- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9
