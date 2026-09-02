class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_subarrays(self, nums: list[int], k: int) -> int:
        mx = max(nums)
        total = 0
        count = 0
        left = 0
        for value in nums:
            if value == mx:
                count += 1
            while count >= k:
                if nums[left] == mx:
                    count -= 1
                left += 1
            total += left
        return total
