class Solution:
    # Time: O(n + L) where n = len(trips), L = max location (1001)
    # Space: O(L) for the difference array
    def car_pooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Difference array: pickups add passengers at `from`, drop-offs remove at `to`.
        delta: list[int] = [0] * 1001
        for passengers, start, end in trips:
            delta[start] += passengers
            delta[end] -= passengers

        current = 0
        for load in delta:
            current += load
            if current > capacity:
                return False

        return True
