# Find Kth Bit in Nth Binary String

**Difficulty:** Medium
**Topics:** String, Recursion, Simulation
**Tags:** neetcode

**LeetCode:** [Problem 1545](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/)

## Problem Description

Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows:

- `S_1 = "0"`
- `S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

- `S_1 = "0"`
- `S_2 = "011"`
- `S_3 = "0111001"`
- `S_4 = "011100110110001"`

Return _the_ `k^th` _bit_ _in_ `S_n`. It is guaranteed that `k` is valid for the given `n`.

## Examples

### Example 1:

```
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
```

### Example 2:

```
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
```

## Constraints

- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`
