class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def rearrange_array(self, nums: list[int]) -> list[int]:
        result = sorted(nums)
        for i in range(0, len(result) - 1, 2):
            result[i], result[i + 1] = result[i + 1], result[i]
        return result
