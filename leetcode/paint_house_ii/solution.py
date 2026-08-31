class Solution:
    # Time: O(nk)
    # Space: O(k)
    def min_cost_ii(self, costs: list[list[int]]) -> int:
        best = costs[0][:]
        for house in costs[1:]:
            min1 = min(best)
            min1_idx = best.index(min1)
            min2 = min(value for idx, value in enumerate(best) if idx != min1_idx)
            best = [cost + (min2 if idx == min1_idx else min1) for idx, cost in enumerate(house)]
        return min(best)
