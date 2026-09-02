# Queue Reconstruction by Height

**Difficulty:** Medium
**Topics:** Array, Binary Indexed Tree, Segment Tree, Sorting
**Tags:**

**LeetCode:** [Problem 406](https://leetcode.com/problems/queue-reconstruction-by-height/description/)

## Problem Description

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [h<sub>i</sub>, k<sub>i</sub>]` represents the i<sup>th</sup> person of height `h<sub>i</sub>` with exactly `k<sub>i</sub>` other people in front who have a height greater than or equal to `h<sub>i</sub>`.

Reconstruct and return the queue that is represented by the input array `people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [h<sub>j</sub>, k<sub>j</sub>]` is the attributes of the j<sup>th</sup> person in the queue (`queue[0]` is the person at the front of the queue).

## Examples

### Example 1:

```
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
```

**Explanation:**

- Person 0 has height 5 with no other people taller or the same height in front.
- Person 1 has height 7 with no other people taller or the same height in front.
- Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
- Person 3 has height 6 with one person taller or the same height in front, which is person 1.
- Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
- Person 5 has height 7 with one person taller or the same height in front, which is person 1.
  Hence `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]` is the reconstructed queue.

### Example 2:

```
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
```

## Constraints

- `1 <= people.length <= 2000`
- `0 <= h<sub>i</sub> <= 10^6`
- `0 <= k<sub>i</sub> < people.length`
- It is guaranteed that the queue can be reconstructed.
