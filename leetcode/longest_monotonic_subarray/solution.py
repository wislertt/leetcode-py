class Solution:
    # Time: O(n)
    # Space: O(1)
    def longest_monotonic_subarray(self, nums: list[int]) -> int:
        best = 1
        inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            best = max(best, inc, dec)
        return best
