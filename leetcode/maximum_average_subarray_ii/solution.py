class Solution:
    # Time: O(n log M) where M = max(nums) - min(nums)
    # Space: O(1)
    def find_max_average(self, nums: list[int], k: int) -> float:
        def check(v: float) -> bool:
            s = sum(nums[:k]) - k * v
            if s >= 0:
                return True
            t = mi = 0.0
            for i in range(k, len(nums)):
                s += nums[i] - v
                t += nums[i - k] - v
                mi = min(mi, t)
                if s >= mi:
                    return True
            return False

        eps = 1e-5
        lo, hi = min(nums), max(nums)
        while hi - lo >= eps:
            mid = (lo + hi) / 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo
