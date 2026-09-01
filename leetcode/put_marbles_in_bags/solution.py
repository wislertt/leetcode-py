class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def put_marbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        pair_sums = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        splits = k - 1
        return sum(pair_sums[-splits:]) - sum(pair_sums[:splits])
