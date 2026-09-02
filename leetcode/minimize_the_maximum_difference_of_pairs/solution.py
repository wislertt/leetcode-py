class Solution:
    # Time: O(n log n + n log m) where m = max(nums) - min(nums)
    # Space: O(n) for the sorted copy
    def minimize_max(self, nums: list[int], p: int) -> int:
        vals = sorted(nums)
        n = len(vals)

        def can_pair(target: int) -> bool:
            count = 0
            i = 0
            while i < n - 1:
                if vals[i + 1] - vals[i] <= target:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        low, high = 0, vals[-1] - vals[0]
        while low < high:
            mid = (low + high) // 2
            if can_pair(mid):
                high = mid
            else:
                low = mid + 1
        return low
