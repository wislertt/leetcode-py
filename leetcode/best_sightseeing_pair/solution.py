class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        best = 0
        best_left = values[0]
        for j in range(1, len(values)):
            best = max(best, best_left + values[j] - j)
            best_left = max(best_left, values[j] + j)
        return best
