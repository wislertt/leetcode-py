class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy and the output
    def divide_array(self, nums: list[int], k: int) -> list[list[int]]:
        nums_sorted = sorted(nums)
        result: list[list[int]] = []
        for i in range(0, len(nums_sorted), 3):
            group = nums_sorted[i : i + 3]
            if group[2] - group[0] > k:
                return []
            result.append(group)
        return result
