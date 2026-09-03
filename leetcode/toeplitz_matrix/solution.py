from itertools import pairwise


class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def is_toeplitz_matrix(self, matrix: list[list[int]]) -> bool:
        return all(row[:-1] == below[1:] for row, below in pairwise(matrix))
