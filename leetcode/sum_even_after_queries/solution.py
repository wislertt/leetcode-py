class Solution:
    # Time: O(n + q)
    # Space: O(q)
    def sum_even_after_queries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result: list[int] = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            result.append(even_sum)
        return result
