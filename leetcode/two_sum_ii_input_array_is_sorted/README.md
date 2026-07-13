# Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search
**Tags:** neetcode-150, neetcode-250

**LeetCode:** [Problem 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Problem Description

Given a **1-indexed** array of integers `numbers` that is already _**sorted in non-decreasing order**_, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return _the indices of the two numbers_ `index1` _and_ `index2`_, **each incremented by one,** as an integer array_ `[index1, index2]` _of length 2._

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Examples

### Example 1:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Explanation:** The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2. We return [1, 2].

### Example 2:

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

**Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

### Example 3:

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

**Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

## Constraints

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- `numbers` is sorted in **non-decreasing order**.
- -1000 <= target <= 1000
- The tests are generated such that there is **exactly one solution**.
