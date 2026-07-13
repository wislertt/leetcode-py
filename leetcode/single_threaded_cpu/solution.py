import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def get_order(self, tasks: list[list[int]]) -> list[int]:
        indexed = sorted(range(len(tasks)), key=lambda i: tasks[i][0])

        order: list[int] = []
        heap: list[tuple[int, int]] = []
        time = 0
        pointer = 0
        n = len(tasks)

        while len(order) < n:
            while pointer < n and tasks[indexed[pointer]][0] <= time:
                idx = indexed[pointer]
                heapq.heappush(heap, (tasks[idx][1], idx))
                pointer += 1

            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                order.append(idx)
            else:
                time = tasks[indexed[pointer]][0]

        return order
