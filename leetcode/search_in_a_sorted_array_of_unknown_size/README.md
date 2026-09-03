# Search in a Sorted Array of Unknown Size

**Difficulty:** Medium
**Topics:** Array, Binary Search, Interactive
**Tags:**

**LeetCode:** [Problem 702](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/)

## Problem Description

This is an <strong><em>interactive problem</em></strong>.

You have a sorted array of <strong>unique</strong> elements and an <strong>unknown size</strong>. You do not have an access to the array but you can use the <code>ArrayReader</code> interface to access it. You can call <code>ArrayReader.get(i)</code> that:

<ul>
<li>returns the value at the <code>i<sup>th</sup></code> index (<strong>0-indexed</strong>) of the secret array (i.e., <code>secret[i]</code>), or</li>
<li>returns <code>2<sup>31</sup> - 1</code> if the <code>i</code> is out of the boundary of the array.</li>
</ul>

You are also given an integer <code>target</code>.

Return the index <code>k</code> of the hidden array where <code>secret[k] == target</code> or return <code>-1</code> otherwise.

You must write an algorithm with <code>O(log n)</code> runtime complexity.

## Examples

### Example 1:

```
Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.
```

### Example 2:

```
Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1.
```

## Constraints

- `1 <= secret.length <= 10^4`
- `-10^4 <= secret[i], target <= 10^4`
- All the integers of `secret` are <strong>unique</strong>.
- `secret` is sorted in a strictly increasing order.
