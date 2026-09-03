import pytest

from leetcode_py import logged_test

from .helpers import assert_reach_number, run_reach_number
from .solution import Solution


class TestReachANumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, expected",
        [
            (1, 1),
            (2, 3),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 3),
            (7, 5),
            (8, 4),
            (9, 5),
            (10, 4),
            (11, 5),
            (12, 7),
            (13, 5),
            (14, 7),
            (15, 5),
            (16, 7),
            (17, 6),
            (18, 7),
            (19, 6),
            (20, 7),
            (25, 9),
            (30, 8),
            (50, 11),
            (100, 15),
            (111, 17),
            (1000, 47),
            (12345, 157),
            (99999, 449),
            (1000000000, 44723),
            (999999999, 44721),
            (999999937, 44721),
            (1073741824, 46343),
            (-1, 1),
            (-2, 3),
            (-3, 2),
            (-5, 5),
            (-11, 5),
            (-1000, 47),
            (-999999937, 44721),
            (-1000000000, 44723),
            (-999999999, 44721),
            (44, 11),
            (45, 9),
            (46, 11),
            (44721, 301),
            (44722, 299),
        ],
    )
    def test_reach_number(self, target: int, expected: int):
        result = run_reach_number(Solution, target)
        assert_reach_number(result, expected)
