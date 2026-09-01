class Solution:
    # Time: O(n)
    # Space: O(n)
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result: list[int] = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + n]
        return result
