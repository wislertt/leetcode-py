# Asteroid Collision

**Difficulty:** Medium
**Topics:** Array, Stack, Simulation
**Tags:** grind-75

**LeetCode:** [Problem 735](https://leetcode.com/problems/asteroid-collision/description/)


## Problem Description

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

&nbsp;
Example 1:


Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.


Example 2:


Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.


Example 3:


Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Example 4:


Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.


&nbsp;
Constraints:


	2 &lt;= asteroids.length &lt;= 104
	-1000 &lt;= asteroids[i] &lt;= 1000
	asteroids[i] != 0

## Examples

### Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.


Example 2:


Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.


Example 3:


Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Example 4:


Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

## Constraints

- 2 &lt;= asteroids.length &lt;= 104
- -1000 &lt;= asteroids[i] &lt;= 1000
- asteroids[i] != 0


