# Course Schedule III

**Difficulty:** Hard
**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)
**Tags:**

**LeetCode:** [Problem 630](https://leetcode.com/problems/course-schedule-iii/description/)

## Problem Description

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration_i, lastDay_i]` indicate that the `i_th` course should be taken **continuously** for `duration_i` days and must be finished before or on `lastDay_i`.

You will start on the `1_st` day and you cannot take two or more courses simultaneously.

Return _the maximum number of courses that you can take_.

## Examples

### Example 1:

```
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
```

### Example 2:

```
Input: courses = [[1,2]]
Output: 1
```

### Example 3:

```
Input: courses = [[3,2],[4,3]]
Output: 0
```

## Constraints

- `1 <= courses.length <= 10^4`
- `1 <= duration_i, lastDay_i <= 10^4`
