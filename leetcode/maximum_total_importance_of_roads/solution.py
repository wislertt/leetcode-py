class Solution:
    # Time: O(E + V log V) where E = len(roads), V = n
    # Space: O(V)
    def maximum_importance(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        return sum(d * (i + 1) for i, d in enumerate(degree))
