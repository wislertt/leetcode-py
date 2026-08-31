import pytest

from leetcode_py import logged_test

from .helpers import assert_height_checker, run_height_checker
from .solution import Solution


class TestHeightChecker:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([1, 1, 4, 2, 1, 3], 3),
            ([5, 1, 2, 3, 4], 5),
            ([1, 2, 3, 4, 5], 0),
            ([1], 0),
            ([2, 2], 0),
            ([2, 1], 2),
            ([1, 1, 1, 1], 0),
            ([3, 3, 2, 2], 4),
            ([1, 2, 1, 2], 2),
            ([5, 4, 3, 2, 1], 4),
            ([100, 1], 2),
            ([1, 3, 2, 4, 3, 5], 4),
        ],
    )
    def test_height_checker(self, heights: list[int], expected: int):
        result = run_height_checker(Solution, heights)
        assert_height_checker(result, expected)
