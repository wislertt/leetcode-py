class Solution:
    # Time: O(n log n * d) where d is the digit count
    # Space: O(n)
    def sort_jumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda num: int("".join(str(mapping[int(d)]) for d in str(num))))
