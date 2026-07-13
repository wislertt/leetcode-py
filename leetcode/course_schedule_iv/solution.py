class Solution:
    # Time: O(n^3) Floyd-Warshall transitive closure (n <= 100)
    # Space: O(n^2)
    def check_if_prerequisite(
        self, num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        # reach[a][b] = True if a is a (direct or indirect) prerequisite of b.
        reach = [[False] * num_courses for _ in range(num_courses)]
        for a, b in prerequisites:
            reach[a][b] = True

        for k in range(num_courses):
            for i in range(num_courses):
                if reach[i][k]:
                    for j in range(num_courses):
                        if reach[k][j]:
                            reach[i][j] = True

        return [reach[u][v] for u, v in queries]
