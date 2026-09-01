class Solution:
    # Time: O(n)
    # Space: O(n)
    def count_elements(self, arr: list[int]) -> int:
        counts: set[int] = set(arr)
        return sum(x + 1 in counts for x in arr)
