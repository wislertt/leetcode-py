class Solution:
    # Time: O(10^n) over the first half, each candidate factorized in O(10^(n/2))
    # Space: O(1)
    def largest_palindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = 10 ** (n - 1)
        for half in range(upper, lower - 1, -1):
            s = str(half)
            cand = int(s + s[::-1])
            factor = upper
            while factor * factor >= cand:
                if cand % factor == 0:
                    return cand % 1337
                factor -= 1
        raise AssertionError("no palindrome found")
