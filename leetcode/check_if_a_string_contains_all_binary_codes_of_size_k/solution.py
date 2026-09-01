class Solution:
    # Time: O(n) each window hashed once; Space: O(2^k) for the set
    def has_all_codes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) < need + k - 1:
            return False
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i : i + k])
            if len(seen) == need:
                return True
        return False
