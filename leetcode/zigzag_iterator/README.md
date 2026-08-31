# Zigzag Iterator

**Difficulty:** Medium
**Topics:** Design, Queue, Array, Iterator
**Tags:** neetcode

**LeetCode:** [Problem 281](https://leetcode.com/problems/zigzag-iterator/description/)

## Problem Description

Given two vectors of integers `v1` and `v2`, implement an iterator to return their elements alternately.

Implement the `ZigzagIterator` class:

- `ZigzagIterator(List<int> v1, List<int> v2)` initializes the object with the two vectors `v1` and `v2`.
- `boolean hasNext()` returns `true` if the iterator still has elements, and `false` otherwise.
- `int next()` returns the current element of the iterator and moves the iterator to the next element.

**Follow up:** What if you are given `k` vectors? How well can your code be extended to such cases?

## Examples

### Example 1:

```
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
```

### Example 2:

```
Input: v1 = [1], v2 = []
Output: [1]
```

### Example 3:

```
Input: v1 = [], v2 = [1]
Output: [1]
```

## Constraints

- `0 <= v1.length, v2.length <= 1000`
- `1 <= v1.length + v2.length <= 2000`
- `-10^9 <= v1[i], v2[i] <= 10^9`
