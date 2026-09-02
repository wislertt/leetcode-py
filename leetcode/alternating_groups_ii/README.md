# Alternating Groups II

**Difficulty:** Medium
**Topics:** Array, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 3208](https://leetcode.com/problems/alternating-groups-ii/description/)

## Problem Description

There is a circle of red and blue tiles. You are given an array of integers <code>colors</code> and an integer <code>k</code>. The color of tile <code>i</code> is represented by <code>colors[i]</code>:

<ul>
	<li><code>colors[i] == 0</code> means that tile <code>i</code> is <strong>red</strong>.</li>
	<li><code>colors[i] == 1</code> means that tile <code>i</code> is <strong>blue</strong>.</li>
</ul>

<p>An <strong>alternating</strong> group is every <code>k</code> contiguous tiles in the circle with <strong>alternating</strong> colors (each tile in the group except the first and last one has a different color from its <strong>left</strong> and <strong>right</strong> tiles).</p>

<p>Return the number of <strong>alternating</strong> groups.</p>

<p><strong>Note</strong> that since <code>colors</code> represents a <strong>circle</strong>, the <strong>first</strong> and the <strong>last</strong> tiles are considered to be next to each other.</p>

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png)

```
Input: colors = [0,1,0,1,0], k = 3
Output: 3
```

Alternating groups:

![Group 1](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png)

![Group 2](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png)

![Group 3](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png)

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png)

```
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2
```

Alternating groups:

![Group 1](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png)

![Group 2](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png)

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png)

```
Input: colors = [1,1,0,1], k = 4
Output: 0
```

## Constraints

- 3 <= colors.length <= 10^5
- 0 <= colors[i] <= 1
- 3 <= k <= colors.length
