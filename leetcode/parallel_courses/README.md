# Parallel Courses

**Difficulty:** Medium
**Topics:** Graph, Topological Sort
**Tags:** neetcode

**LeetCode:** [Problem 1136](https://leetcode.com/problems/parallel-courses/description/)

## Problem Description

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCourse_i, nextCourse_i]`, representing a prerequisite relationship between course `prevCourse_i` and course `nextCourse_i`: course `prevCourse_i` has to be taken before course `nextCourse_i`.

In one semester, you can take **any number** of courses as long as you have taken all the prerequisites in the **previous** semester for the courses you are taking.

Return _the **minimum** number of semesters needed to take all courses_. If there is no way to take all the courses, return `-1`.

## Examples

### Example 1:

![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1136.Parallel%20Courses/images/course1graph.jpg)

```
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
```

**Explanation:** In the first semester, you can take courses 1 and 2. In the second semester, you can take course 3.

### Example 2:

![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1136.Parallel%20Courses/images/course2graph.jpg)

```
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
```

**Explanation:** No course can be studied because they are prerequisites of each other.

## Constraints

- `1 <= n <= 5000`
- `1 <= relations.length <= 5000`
- `relations[i].length == 2`
- `1 <= prevCourse_i, nextCourse_i <= n`
- `prevCourse_i != nextCourse_i`
- All the pairs `[prevCourse_i, nextCourse_i]` are **unique**.
