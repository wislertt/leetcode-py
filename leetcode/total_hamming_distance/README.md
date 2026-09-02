# Total Hamming Distance

**Difficulty:** Medium
**Topics:** Array, Math, Bit Manipulation
**Tags:**

**LeetCode:** [Problem 477](https://leetcode.com/problems/total-hamming-distance/description/)

## Problem Description

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Given an integer array <code>nums</code>, return <em>the sum of <strong>Hamming distances</strong> between all the pairs of the integers in</em> <code>nums</code>.

## Examples

### Example 1:

```
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```

### Example 2:

```
Input: nums = [4,14,4]
Output: 4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^9`
- The answer for the given input will fit in a **32-bit** integer.

**Follow up:** Could you solve this problem with a linear runtime?
