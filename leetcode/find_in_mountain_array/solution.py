class MountainArray:
    def get(self, index: int) -> int:
        raise NotImplementedError

    def length(self) -> int:
        raise NotImplementedError


class Solution:
    # Time: O(log n) — three binary searches (peak, ascending side, descending side)
    # Space: O(1)
    def find_in_mountain_array(self, target: int, mountain_arr: MountainArray) -> int:
        n = mountain_arr.length()

        # 1. Find the peak index (mountainArr is strictly increasing then decreasing).
        lo, hi = 1, n - 2
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # 2. Binary search the strictly ascending left slope for target (min index).
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mountain_arr.get(mid)
            if value == target:
                return mid
            if value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # 3. Binary search the strictly descending right slope for target.
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mountain_arr.get(mid)
            if value == target:
                return mid
            if value > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
