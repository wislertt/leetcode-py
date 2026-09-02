class Solution:
    def find_the_city(self, n: int, edges: list[list[int]], distance_threshold: int) -> int:
        inf = 10**9
        dist = [[inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        best_city, best_count = -1, n + 1
        for i in range(n):
            count = sum(1 for j in range(n) if j != i and dist[i][j] <= distance_threshold)
            if count <= best_count:
                best_count = count
                best_city = i
        return best_city
