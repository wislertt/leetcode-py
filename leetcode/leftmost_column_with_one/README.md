# Leftmost Column with at Least a One

**Difficulty:** Medium
**Topics:** Array, Binary Search, Interactive, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 1428](https://leetcode.com/problems/leftmost-column-with-one/description/)

## Problem Description

A <strong>row-sorted binary matrix</strong> means that all elements are <code>0</code> or <code>1</code> and each row of the matrix is sorted in non-decreasing order.

Given a <strong>row-sorted binary matrix</strong> <code>binaryMatrix</code>, return <em>the index (0-indexed) of the <strong>leftmost column</strong> with a 1 in it</em>. If such an index does not exist, return <code>-1</code>.

<strong>You can't access the Binary Matrix directly.</strong> You may only access the matrix using a <code>BinaryMatrix</code> interface:

<ul>
<li><code>BinaryMatrix.get(row, col)</code> returns the element of the matrix at index <code>(row, col)</code> (0-indexed).</li>
<li><code>BinaryMatrix.dimensions()</code> returns the dimensions of the matrix as a list of 2 elements <code>[rows, cols]</code>, which means the matrix is <code>rows x cols</code>.</li>
</ul>

Submissions making more than <code>1000</code> calls to <code>BinaryMatrix.get</code> will be judged <em>Wrong Answer</em>.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-5.jpg)

```
Input: mat = [[0,0],[1,1]]
Output: 0
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-4.jpg)

```
Input: mat = [[0,0],[0,1]]
Output: 1
```

### Example 3:

![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1428.Leftmost%20Column%20with%20at%20Least%20a%20One/images/untitled-diagram-3.jpg)

```
Input: mat = [[0,0],[0,0]]
Output: -1
```

## Constraints

- <code>rows == mat.length</code>
- <code>cols == mat[i].length</code>
- <code>1 &lt;= rows, cols &lt;= 100</code>
- <code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.
- <code>mat[i]</code> is sorted in non-decreasing order.

<strong>Follow up:</strong> Could you find a solution with a complexity better than <code>O(rows x cols)</code>?
