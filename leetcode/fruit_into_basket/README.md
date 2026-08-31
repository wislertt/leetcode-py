# Fruit Into Baskets

**Difficulty:** Medium
**Topics:** Array, Hash Table, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 904](https://leetcode.com/problems/fruit-into-basket/description/)

## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the <strong>type</strong> of fruit the <code>i<sup>th</sup></code> tree produces. You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:</p>

<ul>
	<li>You only have <strong>two</strong> baskets, and each basket can only hold a <strong>single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
	<li>Starting from any tree of your choice, you must pick exactly <strong>one fruit</strong> from <strong>every</strong> tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
	<li>Once you get to a tree, the fruit cannot jump back to the tree 1. (For example, if you pick fruit 1 from tree 2, you cannot pick fruit 1 from tree 1.)</li>
	<li>Given the integer array <code>fruits</code>, return <em>the <strong>maximum</strong> number of fruits you can pick.</em></li>
</ul>

## Examples

### Example 1:

```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```

### Example 2:

```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started from the first tree, we would only pick from trees [0,1].
```

### Example 3:

```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started from the first tree, we would only pick from trees [1,2].
```

## Constraints

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
