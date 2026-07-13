from collections import defaultdict, deque


class Solution:
    # Time: O(k + n + m)
    # Space: O(k + n + m)
    def build_matrix(
        self, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]
    ) -> list[list[int]]:
        def topological_order(conditions: list[list[int]]) -> list[int]:
            graph: dict[int, list[int]] = defaultdict(list)
            indegree = [0] * (k + 1)
            for above, below in conditions:
                graph[above].append(below)
                indegree[below] += 1

            queue = deque(node for node in range(1, k + 1) if indegree[node] == 0)
            order: list[int] = []

            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            return order if len(order) == k else []

        row_order = topological_order(row_conditions)
        if not row_order:
            return []

        col_order = topological_order(col_conditions)
        if not col_order:
            return []

        column_index = {number: idx for idx, number in enumerate(col_order)}
        matrix = [[0] * k for _ in range(k)]
        for row, number in enumerate(row_order):
            matrix[row][column_index[number]] = number

        return matrix
