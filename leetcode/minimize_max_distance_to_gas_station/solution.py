class Solution:
    # Time: O(n log M) where M = max gap
    # Space: O(1)
    def minmax_gas_dist(self, stations: list[int], k: int) -> float:
        gaps = [stations[i + 1] - stations[i] for i in range(len(stations) - 1)]

        def check(x: float) -> bool:
            return sum(int(g / x) for g in gaps) <= k

        left, right = 0.0, float(max(gaps))
        while right - left > 1e-6:
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return left
