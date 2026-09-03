class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_max_average(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            if window > best:
                best = window
        return best / k
