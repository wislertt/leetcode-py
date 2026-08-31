# Grumpy Bookstore Owner

**Difficulty:** Medium
**Topics:** Array, Sliding Window
**Tags:** neetcode

**LeetCode:** [Problem 1052](https://leetcode.com/problems/grumpy-bookstore-owner/description/)

## Problem Description

There is a bookstore owner that has a store open for <code>n</code> minutes. You are given an integer array <code>customers</code> of length <code>n</code> where <code>customers[i]</code> is the number of the customers that enter the store at the start of the <code>i<sup>th</sup></code> minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array <code>grumpy</code> where <code>grumpy[i]</code> is <code>1</code> if the bookstore owner is grumpy during the <code>i<sup>th</sup></code> minute, and is <code>0</code> otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not <strong>satisfied</strong>. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain <strong>not grumpy</strong> for <code>minutes</code> consecutive minutes, but this technique can only be used <strong>once</strong>.

Return the <strong>maximum</strong> number of customers that can be <em>satisfied</em> throughout the day.

## Examples

### Example 1:

```
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

### Example 2:

```
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
```

## Constraints

- <code>n == customers.length == grumpy.length</code>
- <code>1 &lt;= minutes &lt;= n &lt;= 2 * 10<sup>4</sup></code>
- <code>0 &lt;= customers[i] &lt;= 1000</code>
- <code>grumpy[i]</code> is either <code>0</code> or <code>1</code>.
