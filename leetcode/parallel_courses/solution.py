from collections import deque


class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def minimum_semesters(self, n: int, relations: list[list[int]]) -> int:
        graph: list[list[int]] = [[] for _ in range(n)]
        indegree = [0] * n
        for prev_course, next_course in relations:
            graph[prev_course - 1].append(next_course - 1)
            indegree[next_course - 1] += 1

        queue: deque[int] = deque(i for i in range(n) if indegree[i] == 0)
        semesters = 0
        taken = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for nxt in graph[course]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
        return semesters if taken == n else -1
