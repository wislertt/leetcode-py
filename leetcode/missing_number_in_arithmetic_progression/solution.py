class Solution:
    # Time: O(n)
    # Space: O(1)
    def missing_number(self, arr: list[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)
