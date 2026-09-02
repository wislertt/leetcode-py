from collections import defaultdict, deque


class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_reorder(self, n: int, connections: list[list[int]]) -> int:
        adjacency: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for src, dst in connections:
            adjacency[src].append((dst, 1))
            adjacency[dst].append((src, 0))

        flips = 0
        visited = [False] * n
        visited[0] = True
        queue: deque[int] = deque([0])
        while queue:
            city = queue.popleft()
            for neighbor, directed_out in adjacency[city]:
                if visited[neighbor]:
                    continue
                flips += directed_out
                visited[neighbor] = True
                queue.append(neighbor)
        return flips
