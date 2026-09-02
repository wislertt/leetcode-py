class Solution:
    # Time: O(log n)
    # Space: O(1)
    def missing_element(self, nums: list[int], k: int) -> int:
        def missing(i: int) -> int:
            return nums[i] - nums[0] - i

        n = len(nums)
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if missing(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return nums[left - 1] + k - missing(left - 1)
