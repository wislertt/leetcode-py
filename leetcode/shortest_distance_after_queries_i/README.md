# Shortest Distance After Road Addition Queries I

**Difficulty:** Medium
**Topics:** Array, Breadth-First Search, Graph Theory
**Tags:** neetcode

**LeetCode:** [Problem 3243](https://leetcode.com/problems/shortest-distance-after-queries-i/description/)

## Problem Description

You are given an integer <code>n</code> and a 2D integer array <code>queries</code>.

There are <code>n</code> cities numbered from <code>0</code> to <code>n - 1</code>. Initially, there is a <strong>unidirectional</strong> road from city <code>i</code> to city <code>i + 1</code> for all <code>0 &lt;= i &lt; n - 1</code>.

<code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> represents the addition of a new <strong>unidirectional</strong> road from city <code>u<sub>i</sub></code> to city <code>v<sub>i</sub></code>. After each query, you need to find the <strong>length</strong> of the <strong>shortest path</strong> from city <code>0</code> to city <code>n - 1</code>.

Return an array <code>answer</code> where for each <code>i</code> in the range <code>[0, queries.length - 1]</code>, <code>answer[i]</code> is the length of the shortest path from city <code>0</code> to city <code>n - 1</code> after processing the <strong>first</strong> <code>i + 1</code> queries.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image8.jpg)

```
Input: n = 5, queries = [[2,4],[0,2],[0,4]]
Output: [3,2,1]
Explanation:

After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
```

### Example 2:

![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image9.jpg)

After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

### Example 3:

![Example 1](https://assets.leetcode.com/uploads/2024/06/28/image10.jpg)

After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

### Example 4:

![Example 2](https://assets.leetcode.com/uploads/2024/06/28/image11.jpg)

```
Input: n = 4, queries = [[0,3],[0,2]]
Output: [1,1]
Explanation:

After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
```

![Example 2](https://assets.leetcode.com/uploads/2024/06/28/image12.jpg)

After the addition of the road from 0 to 2, the length of the shortest path remains 1.

## Constraints

- <code>3 &lt;= n &lt;= 500</code>
- <code>1 &lt;= queries.length &lt;= 500</code>
- <code>queries[i].length == 2</code>
- <code>0 &lt;= queries[i][0] &lt; queries[i][1] &lt; n</code>
- <code>1 &lt; queries[i][1] - queries[i][0]</code>
- There are no repeated roads among the queries.
