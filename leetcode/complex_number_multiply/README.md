# Complex Number Multiplication

**Difficulty:** Medium
**Topics:** Math, String, Simulation
**Tags:**

**LeetCode:** [Problem 537](https://leetcode.com/problems/complex-number-multiply/description/)

## Problem Description

A <a href="https://en.wikipedia.org/wiki/Complex_number" target="_blank">complex number</a> can be represented as a string on the form "real+imaginaryi" where:

- `real` is the real part and is an integer in the range `[-100, 100]`.
- `imaginary` is the imaginary part and is an integer in the range `[-100, 100]`.
- `i^2 == -1`.

Given two complex numbers `num1` and `num2` as strings, return <em>a string of the complex number that represents their multiplication</em>.

## Examples

### Example 1:

```
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

### Example 2:

```
Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

## Constraints

- `num1` and `num2` are valid complex numbers.
