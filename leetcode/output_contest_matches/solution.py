class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def find_contest_match(self, n: int) -> str:
        teams = [str(i + 1) for i in range(n)]
        while n > 1:
            for i in range(n >> 1):
                teams[i] = f"({teams[i]},{teams[n - i - 1]})"
            n >>= 1
        return teams[0]
