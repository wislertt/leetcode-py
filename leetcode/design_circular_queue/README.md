# Design Circular Queue

**Difficulty:** Medium
**Topics:** Array, Linked List, Design, Queue
**Tags:** neetcode-250

**LeetCode:** [Problem 622](https://leetcode.com/problems/design-circular-queue/description/)

## Problem Description

Design your implementation of the circular queue. The circular queue is a linear data structure that operates on the FIFO (First In First Out) principle, with the last position connected back to the first to form a circle (a "Ring Buffer").

Implement the `MyCircularQueue` class:

- `MyCircularQueue(k)` Initializes the object with the queue size `k`.
- `int Front()` Gets the front item; returns `-1` if empty.
- `int Rear()` Gets the last item; returns `-1` if empty.
- `boolean enQueue(int value)` Inserts an element. Returns `true` if successful.
- `boolean deQueue()` Deletes an element from the queue. Returns `true` if successful.
- `boolean isEmpty()` Checks whether the queue is empty.
- `boolean isFull()` Checks whether the queue is full.

You must solve the problem without using the built-in queue data structure.

## Examples

### Example 1:

```
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
myCircularQueue = MyCircularQueue(3);
myCircularQueue.enQueue(1);  // True
myCircularQueue.enQueue(2);  // True
myCircularQueue.enQueue(3);  // True
myCircularQueue.enQueue(4);  // False, queue is full
myCircularQueue.Rear();      // 3
myCircularQueue.isFull();    // True
myCircularQueue.deQueue();   // True
myCircularQueue.enQueue(4);  // True
myCircularQueue.Rear();      // 4
```

## Constraints

- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
