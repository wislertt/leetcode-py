# Rotating the Box

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Matrix
**Tags:** neetcode

**LeetCode:** [Problem 1861](https://leetcode.com/problems/rotating-the-box/description/)

## Problem Description

You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

- A stone `'#'`
- A stationary obstacle `'*'`
- Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not** affect the stones' horizontal positions.

It is **guaranteed** that each stone in `boxGrid` rests on an obstacle, another stone, or the bottom of the box.

Return _an_ `n x m` _matrix representing the box after the rotation described above_.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png)

```
Input: boxGrid = [['#','.','#']]
Output: [['.'],['#'],['#']]
```

### Example 2:

![Example 2](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png)

```
Input: boxGrid = [['#','.','*','.'],['#','#','*','.']]
Output: [['#','.'],['#','#'],['*','*'],['.','.']]
```

### Example 3:

![Example 3](https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png)

```
Input: boxGrid = [['#','#','*','.','*','.'],['#','#','#','*','.','.'],['#','#','#','.','#','.']]
Output: [['.','#','#'],['.','#','#'],['#','#','*'],['#','*','.'],['#','.','*'],['#','.','.']]
```

## Constraints

- `m == boxGrid.length`
- `n == boxGrid[i].length`
- `1 <= m, n <= 500`
- `boxGrid[i][j]` is either `'#'`, `'*'`, or `'.'`.
