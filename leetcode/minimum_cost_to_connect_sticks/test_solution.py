import pytest

from leetcode_py import logged_test

from .helpers import assert_connect_sticks, run_connect_sticks
from .solution import Solution


class TestMinimumCostToConnectSticks:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sticks, expected",
        [
            ([2, 4, 3], 14),
            ([1, 8, 3, 5], 30),
            ([5], 0),
            ([1, 2], 3),
            ([1, 1], 2),
            ([10, 10], 20),
            ([1, 100, 1], 104),
            ([5, 5, 5], 25),
            ([4, 3, 2, 6], 29),
            ([1, 2, 3, 4, 5], 33),
            ([3354, 4318, 769, 9973, 800], 34947),
            ([10000, 10000, 10000, 10000, 10000], 120000),
            ([1, 1, 1, 1, 1, 1, 1, 1], 24),
            ([2, 2, 2, 2, 2, 2], 32),
            ([9999, 1], 10000),
            ([7, 1, 9, 3, 5, 8], 79),
            ([1000, 2000, 3000, 4000], 19000),
        ],
    )
    def test_connect_sticks(self, sticks: list[int], expected: int):
        result = run_connect_sticks(Solution, sticks)
        assert_connect_sticks(result, expected)
