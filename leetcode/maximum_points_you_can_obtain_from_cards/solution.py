class Solution:
    # Time: O(k)
    # Space: O(1)
    def max_score(self, card_points: list[int], k: int) -> int:
        window = sum(card_points[:k])
        best = window
        for i in range(1, k + 1):
            window += card_points[-i] - card_points[k - i]
            best = max(best, window)
        return best
