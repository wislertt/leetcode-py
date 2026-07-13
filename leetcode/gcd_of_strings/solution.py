from math import gcd


class Solution:
    # Time: O(n + m) — concatenate + compare strings of total length n + m
    # Space: O(n + m) — concatenated strings
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        # If a common divisor exists, str1 and str2 must compose the same
        # string regardless of concatenation order.
        if str1 + str2 != str2 + str1:
            return ""

        # The largest common divisor has length = gcd of the two lengths.
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
