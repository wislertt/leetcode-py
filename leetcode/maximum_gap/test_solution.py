import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_gap, run_maximum_gap
from .solution import Solution


class TestMaximumGap:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 6, 9, 1], 3),
            ([10], 0),
            ([1], 0),
            ([1, 1, 1, 1], 0),
            ([1, 10000000], 9999999),
            ([5, 5, 5, 100], 95),
            ([0, 10, 30, 31, 100], 69),
            ([1, 3, 100], 97),
            ([2, 99999999], 99999997),
            ([7, 7, 7, 7, 7, 8], 1),
            ([0, 0], 0),
            ([4, 1, 6, 3], 2),
            ([100, 3, 2, 4, 50], 50),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 1),
            ([24, 12, 36, 1, 48], 12),
            ([795979244, 323235435], 472743809),
            ([497133905, 525536988, 649667217, 412728382], 124130229),
            ([92094067, 445522750], 353428683),
        ],
    )
    def test_maximum_gap(self, nums: list[int], expected: int):
        result = run_maximum_gap(Solution, nums)
        assert_maximum_gap(result, expected)
