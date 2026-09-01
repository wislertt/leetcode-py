# Clone N-ary Tree

**Difficulty:** Medium
**Topics:** Tree, Depth-First Search, Breadth-First Search, Hash Table
**Tags:** neetcode

**LeetCode:** [Problem 1490](https://leetcode.com/problems/clone-n-ary-tree/description/)

## Problem Description

Given a `root` of an N-ary tree, return a **deep copy** (clone) of the tree.

Each node in the n-ary tree contains a val (`int`) and a list (`List[Node]`) of its children.

```
class Node {
    public int val;
    public List<Node> children;
}
```

_Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples)._

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

## Constraints

- The depth of the n-ary tree is less than or equal to 1000.
- The total number of nodes is between [0, 10^4].

**Follow up:** Can your solution work for the graph problem?
