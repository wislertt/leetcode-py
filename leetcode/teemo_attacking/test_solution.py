import pytest

from leetcode_py import logged_test

from .helpers import assert_find_poisoned_duration, run_find_poisoned_duration
from .solution import Solution


class TestTeemoAttacking:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "time_series, duration, expected",
        [
            ([1, 4], 2, 4),
            ([1, 2], 2, 3),
            ([1], 2, 2),
            ([5], 1, 1),
            ([1, 2, 3, 4, 5], 5, 9),
            ([1, 1, 1], 2, 2),
            ([1, 5], 0, 0),
            ([0, 10000000], 10000000, 20000000),
            ([1, 3, 5, 7, 9, 11], 1, 6),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 12),
            ([10000000], 10000000, 10000000),
            ([1, 2, 3, 10000000], 10000000, 19999999),
            ([0, 0, 1, 3, 3, 7], 4, 11),
            ([1, 3, 8], 4, 10),
            ([5, 5, 9, 10], 2, 5),
            ([3, 11, 12], 4, 9),
        ],
    )
    def test_find_poisoned_duration(self, time_series: list[int], duration: int, expected: int):
        result = run_find_poisoned_duration(Solution, time_series, duration)
        assert_find_poisoned_duration(result, expected)
