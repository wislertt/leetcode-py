from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_error_nums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = Counter(nums)
        duplicate = missing = -1
        for value in range(1, n + 1):
            if counts[value] == 2:
                duplicate = value
            elif counts[value] == 0:
                missing = value
        return [duplicate, missing]
