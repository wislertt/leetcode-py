import pytest

from leetcode_py import logged_test

from .helpers import assert_construct_2d_array, run_construct_2d_array
from .solution import Solution


class TestConvert1dArrayInto2dArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "original, m, n, expected",
        [
            ([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),
            ([1, 2, 3], 1, 3, [[1, 2, 3]]),
            ([1, 2], 1, 1, []),
            ([3], 1, 1, [[3]]),
            ([1, 2, 3, 4, 5, 6], 2, 3, [[1, 2, 3], [4, 5, 6]]),
            ([1, 2, 3, 4, 5, 6], 3, 2, [[1, 2], [3, 4], [5, 6]]),
            ([1, 2, 3, 4, 5, 6], 6, 1, [[1], [2], [3], [4], [5], [6]]),
            ([1, 2, 3, 4], 1, 4, [[1, 2, 3, 4]]),
            ([1, 2, 3, 4], 4, 1, [[1], [2], [3], [4]]),
            ([1, 2, 3, 4], 3, 2, []),
            ([1, 2, 3, 4], 2, 3, []),
            ([5, 10], 2, 1, [[5], [10]]),
            ([7, 7, 7], 3, 1, [[7], [7], [7]]),
            ([1, 2, 3, 4, 5, 6, 7, 8], 4, 2, [[1, 2], [3, 4], [5, 6], [7, 8]]),
            ([100000, 1], 1, 2, [[100000, 1]]),
            ([9, 8, 7, 6, 5], 1, 5, [[9, 8, 7, 6, 5]]),
            ([1], 2, 1, []),
        ],
    )
    def test_construct_2d_array(
        self, original: list[int], m: int, n: int, expected: list[list[int]]
    ):
        result = run_construct_2d_array(Solution, original, m, n)
        assert_construct_2d_array(result, expected)
