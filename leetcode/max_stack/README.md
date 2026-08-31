# Max Stack

**Difficulty:** Hard
**Topics:** Linked List, Stack, Design, Doubly-Linked List, Ordered Set
**Tags:** neetcode

**LeetCode:** [Problem 716](https://leetcode.com/problems/max-stack/description/)

## Problem Description

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the `MaxStack` class:

- `MaxStack()` Initializes the stack object.
- `void push(int x)` Pushes element x onto the stack.
- `int pop()` Removes the element on top of the stack and returns it.
- `int top()` Gets the element on the top of the stack without removing it.
- `int peekMax()` Retrieves the maximum element in the stack without removing it.
- `int popMax()` Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

You must come up with a solution that supports `O(1)` for each `top` call and `O(logn)` for each other call.

## Examples

### Example 1:

```
Input
['MaxStack', 'push', 'push', 'push', 'top', 'pop_max', 'top', 'peek_max', 'pop', 'top']
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]
```

## Constraints

- -10^7 <= x <= 10^7
- At most 10^5 calls will be made to push, pop, top, peek_max, and pop_max.
- There will be at least one element in the stack when pop, top, peek_max, or pop_max is called.
