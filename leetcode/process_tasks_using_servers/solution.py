import heapq


class Solution:
    # Time: O((n + m) log n)
    # Space: O(n)
    def assign_tasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy: list[tuple[int, int, int]] = []  # (free_at, weight, index)
        ans: list[int] = []
        time = 0
        for j, dur in enumerate(tasks):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + dur, w, i))
        return ans
