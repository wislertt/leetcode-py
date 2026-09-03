import pytest

from leetcode_py import logged_test

from .helpers import assert_num_factored_binary_trees, run_num_factored_binary_trees
from .solution import Solution


class TestBinaryTreesWithFactors:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 4], 3),
            ([2, 4, 5, 10], 7),
            ([2], 1),
            ([3], 1),
            ([1000000000], 1),
            ([2, 3], 2),
            ([2, 3, 5], 3),
            ([2, 4, 8, 16], 23),
            ([3, 9, 27, 81], 23),
            ([2, 4, 3, 6, 12], 18),
            ([5, 25, 125, 625, 3125], 74),
            ([18, 2, 9, 3, 6], 18),
            ([7, 49, 343], 8),
            ([1000000000, 2, 4], 4),
            ([4, 2, 16, 8, 64], 109),
            ([2, 4, 10, 16, 21, 27, 28, 32, 59], 24),
            ([5, 9, 10, 19, 29, 30, 39, 58], 8),
            ([2, 16, 18, 21, 29, 31, 40, 45, 59], 9),
            ([11, 15, 17, 21, 47, 50], 6),
            ([2, 6, 7, 9, 41], 5),
            ([17, 26, 52, 56, 57], 5),
            ([6, 10, 27, 35, 38, 45, 58], 7),
            ([6, 20, 21, 23, 28, 34, 41, 45, 46], 9),
        ],
    )
    def test_num_factored_binary_trees(self, arr: list[int], expected: int):
        result = run_num_factored_binary_trees(Solution, arr)
        assert_num_factored_binary_trees(result, expected)
