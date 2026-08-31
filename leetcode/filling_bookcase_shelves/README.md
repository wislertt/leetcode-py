# Filling Bookcase Shelves

**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Tags:** neetcode

**LeetCode:** [Problem 1105](https://leetcode.com/problems/filling-bookcase-shelves/description/)

## Problem Description

You are given an array <code>books</code> where <code>books[i] = [thickness<sub>i</sub>, height<sub>i</sub>]</code> indicates the thickness and height of the <code>i<sup>th</sup></code> book. You are also given an integer <code>shelfWidth</code>.

We want to place these books in order onto bookcase shelves that have a total width <code>shelfWidth</code>.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to <code>shelfWidth</code>, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of <code>5</code> books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return <em>the minimum possible height that the total bookshelf can be after placing shelves in this manner</em>.

## Examples

### Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/06/24/shelves.png)

```
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation: The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6. Notice that book number 2 does not have to be on the first shelf.
```

### Example 2:

```
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
```

## Constraints

- <code>1 &lt;= books.length &lt;= 1000</code>
- <code>1 &lt;= thickness<sub>i</sub> &lt;= shelfWidth &lt;= 1000</code>
- <code>1 &lt;= height<sub>i</sub> &lt;= 1000</code>
