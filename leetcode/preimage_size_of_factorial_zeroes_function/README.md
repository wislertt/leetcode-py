# Preimage Size of Factorial Zeroes Function

**Difficulty:** Hard
**Topics:** Math, Binary Search
**Tags:**

**LeetCode:** [Problem 793](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/description/)

## Problem Description

Let <code>f(x)</code> be the number of zeroes at the end of <code>x!</code>. Recall that <code>x! = 1 * 2 * 3 * ... * x</code> and by convention, <code>0! = 1</code>.

<ul>
	<li>For example, <code>f(3) = 0</code> because <code>3! = 6</code> has no zeroes at the end, while <code>f(11) = 2</code> because <code>11! = 39916800</code> has two zeroes at the end.</li>
</ul>

<p>Given an integer <code>k</code>, return <em>the number of non-negative integers</em> <code>x</code> <em>have the property that</em> <code>f(x) = k</code>.</p>

## Examples

### Example 1:

```
Input: k = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
```

### Example 2:

```
Input: k = 5
Output: 0
Explanation: There is no x such that x! ends in k = 5 zeroes.
```

### Example 3:

```
Input: k = 3
Output: 5
```

## Constraints

- 0 <= k <= 10^9
