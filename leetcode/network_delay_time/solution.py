import heapq


class Solution:
    # Time: O(E log V) where E = edges, V = nodes
    # Space: O(V + E)
    def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list (1-indexed)
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
        for source, target, weight in times:
            graph[source].append((target, weight))

        # Dijkstra from source k
        distances: list[int | float] = [float("inf")] * (n + 1)
        distances[k] = 0
        min_heap: list[tuple[int, int]] = [(0, k)]  # (time, node)

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                arrival = time + weight
                if arrival < distances[neighbor]:
                    distances[neighbor] = arrival
                    heapq.heappush(min_heap, (arrival, neighbor))

        max_time = max(distances[1:])
        return int(max_time) if max_time != float("inf") else -1
