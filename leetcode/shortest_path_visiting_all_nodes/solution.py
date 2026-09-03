from collections import deque


class Solution:
    # Time: O(n * 2^n * n) = O(n^2 * 2^n) - each state dequeued once, n edges per state
    # Space: O(n * 2^n) for the visited-state set
    def shortest_path_length(self, graph: list[list[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1
        queue: deque[tuple[int, int]] = deque((node, 1 << node) for node in range(n))
        seen = {(node, 1 << node) for node in range(n)}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()
                if mask == full:
                    return steps
                for neighbor in graph[node]:
                    state = (neighbor, mask | (1 << neighbor))
                    if state not in seen:
                        seen.add(state)
                        queue.append(state)
            steps += 1
        return steps
