# Optimize Water Distribution in a Village

**Difficulty:** Hard
**Topics:** Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)
**Tags:**

**LeetCode:** [Problem 1168](https://leetcode.com/problems/optimize-water-distribution-in-a-village/description/)

## Problem Description

There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house `i`, we can either build a well inside it directly with cost `wells[i - 1]` (note the `-1` due to **0-indexing**), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array `pipes` where each `pipes[j] = [house1_j, house2_j, cost_j]` represents the cost to connect `house1_j` and `house2_j` together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return _the minimum total cost to supply water to all houses_.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1168.Optimize%20Water%20Distribution%20in%20a%20Village/images/1359_ex1.png)

```
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
```

### Example 2:

```
Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
  - Build a well inside house 1 with cost 1.
  - Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
  - Build a well inside house 1 with cost 1.
  - Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
  - Build a well inside house 2 with cost 1.
  - Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose **the cheapest option**.
```

## Constraints

- 2 <= n <= 10^4
- wells.length == n
- 0 <= wells[i] <= 10^5
- 1 <= pipes.length <= 10^4
- pipes[j].length == 3
- 1 <= house1_j, house2_j <= n
- 0 <= cost_j <= 10^5
- house1_j != house2_j
