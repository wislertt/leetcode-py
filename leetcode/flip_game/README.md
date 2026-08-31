# Flip Game

**Difficulty:** Easy
**Topics:** String
**Tags:** grind-75

**LeetCode:** [Problem 293](https://leetcode.com/problems/flip-game/description/)

## Problem Description

You are playing a Flip Game with your friend.

You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip **two consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string `currentState` after **one valid move**. You may return the answer in **any order**. If there is no valid move, return an empty list `[]`.

## Examples

### Example 1:

```
Input: currentState = "++++"
Output: ["--++","+--+","++--"]
```

### Example 2:

```
Input: currentState = "+"
Output: []
```

## Constraints

- `1 <= currentState.length <= 500`
- `currentState[i]` is either `'+'` or `'-'`.
