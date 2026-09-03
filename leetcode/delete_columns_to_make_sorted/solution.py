class Solution:
    # Time: O(n * m) where n = len(strs), m = len(strs[0])
    # Space: O(1)
    def min_deletion_size(self, strs: list[str]) -> int:
        return sum(
            any(strs[row][col] < strs[row - 1][col] for row in range(1, len(strs)))
            for col in range(len(strs[0]))
        )
