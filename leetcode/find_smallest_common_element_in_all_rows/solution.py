class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def smallest_common_element(self, mat: list[list[int]]) -> int:
        counts: dict[int, int] = {}
        for row in mat:
            for x in row:
                count = counts.get(x, 0) + 1
                if count == len(mat):
                    return x
                counts[x] = count
        return -1
