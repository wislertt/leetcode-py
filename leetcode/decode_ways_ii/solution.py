class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_decodings(self, s: str) -> int:
        mod = 1_000_000_007
        prev = 1
        curr = self._ways_single(s[0])
        for i in range(1, len(s)):
            pair = self._ways_pair(s[i - 1], s[i])
            prev, curr = curr, (curr * self._ways_single(s[i]) + prev * pair) % mod
        return curr

    def _ways_single(self, ch: str) -> int:
        if ch == "*":
            return 9
        return 0 if ch == "0" else 1

    def _ways_pair(self, a: str, b: str) -> int:
        if a == "*":
            if b == "*":
                return 15
            return 2 if b <= "6" else 1
        if b == "*":
            return 9 if a == "1" else (6 if a == "2" else 0)
        if a == "0":
            return 0
        return 1 if int(a + b) <= 26 else 0
