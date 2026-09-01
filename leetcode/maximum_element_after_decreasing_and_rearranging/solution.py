class Solution:
    # Time: O(n log n)
    # Space: O(1) extra (sorting in place)
    def maximum_element(self, arr: list[int]) -> int:
        arr.sort()
        prev = 0
        for value in arr:
            prev = min(prev + 1, value)
        return prev
