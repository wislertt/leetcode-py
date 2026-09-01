class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def eliminate_maximum(self, dist: list[int], speed: list[int]) -> int:
        arrival = sorted(-(-d // s) for d, s in zip(dist, speed, strict=True))
        for minute, time in enumerate(arrival):
            if time <= minute:
                return minute
        return len(arrival)
