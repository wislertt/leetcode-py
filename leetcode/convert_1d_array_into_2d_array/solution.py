class Solution:
    # Time: O(len(original))
    # Space: O(m * n) for the output
    def construct_2d_array(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        return [original[i * n : (i + 1) * n] for i in range(m)]
