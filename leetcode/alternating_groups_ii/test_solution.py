import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_alternating_groups, run_number_of_alternating_groups
from .solution import Solution


class TestAlternatingGroupsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "colors, k, expected",
        [
            ([0, 1, 0, 1, 0], 3, 3),
            ([0, 1, 0, 0, 1, 0, 1], 6, 2),
            ([1, 1, 0, 1], 4, 0),
            ([0, 1, 0], 3, 1),
            ([0, 1, 0, 1], 4, 4),
            ([1, 1, 1], 3, 0),
            ([0, 0, 1, 1], 3, 0),
            ([1, 0, 1, 0, 1, 0], 3, 6),
            ([1, 0, 1, 0, 1, 0], 6, 6),
            ([0, 0, 0, 1, 0], 4, 0),
            ([1, 1, 0, 0, 1, 1], 3, 0),
            ([0, 1, 1, 0, 1, 1, 0, 0], 4, 0),
            ([0, 1, 0, 1, 0, 1, 0, 1], 8, 8),
            ([0, 0, 1, 0, 1, 1, 0, 1, 0], 5, 0),
            ([1, 1, 0, 1, 1, 1, 0, 0, 1], 3, 1),
            ([0, 1, 0, 0, 1, 0, 0, 0, 1, 1], 7, 0),
            ([1, 0, 1, 1, 0, 0, 1, 0, 1, 0], 4, 5),
            ([0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0], 3, 4),
            ([1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], 12, 0),
            ([1, 1, 1, 0, 0, 1, 1, 0], 5, 0),
        ],
    )
    def test_number_of_alternating_groups(self, colors: list[int], k: int, expected: int):
        result = run_number_of_alternating_groups(Solution, colors, k)
        assert_number_of_alternating_groups(result, expected)
