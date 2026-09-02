# Delete Nodes From Linked List Present in Array

**Difficulty:** Medium
**Topics:** Array, Hash Table, Linked List
**Tags:** neetcode

**LeetCode:** [Problem 3217](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/)

## Problem Description

You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after <strong>removing</strong> all nodes from the linked list that have a value that exists in `nums`.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png)

```
Input: nums = [1,2,3], head = [1,2,3,4,5]
Output: [4,5]
Explanation: Remove the nodes with values 1, 2, and 3.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png)

```
Input: nums = [1], head = [1,2,1,2,1,2]
Output: [2,2,2]
Explanation: Remove the nodes with value 1.
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png)

```
Input: nums = [5], head = [1,2,3,4]
Output: [1,2,3,4]
Explanation: No node has value 5.
```

## Constraints

- 1 <= nums.length <= 10<sup>5</sup>
- 1 <= nums[i] <= 10<sup>5</sup>
- All elements in nums are unique.
- The number of nodes in the given list is in the range [1, 10<sup>5</sup>].
- 1 <= Node.val <= 10<sup>5</sup>
- The input is generated such that there is at least one node in the linked list that has a value not present in nums.
