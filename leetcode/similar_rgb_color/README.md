# Similar RGB Color

**Difficulty:** Easy
**Topics:** Math, String, Enumeration
**Tags:**

**LeetCode:** [Problem 800](https://leetcode.com/problems/similar-rgb-color/description/)

## Problem Description

The red-green-blue color `"#AABBCC"` can be written as `"#ABC"` in shorthand.

- For example, `"#15c"` is shorthand for the color `"#1155cc"`.

The similarity between the two colors `"#ABCDEF"` and `"#UVWXYZ"` is `-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2`.

Given a string `color` that follows the format `"#ABCDEF"`, return a string represents the color that is most similar to the given color and has a shorthand (i.e., it can be represented as some `"#XYZ"`).

**Any answer** which has the same highest similarity as the best answer will be accepted.

## Examples

### Example 1:

```
Input: color = "#09f166"
Output: "#11ee66"
Explanation:
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.
```

### Example 2:

```
Input: color = "#4e3fe1"
Output: "#5544dd"
```

## Constraints

- `color.length == 7`
- `color[0] == '#'`
- `color[i]` is either digit or character in the range `['a', 'f']` for `i > 0`.
