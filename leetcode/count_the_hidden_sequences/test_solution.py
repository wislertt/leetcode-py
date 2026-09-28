import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_arrays, run_number_of_arrays
from .solution import Solution


class TestCountTheHiddenSequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "differences, lower, upper, expected",
        [
            ([1, -3, 4], 1, 6, 2),
            ([3, -4, 5, 1, -2], -4, 5, 4),
            ([4, -7, 2], 3, 6, 0),
            ([1], 1, 2, 1),
            ([1], 1, 1, 0),
            ([0], 5, 5, 1),
            ([0, 0, 0], -2, 2, 5),
            ([1, 1, 1], 0, 3, 1),
            ([-1, -1, -1], -3, 0, 1),
            ([2, -2, 2, -2], 0, 4, 3),
            ([5, -5], -10, 10, 16),
            ([100000], -100000, 100000, 100001),
        ],
    )
    def test_number_of_arrays(self, differences: list[int], lower: int, upper: int, expected: int):
        result = run_number_of_arrays(Solution, differences, lower, upper)
        assert_number_of_arrays(result, expected)
