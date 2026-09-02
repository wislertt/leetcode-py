# First Unique Number

**Difficulty:** Medium
**Topics:** Design, Queue, Array, Hash Table, Data Stream
**Tags:** neetcode

**LeetCode:** [Problem 1429](https://leetcode.com/problems/first-unique-number/description/)

## Problem Description

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the `FirstUnique` class:

- `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
- `int showFirstUnique()` returns the value of **the first unique** integer of the queue, and returns **-1** if there is no such integer.
- `void add(int value)` insert value to the queue.

## Examples

### Example 1:

```
Input
["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
[[[2, 3, 5]], [], [5], [], [2], [], [3], []]
Output
[null, 2, null, 2, null, 3, null, -1]
```

### Example 2:

```
Input
["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
[[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]
Output
[null, -1, null, null, null, null, null, 17]
```

### Example 3:

```
Input
["FirstUnique", "showFirstUnique", "add", "showFirstUnique"]
[[[809]], [], [809], []]
Output
[null, 809, null, -1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^8`
- `1 <= value <= 10^8`
- At most `50000` calls will be made to `showFirstUnique` and `add`.
