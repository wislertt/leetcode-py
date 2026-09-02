import pytest

from leetcode_py import logged_test

from .helpers import assert_poor_pigs, run_poor_pigs
from .solution import Solution


class TestPoorPigs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "buckets, minutes_to_die, minutes_to_test, expected",
        [
            (4, 15, 15, 2),
            (4, 15, 30, 2),
            (1, 15, 15, 0),
            (1, 1, 1, 0),
            (1, 100, 100, 0),
            (2, 1, 1, 1),
            (2, 15, 15, 1),
            (3, 1, 1, 2),
            (5, 15, 15, 3),
            (100, 15, 15, 7),
            (500, 15, 15, 9),
            (1000, 15, 15, 10),
            (1000, 15, 30, 7),
            (1000, 15, 60, 5),
            (1000, 1, 100, 2),
            (25, 15, 15, 5),
            (999, 15, 15, 10),
            (998, 15, 30, 7),
            (544, 10, 87, 3),
            (91, 57, 61, 7),
            (363, 37, 99, 6),
            (833, 92, 100, 10),
            (19, 74, 96, 5),
            (333, 59, 78, 9),
            (759, 10, 12, 10),
            (303, 47, 62, 9),
        ],
    )
    def test_poor_pigs(
        self, buckets: int, minutes_to_die: int, minutes_to_test: int, expected: int
    ):
        result = run_poor_pigs(Solution, buckets, minutes_to_die, minutes_to_test)
        assert_poor_pigs(result, expected)
