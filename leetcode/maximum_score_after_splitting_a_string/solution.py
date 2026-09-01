class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_score(self, s: str) -> int:
        left_zeros = 1 if s[0] == "0" else 0
        right_ones = s[1:].count("1")
        best = left_zeros + right_ones
        for ch in s[1:-1]:
            if ch == "0":
                left_zeros += 1
            else:
                right_ones -= 1
            best = max(best, left_zeros + right_ones)
        return best
