import pytest

from leetcode_py import logged_test

from .helpers import assert_k_smallest_pairs, run_k_smallest_pairs
from .solution import Solution


class TestFindKPairsWithSmallestSums:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, k, expected",
        [
            ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
            ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
            ([1, 2], [3], 1, [[1, 3]]),
            ([-5], [-3], 1, [[-5, -3]]),
            ([1, 2, 3], [4, 5], 6, [[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]]),
            ([1, 3, 5], [2, 4], 3, [[1, 2], [1, 4], [3, 2]]),
            ([0, 1], [0, 2], 2, [[0, 0], [1, 0]]),
            ([-2, 1], [-1, 3], 3, [[-2, -1], [1, -1], [-2, 3]]),
            ([1], [1, 2, 3], 3, [[1, 1], [1, 2], [1, 3]]),
            ([1, 1, 1], [1], 3, [[1, 1], [1, 1], [1, 1]]),
            ([1, 4, 7, 10], [2, 5, 8], 6, [[1, 2], [1, 5], [4, 2], [1, 8], [4, 5], [7, 2]]),
            ([2, 4], [1, 3], 1, [[2, 1]]),
            ([-1000, 0, 1000], [-500, 500], 3, [[-1000, -500], [-1000, 500], [0, -500]]),
            ([1, 2], [1, 2], 4, [[1, 1], [1, 2], [2, 1], [2, 2]]),
            ([4], [5], 1, [[4, 5]]),
            ([3, 3], [-1, 0], 4, [[3, -1], [3, -1], [3, 0], [3, 0]]),
            ([-5, -1, 1, 4], [-6, -2, 4], 1, [[-5, -6]]),
            ([-5], [4], 1, [[-5, 4]]),
            ([-1, 4], [-5, -3, -1], 3, [[-1, -5], [-1, -3], [-1, -1]]),
            ([4], [-2, 1, 1], 3, [[4, -2], [4, 1], [4, 1]]),
        ],
    )
    def test_k_smallest_pairs(
        self, nums1: list[int], nums2: list[int], k: int, expected: list[list[int]]
    ):
        result = run_k_smallest_pairs(Solution, nums1, nums2, k)
        assert_k_smallest_pairs(result, expected)
