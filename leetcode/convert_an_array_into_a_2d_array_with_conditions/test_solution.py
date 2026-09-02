import pytest

from leetcode_py import logged_test

from .helpers import assert_find_matrix, run_find_matrix
from .solution import Solution


class TestConvertAnArrayIntoA2DArrayWithConditions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 4, 1, 2, 3, 1], [1, 1, 1, 2, 3, 3, 4]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([1], [1]),
            ([1, 1], [1, 1]),
            ([1, 1, 1], [1, 1, 1]),
            ([2, 1], [1, 2]),
            ([1, 2, 1], [1, 1, 2]),
            ([2, 2, 1, 1], [1, 1, 2, 2]),
            ([3, 3, 3, 1, 1, 2], [1, 1, 2, 3, 3, 3]),
            ([4, 4, 4, 4], [4, 4, 4, 4]),
            ([1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3]),
            ([2, 1, 2, 1, 2, 1], [1, 1, 1, 2, 2, 2]),
            ([5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5]),
            ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
            ([6, 6, 6, 6, 6, 6, 6], [6, 6, 6, 6, 6, 6, 6]),
            ([8, 7, 2, 7, 2, 9, 6, 1, 3, 2], [1, 2, 2, 2, 3, 6, 7, 7, 8, 9]),
            ([1, 2, 2, 1, 2], [1, 1, 2, 2, 2]),
            ([3, 8, 8, 6, 1, 3, 1, 4, 3], [1, 1, 3, 3, 3, 4, 6, 8, 8]),
            ([3, 1, 4, 5, 2, 6, 1], [1, 1, 2, 3, 4, 5, 6]),
            ([5, 5, 1, 2, 4], [1, 2, 4, 5, 5]),
            ([2, 7, 6, 8, 6, 7, 8, 8, 4], [2, 4, 6, 6, 7, 7, 8, 8, 8]),
            ([1, 1, 4, 1], [1, 1, 1, 4]),
            ([1, 4, 2, 2, 4], [1, 2, 2, 4, 4]),
        ],
    )
    def test_find_matrix(self, nums: list[int], expected: list[int]):
        result = run_find_matrix(Solution, nums)
        assert_find_matrix(result, expected)
