class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Sort cars by position descending (closest to target first).
        cars = sorted(zip(position, speed, strict=False), reverse=True)
        fleets = 0
        slowest_arrival = 0.0
        for pos, spd in cars:
            arrival = (target - pos) / spd
            # A car forms a new fleet only if it arrives strictly later than
            # the fleet ahead of it; otherwise it catches up and merges.
            if arrival > slowest_arrival:
                fleets += 1
                slowest_arrival = arrival
        return fleets
