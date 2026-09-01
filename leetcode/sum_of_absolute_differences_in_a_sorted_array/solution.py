class Solution:
    # Time: O(n)
    # Space: O(n)
    def get_sum_absolute_differences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, value in enumerate(nums):
            prefix[i + 1] = prefix[i] + value

        total = prefix[n]
        result = []
        for i, value in enumerate(nums):
            left_sum = i * value - prefix[i]
            right_sum = (total - prefix[i + 1]) - (n - i - 1) * value
            result.append(left_sum + right_sum)
        return result
