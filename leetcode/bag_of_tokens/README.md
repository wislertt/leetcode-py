# Bag of Tokens

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Greedy, Sorting
**Tags:** neetcode

**LeetCode:** [Problem 948](https://leetcode.com/problems/bag-of-tokens/description/)

## Problem Description

<p>You start with an initial power of <code>power</code>, an initial score of <code>0</code>, and a bag of tokens given as an integer array <code>tokens</code>, where each&nbsp;<code>tokens[i]</code> denotes the value of token<sub>i</sub>.</p>

<p>Your goal is to maximize the total <strong>score</strong> by strategically playing these tokens. In one move, you can play an <strong>unplayed</strong> token in one of the two ways (but not both for the same token):</p>

<ul>
	<li><strong>Face-up:</strong> If your current power is at least <code>tokens[i]</code>, you may play token<sub>i</sub>, losing <code>tokens[i]</code> power and gaining <code>1</code> score.</li>
	<li><strong>Face-down:</strong> If your current score is at least <code>1</code>, you may play token<sub>i</sub>, gaining <code>tokens[i]</code> power and losing <code>1</code> score.</li>
</ul>

<p>Return <em>the maximum possible <strong>score</strong> you can achieve after playing any number of tokens</em>.</p>

## Examples

### Example 1:

```
Input: tokens = [100], power = 50
Output: 0
Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).
```

### Example 2:

```
Input: tokens = [200,100], power = 150
Output: 1
Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
```

### Example 3:

```
Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
```

## Constraints

- 0 &lt;= tokens.length &lt;= 1000
- 0 &lt;= tokens[i], power &lt; 10^4
