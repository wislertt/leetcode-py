from collections import deque


class Solution:
    # Time: O(n + e)
    # Space: O(n + e)
    def minimum_time(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adj: list[list[int]] = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for prev_course, next_course in relations:
            adj[prev_course].append(next_course)
            indegree[next_course] += 1

        finish = [0] * (n + 1)
        queue: deque[int] = deque()
        for course in range(1, n + 1):
            if indegree[course] == 0:
                finish[course] = time[course - 1]
                queue.append(course)

        while queue:
            course = queue.popleft()
            for nxt in adj[course]:
                finish[nxt] = max(finish[nxt], finish[course] + time[nxt - 1])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return max(finish)
