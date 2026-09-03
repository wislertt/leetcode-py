import pytest

from leetcode_py import logged_test

from .helpers import assert_max_dist_to_closest, run_max_dist_to_closest
from .solution import Solution


class TestMaximizeDistanceToClosestPerson:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "seats, expected",
        [
            ([1, 0, 0, 0, 1, 0, 1], 2),
            ([1, 0, 0, 0], 3),
            ([0, 1], 1),
            ([1, 0], 1),
            ([0, 0, 1], 2),
            ([1, 0, 0, 0, 0], 4),
            ([1, 0, 1], 1),
            ([1, 0, 0, 1], 1),
            ([1, 0, 0, 0, 1], 2),
            ([0, 1, 0, 0, 0, 1], 2),
            ([1, 1, 1, 1, 0], 1),
            ([0, 1, 1, 1, 1], 1),
            ([1, 0, 1, 0, 1], 1),
            ([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 5),
            ([1, 0, 0, 1, 0, 0, 0, 1], 2),
            ([1, 1, 0, 0, 0, 0, 1, 0, 0], 2),
            ([0, 0, 1, 1, 1, 0], 2),
            ([1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0], 1),
            ([0, 1, 1, 0, 0, 0, 1, 0], 2),
            ([0, 1, 0, 0, 0, 0, 0, 1], 3),
        ],
    )
    def test_max_dist_to_closest(self, seats: list[int], expected: int):
        result = run_max_dist_to_closest(Solution, seats)
        assert_max_dist_to_closest(result, expected)
