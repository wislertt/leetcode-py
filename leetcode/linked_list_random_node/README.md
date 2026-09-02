# Linked List Random Node

**Difficulty:** Medium
**Topics:** Linked List, Math, Reservoir Sampling, Randomized
**Tags:**

**LeetCode:** [Problem 382](https://leetcode.com/problems/linked-list-random-node/description/)

## Problem Description

Given a singly linked list, return a random node's value from the linked list. Each node must have the **same probability** of being chosen.

Implement the `Solution` class:

- `Solution(ListNode head)` Initializes the object with the head of the singly-linked list `head`.
- `int getRandom()` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)

```
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
```

### Example 2:

```
Input
["Solution", "getRandom", "getRandom"]
[[[7]], [], []]
Output
[null, 7, 7]

Explanation
Solution solution = new Solution([7]);
solution.getRandom(); // return 7, the only node in the list.
```

## Constraints

- The number of nodes in the linked list will be in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls will be made to `getRandom`.

**Follow up:**

- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?
