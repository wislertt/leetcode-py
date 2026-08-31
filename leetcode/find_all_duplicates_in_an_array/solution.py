class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_duplicates(self, nums: list[int]) -> list[int]:
        result: list[int] = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return result
