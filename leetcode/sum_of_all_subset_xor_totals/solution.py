class Solution:
    # Time: O(n * 2^n)
    # Space: O(n)
    def subset_xor_sum(self, nums: list[int]) -> int:
        def backtrack(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor

            include = backtrack(index + 1, current_xor ^ nums[index])
            exclude = backtrack(index + 1, current_xor)

            return include + exclude

        return backtrack(0, 0)
