class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def num_teams(self, rating: list[int]) -> int:
        n = len(rating)
        total = 0
        for mid in range(n):
            less_before = sum(rating[i] < rating[mid] for i in range(mid))
            greater_before = mid - less_before
            less_after = sum(rating[k] < rating[mid] for k in range(mid + 1, n))
            greater_after = n - mid - 1 - less_after
            total += less_before * greater_after + greater_before * less_after
        return total
