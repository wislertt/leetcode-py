from itertools import pairwise


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def lexicographically_smallest_array(self, nums: list[int], limit: int) -> list[int]:
        order = sorted(range(len(nums)), key=lambda i: nums[i])
        result: list[int] = [0] * len(nums)
        group: list[int] = [order[0]]
        for prev, idx in pairwise(order):
            if nums[idx] - nums[prev] > limit:
                self._assign_group(result, group, nums)
                group = []
            group.append(idx)
        self._assign_group(result, group, nums)
        return result

    def _assign_group(self, result: list[int], indices: list[int], nums: list[int]) -> None:
        values = sorted(nums[i] for i in indices)
        for pos, val in zip(sorted(indices), values, strict=True):
            result[pos] = val
