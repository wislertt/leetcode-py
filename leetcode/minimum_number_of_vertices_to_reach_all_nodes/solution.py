class Solution:
    # Time: O(n + e)
    # Space: O(n)
    def find_smallest_set_of_vertices(self, n: int, edges: list[list[int]]) -> list[int]:
        has_incoming = [False] * n
        for _from, to in edges:
            has_incoming[to] = True
        return [node for node in range(n) if not has_incoming[node]]
