# Sliding Window Maximum

**Difficulty:** Hard
**Topics:** Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
**Tags:** algo-master-75, neetcode-150

**LeetCode:** [Problem 239](https://leetcode.com/problems/sliding-window-maximum/description/)

## Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return _the max sliding window_.

## Examples

### Example 1:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Explanation:**

Window position Max

---

[1 3 -1] -3 5 3 6 7 **3**
1 [3 -1 -3] 5 3 6 7 **3**
1 3 [-1 -3 5] 3 6 7 ** 5**
1 3 -1 [-3 5 3] 6 7 **5**
1 3 -1 -3 [5 3 6] 7 **6**
1 3 -1 -3 5 [3 6 7] **7**

### Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
