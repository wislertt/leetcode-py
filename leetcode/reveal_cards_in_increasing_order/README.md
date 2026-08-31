# Reveal Cards In Increasing Order

**Difficulty:** Medium
**Topics:** Array, Queue, Sorting, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 950](https://leetcode.com/problems/reveal-cards-in-increasing-order/description/)

## Problem Description

<p>You are given an integer array <code>deck</code>. There is a deck of cards where every card has a unique integer. The integer on the <code>i<sup>th</sup></code> card is <code>deck[i]</code>.</p>

<p>You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.</p>

<p>You will do the following steps repeatedly until all cards are revealed:</p>

<ol>
	<li>Take the top card of the deck, reveal it, and take it out of the deck.</li>
	<li>If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.</li>
	<li>If there are still unrevealed cards, go back to step 1. Otherwise, stop.</li>
</ol>

<p>Return <em>an ordering of the deck that would reveal the cards in <strong>increasing</strong> order</em>.</p>

<p><strong>Note</strong> that the first entry in the answer is considered to be the top of the deck.</p>

## Examples

### Example 1:

```
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
```

### Example 2:

```
Input: deck = [1,1000]
Output: [1,1000]
```

## Constraints

- 1 &lt;= deck.length &lt;= 1000
- 1 &lt;= deck[i] &lt;= 10^6
- All the values of deck are unique.
