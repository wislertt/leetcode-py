class Solution:
    # Time: O(len(s))
    # Space: O(1)
    def equal_substring(self, s: str, t: str, max_cost: int) -> int:
        best = 0
        left = 0
        cost = 0
        for right, (a, b) in enumerate(zip(s, t, strict=True)):
            cost += abs(ord(a) - ord(b))
            while cost > max_cost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            best = max(best, right - left + 1)
        return best
