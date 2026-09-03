class Solution:
    # Time: O(n)
    # Space: O(1)

    def distinct_subseq_ii(self, s: str) -> int:
        mod = 10**9 + 7
        end: list[int] = [0] * 26
        total = 1
        for ch in s:
            c = ord(ch) - 97
            end[c], total = total, (2 * total - end[c]) % mod
        return (total - 1) % mod
