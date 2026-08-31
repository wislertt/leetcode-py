class Solution:
    # Time: O(n)
    # Space: O(n)
    def sort_array_by_parity(self, nums: list[int]) -> list[int]:
        result = [num for num in nums if num % 2 == 0]
        result.extend(num for num in nums if num % 2 == 1)
        return result
