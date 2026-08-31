# Validate Stack Sequences

**Difficulty:** Medium
**Topics:** Array, Stack, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 946](https://leetcode.com/problems/validate-stack-sequences/description/)

## Problem Description

<p>Given two integer arrays <code>pushed</code> and <code>popped</code> each with <strong>distinct</strong> values, return <code>true</code> if this could have been the result of a sequence of push and pop operations on an initially empty stack, or <code>false</code> otherwise.</p>

## Examples

### Example 1:

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

### Example 2:

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

## Constraints

- 1 &lt;= pushed.length &lt;= 1000
- 0 &lt;= pushed[i] &lt;= 1000
- All the elements of pushed are unique.
- popped.length == pushed.length
- popped is a permutation of pushed.
