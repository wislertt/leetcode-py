# Diameter of N-Ary Tree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Tree DP
**Tags:** neetcode

**LeetCode:** [Problem 1522](https://leetcode.com/problems/diameter-of-n-ary-tree/description/)

## Problem Description

Given a `root` of an `N-ary tree`, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the **longest** path between any two nodes in the tree. This path may or may not pass through the `root`.

_(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)_

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_2_1897.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
```

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_1_1897.png)

```
Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
```

### Example 3:

![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_3_1897.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
```

## Constraints

- The depth of the n-ary tree is less than or equal to `1000`.
- The total number of nodes is between `[1, 10^4]`.
