# Friends Of Appropriate Ages

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search, Sorting
**Tags:**

**LeetCode:** [Problem 825](https://leetcode.com/problems/friends-of-appropriate-ages/description/)

## Problem Description

<p>There are <code>n</code> persons on a social media website. You are given an integer array <code>ages</code> where <code>ages[i]</code> is the age of the <code>i<sup>th</sup></code> person.</p>

<p>A Person <code>x</code> will not send a friend request to a person <code>y</code> (<code>x != y</code>) if any of the following conditions is true:</p>

<ul>
	<li><code>age[y] &lt;= 0.5 * age[x] + 7</code></li>
	<li><code>age[y] &gt; age[x]</code></li>
	<li><code>age[y] &gt; 100 &amp;&amp; age[x] &lt; 100</code></li>
</ul>

<p>Otherwise, <code>x</code> will send a friend request to <code>y</code>.</p>

<p>Note that if <code>x</code> sends a request to <code>y</code>, <code>y</code> will not necessarily send a request to <code>x</code>. Also, a person will not send a friend request to themself.</p>

<p>Return <em>the total number of friend requests made</em>.</p>

<p>&nbsp;</p>

## Examples

### Example 1:

```
Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
```

### Example 2:

```
Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```

### Example 3:

```
Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
```

## Constraints

- n == ages.length
- 1 <= n <= 2 * 10^4
- 1 <= ages[i] <= 120
