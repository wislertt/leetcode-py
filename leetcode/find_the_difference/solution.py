class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_the_difference(self, s: str, t: str) -> str:
        acc = 0
        for ch in s:
            acc ^= ord(ch)
        for ch in t:
            acc ^= ord(ch)
        return chr(acc)
