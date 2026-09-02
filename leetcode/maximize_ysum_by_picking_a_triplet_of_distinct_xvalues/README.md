# Maximize Y-Sum by Picking a Triplet of Distinct X-Values

**Difficulty:** Medium
**Topics:** Array, Hash Table, Greedy, Sorting, Heap (Priority Queue)
**Tags:** neetcode

**LeetCode:** [Problem 3572](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/description/)

## Problem Description

You are given two integer arrays <code>x</code> and <code>y</code>, each of length <code>n</code>. You must choose three <strong>distinct</strong> indices <code>i</code>, <code>j</code>, and <code>k</code> such that:

<ul>
	<li><code>x[i] != x[j]</code></li>
	<li><code>x[j] != x[k]</code></li>
	<li><code>x[k] != x[i]</code></li>
</ul>

Your goal is to <strong>maximize</strong> the value of <code>y[i] + y[j] + y[k]</code> under these conditions. Return the <strong>maximum</strong> possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

## Examples

### Example 1:

```
Input: x = [1,2,1,3,2], y = [5,3,4,6,2]
Output: 14
Explanation: Choose i = 0 (x[i] = 1, y[i] = 5), j = 1 (x[j] = 2, y[j] = 3), k = 3 (x[k] = 3, y[k] = 6). All three values chosen from x are distinct. 5 + 3 + 6 = 14 is the maximum we can obtain.
```

### Example 2:

```
Input: x = [1,2,1,2], y = [4,5,6,7]
Output: -1
Explanation: There are only two distinct values in x. Hence, the output is -1.
```

## Constraints

- n == x.length == y.length
- 3 <= n <= 10^5
- 1 <= x[i], y[i] <= 10^6
