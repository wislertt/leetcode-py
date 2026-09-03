class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_length_of_lcis(self, nums: list[int]) -> int:
        best = 1
        run = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                run += 1
                best = max(best, run)
            else:
                run = 1
        return best
