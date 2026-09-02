import pytest

from leetcode_py import logged_test

from .helpers import assert_check_perfect_number, run_check_perfect_number
from .solution import Solution


class TestPerfectNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (28, True),
            (7, False),
            (6, True),
            (496, True),
            (8128, True),
            (33550336, True),
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (12, False),
            (24, False),
            (100, False),
            (120, False),
            (495, False),
            (497, False),
            (999999, False),
            (33550335, False),
            (33550337, False),
            (8127, False),
            (8129, False),
            (100000000, False),
            (1000000, False),
        ],
    )
    def test_check_perfect_number(self, num: int, expected: bool):
        result = run_check_perfect_number(Solution, num)
        assert_check_perfect_number(result, expected)
