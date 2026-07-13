import heapq


class Solution:
    # Time: O((n + k) * log n) sorting + heap operations
    # Space: O(n) for the heap
    def find_maximized_capital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Sort projects by required capital ascending.
        projects = sorted(zip(capital, profits, strict=True))
        heap: list[int] = []  # max-heap of profits (stored negated)
        index = 0
        n = len(projects)
        current = w
        for _ in range(k):
            # Push every project now affordable into the profit heap.
            while index < n and projects[index][0] <= current:
                heapq.heappush(heap, -projects[index][1])
                index += 1
            if not heap:
                break
            current += -heapq.heappop(heap)
        return current
