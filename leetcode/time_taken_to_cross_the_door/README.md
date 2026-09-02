# Time Taken to Cross the Door

**Difficulty:** Hard
**Topics:** Queue, Array, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 2534](https://leetcode.com/problems/time-taken-to-cross-the-door/description/)

## Problem Description

There are <code>n</code> persons numbered from <code>0</code> to <code>n - 1</code> and a door. Each person can enter or exit through the door once, taking one second.</p>

<p>You are given a <strong>non-decreasing</strong> integer array <code>arrival</code> of size <code>n</code>, where <code>arrival[i]</code> is the arrival time of the <code>i<sup>th</sup></code> person at the door. You are also given an array <code>state</code> of size <code>n</code>, where <code>state[i]</code> is <code>0</code> if person <code>i</code> wants to enter through the door or <code>1</code> if they want to exit through the door.</p>

<p>If two or more persons want to use the door at the <strong>same</strong> time, they follow the following rules:</p>

<ul>
	<li>If the door was <strong>not</strong> used in the previous second, then the person who wants to <strong>exit</strong> goes first.</li>
	<li>If the door was used in the previous second for <strong>entering</strong>, the person who wants to enter goes first.</li>
	<li>If the door was used in the previous second for <strong>exiting</strong>, the person who wants to <strong>exit</strong> goes first.</li>
	<li>If multiple persons want to go in the same direction, the person with the <strong>smallest</strong> index goes first.</li>
</ul>

<p>Return <em>an array </em><code>answer</code><em> of size </em><code>n</code><em> where </em><code>answer[i]</code><em> is the second at which the <code>i<sup>th</sup></code> person crosses the door</em>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>Only one person can cross the door at each second.</li>
	<li>A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.</li>
</ul>

## Examples

### Example 1:

```
Input: arrival = [0,1,1,2,4], state = [0,1,0,0,1]
Output: [0,3,1,2,4]
Explanation: At each second we have the following:
- At t = 0: Person 0 is the only one who wants to enter, so they just enter through the door.
- At t = 1: Person 1 wants to exit, and person 2 wants to enter. Since the door was used the previous second for entering, person 2 enters.
- At t = 2: Person 1 still wants to exit, and person 3 wants to enter. Since the door was used the previous second for entering, person 3 enters.
- At t = 3: Person 1 is the only one who wants to exit, so they just exit through the door.
- At t = 4: Person 4 is the only one who wants to exit, so they just exit through the door.
```

### Example 2:

```
Input: arrival = [0,0,0], state = [1,0,1]
Output: [0,2,1]
Explanation: At each second we have the following:
- At t = 0: Person 1 wants to enter while persons 0 and 2 want to exit. Since the door was not used in the previous second, the persons who want to exit get to go first. Since person 0 has a smaller index, they exit first.
- At t = 1: Person 1 wants to enter, and person 2 wants to exit. Since the door was used in the previous second for exiting, person 2 exits.
- At t = 2: Person 1 is the only one who wants to enter, so they just enter through the door.
```

## Constraints

- n == arrival.length == state.length
- 1 <= n <= 10^5
- 0 <= arrival[i] <= n
- arrival is sorted in non-decreasing order.
- state[i] is either 0 or 1.
