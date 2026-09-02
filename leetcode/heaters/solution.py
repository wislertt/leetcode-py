import bisect


class Solution:
    # Time: O(n log n + m log m) for the sorts, then O(m log n) lookups
    # Space: O(1) extra beyond the in-place sorts
    def find_radius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            dists: list[int] = []
            if i > 0:
                dists.append(house - heaters[i - 1])
            if i < len(heaters):
                dists.append(heaters[i] - house)
            radius = max(radius, min(dists))
        return radius
