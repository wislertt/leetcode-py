# LFU Cache

**Difficulty:** Hard
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List
**Tags:** neetcode-250

**LeetCode:** [Problem 460](https://leetcode.com/problems/lfu-cache/description/)

## Problem Description

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the `LFUCache` class:

- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

A **use counter** is maintained for each key. The key with the smallest use counter is the least frequently used key. When a key is first inserted, its use counter is set to `1` (due to the `put` operation). The use counter is incremented each time `get` or `put` is called on it.

Both `get` and `put` must run in `O(1)` average time complexity.

## Examples

### Example 1:

```
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
lfu = LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is LFU (cnt=1 smallest), invalidate 2. cache=[3,1]
lfu.get(2);      // return -1
lfu.get(3);      // return 3, cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // tie cnt 1 and 3, 1 is LRU, invalidate 1. cache=[4,3]
lfu.get(1);      // return -1
lfu.get(3);      // return 3, cnt(3)=3, cnt(4)=1
lfu.get(4);      // return 4, cnt(4)=2, cnt(3)=3
```

## Constraints

- 1 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to `get` and `put`.
