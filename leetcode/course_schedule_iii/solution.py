import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def schedule_course(self, courses: list[list[int]]) -> int:
        taken: list[int] = []
        total = 0
        for duration, last_day in sorted(courses, key=lambda c: c[1]):
            heapq.heappush(taken, -duration)
            total += duration
            if total > last_day:
                total += heapq.heappop(taken)
        return len(taken)
