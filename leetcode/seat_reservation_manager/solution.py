import heapq


class SeatManager:
    # Time: O(1) init, O(log n) reserve, O(log n) unreserve
    # Space: O(n)
    def __init__(self, n: int) -> None:
        self.next_seat = 1
        self.returned: list[int] = []

    def reserve(self) -> int:
        if self.returned and self.returned[0] < self.next_seat:
            return heapq.heappop(self.returned)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.returned, seat_number)
