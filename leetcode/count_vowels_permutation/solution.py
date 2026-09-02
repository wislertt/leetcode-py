class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_vowel_permutation(self, n: int) -> int:
        mod = 10**9 + 7
        counts = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        for _ in range(n - 1):
            counts = {
                "a": counts["e"] + counts["i"] + counts["u"],
                "e": counts["a"] + counts["i"],
                "i": counts["e"] + counts["o"],
                "o": counts["i"],
                "u": counts["i"] + counts["o"],
            }
        return sum(counts.values()) % mod
