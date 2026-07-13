import heapq


class Solution:
    # Time: O(m log m + m log n)
    # Space: O(n)
    def most_booked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda meeting: meeting[0])

        available: list[int] = list(range(n))
        ongoing: list[tuple[int, int]] = []
        counts = [0] * n

        for start, end in meetings:
            while ongoing and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                counts[room] += 1
                heapq.heappush(ongoing, (end, room))
            else:
                free_time, room = heapq.heappop(ongoing)
                counts[room] += 1
                duration = end - start
                heapq.heappush(ongoing, (free_time + duration, room))

        best_room = 0
        for room in range(1, n):
            if counts[room] > counts[best_room]:
                best_room = room

        return best_room
