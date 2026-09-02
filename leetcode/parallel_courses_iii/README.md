# Parallel Courses III

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming, Graph Theory, Topological Sort, Directed Acyclic Graph
**Tags:** neetcode

**LeetCode:** [Problem 2050](https://leetcode.com/problems/parallel-courses-iii/description/)

## Problem Description

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCourse_j, nextCourse_j]` denotes that course `prevCourse_j` has to be completed **before** course `nextCourse_j` (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many **months** it takes to complete the `(i+1)th` course.

You must find the **minimum** number of months needed to complete all the courses following these rules:

- You may start taking a course at **any time** if the prerequisites are met.
- **Any number of courses** can be taken at the **same time**.

Return _the **minimum** number of months needed to complete all the courses_.

**Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/10/07/ex1.png)

```
Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8
```

**Explanation:** We start course 1 and course 2 simultaneously at month 0. Course 1 takes 3 months and course 2 takes 2 months to complete respectively. Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/10/07/ex2.png)

```
Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
Output: 12
```

**Explanation:** Courses 1, 2 and 3 run in parallel and finish after 1, 2 and 3 months. Course 4 starts after course 3 and finishes at month 7. Course 5 starts at month 7 and finishes at month 12.

## Constraints

- `1 <= n <= 5 * 10^4`
- `0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)`
- `relations[j].length == 2`
- `1 <= prevCourse_j, nextCourse_j <= n`
- `prevCourse_j != nextCourse_j`
- All the pairs `[prevCourse_j, nextCourse_j]` are **unique**.
- `time.length == n`
- `1 <= time[i] <= 10^4`
- The given graph is a directed acyclic graph.
