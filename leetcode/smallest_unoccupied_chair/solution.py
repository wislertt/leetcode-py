import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def smallest_chair(self, times: list[list[int]], target_friend: int) -> int:
        free: list[int] = []
        leaving: list[tuple[int, int]] = []
        next_chair = 0
        for i in sorted(range(len(times)), key=lambda idx: times[idx][0]):
            arrive = times[i][0]
            while leaving and leaving[0][0] <= arrive:
                heapq.heappush(free, heapq.heappop(leaving)[1])
            if free:
                chair = heapq.heappop(free)
            else:
                chair = next_chair
                next_chair += 1
            if i == target_friend:
                return chair
            heapq.heappush(leaving, (times[i][1], chair))
        return -1
