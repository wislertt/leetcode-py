# Insert Greatest Common Divisors in Linked List

**Difficulty:** Medium
**Topics:** Linked List, Math, Number Theory
**Tags:** neetcode-250

**LeetCode:** [Problem 2807](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/)

## Problem Description

Given the `head` of a linked list, return the list after inserting the **greatest common divisor** of each pair of adjacent nodes.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2023/07/18/ex1_copy.png)

```
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation:
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2023/07/18/ex2_copy1.png)

```
Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
```

## Constraints

- The number of nodes in the list is in the range `[1, 5000]`.
- `1 <= Node.val <= 1000`
