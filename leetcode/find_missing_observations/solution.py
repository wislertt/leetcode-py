class Solution:
    # Time: O(m + n)
    # Space: O(n)
    def missing_rolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        target = mean * (len(rolls) + n) - sum(rolls)
        if target < n or target > 6 * n:
            return []
        base, extra = divmod(target, n)
        return [base + 1] * extra + [base] * (n - extra)
