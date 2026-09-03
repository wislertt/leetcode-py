import pytest

from leetcode_py import logged_test

from .helpers import assert_three_equal_parts, run_three_equal_parts
from .solution import Solution


class TestThreeEqualParts:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 0, 1, 0, 1], [0, 3]),
            ([1, 1, 0, 1, 1], [-1, -1]),
            ([1, 1, 0, 0, 1], [0, 2]),
            ([0, 0, 0], [0, 2]),
            ([0, 1, 0], [-1, -1]),
            ([1, 1, 0], [-1, -1]),
            ([1, 0, 0, 1, 0, 0, 1], [0, 4]),
            ([1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 5]),
            ([0, 1, 0, 1, 0, 1], [1, 4]),
            ([1, 0, 1, 0, 1, 0, 0], [-1, -1]),
            ([1, 1, 1, 0, 0, 0, 0, 0, 0], [-1, -1]),
            ([0, 0, 1, 0, 0, 1, 0, 0, 1], [2, 6]),
            ([1, 1, 1, 1, 1, 1], [1, 4]),
            ([1, 1, 1, 1], [-1, -1]),
            ([0, 0, 0, 0, 0, 0], [0, 5]),
            ([1, 1, 0, 1, 1, 0, 1, 1, 0], [2, 6]),
            ([0, 1, 1], [-1, -1]),
            ([1, 1, 0, 0, 0], [-1, -1]),
            ([0, 0, 1, 1], [-1, -1]),
            ([1, 0, 1], [-1, -1]),
            ([0, 0, 0, 1, 1], [-1, -1]),
            ([0, 0, 1, 0, 0, 0, 1, 1, 0], [-1, -1]),
            ([0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 10]),
            ([0, 1, 1, 1, 0], [-1, -1]),
            ([1, 0, 1, 0, 1, 1, 1], [-1, -1]),
            ([0, 1, 0, 1, 0], [-1, -1]),
        ],
    )
    def test_three_equal_parts(self, arr: list[int], expected: list[int]):
        result = run_three_equal_parts(Solution, arr)
        assert_three_equal_parts(result, expected)
