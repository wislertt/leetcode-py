class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def two_city_sched_cost(self, costs: list[list[int]]) -> int:
        ordered = sorted(costs, key=lambda cost: cost[0] - cost[1])
        n = len(ordered) // 2
        return sum(cost[0] for cost in ordered[:n]) + sum(cost[1] for cost in ordered[n:])
