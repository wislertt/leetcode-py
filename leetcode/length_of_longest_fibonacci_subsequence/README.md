# Length of Longest Fibonacci Subsequence

**Difficulty:** Medium
**Topics:** Array, Hash Table, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 873](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/)

## Problem Description

A sequence <code>x1, x2, ..., xn</code> is <em>Fibonacci-like</em> if:</p>

<ul>
	<li><code>n &gt;= 3</code></li>
	<li><code>xi + xi+1 == xi+2</code> for all <code>i + 2 &lt;= n</code></li>
</ul>

<p>Given a <strong>strictly increasing</strong> array <code>arr</code> of positive integers forming a sequence, return <em>the length of the longest Fibonacci-like subsequence of</em> <code>arr</code>. If one does not exist, return <code>0</code>.</p>

<p>A <em>subsequence</em> is derived from another sequence <code>arr</code> by deleting any number of elements (including none) from <code>arr</code>, without changing the order of the remaining elements. For example, <code>[3, 5, 8]</code> is a subsequence of <code>[3, 4, 5, 6, 7, 8]</code>.

## Examples

### Example 1:

```
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is Fibonacci-like: [1,2,3,5,8].
```

### Example 2:

```
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is Fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
```

## Constraints

- 3 <= arr.length <= 1000
- 1 <= arr[i] < arr[i + 1] <= 10^9
