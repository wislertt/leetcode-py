import pytest

from leetcode_py import logged_test

from .helpers import assert_count_digit_one, run_count_digit_one
from .solution import Solution


class TestNumberOfDigitOne:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (9, 1),
            (10, 2),
            (11, 4),
            (12, 5),
            (13, 6),
            (19, 12),
            (20, 12),
            (21, 13),
            (99, 20),
            (100, 21),
            (101, 23),
            (110, 33),
            (111, 36),
            (199, 140),
            (999, 300),
            (1000, 301),
            (1234, 689),
            (9999, 4000),
            (12345, 8121),
            (30000, 22000),
            (30001, 22001),
            (30003, 22001),
            (30010, 22002),
            (30011, 22004),
            (30013, 22006),
            (100000, 50001),
            (1000000, 600001),
            (10000000, 7000001),
            (123456789, 130589849),
            (82488329, 68545573),
            (999999999, 900000000),
            (1000000000, 900000001),
        ],
    )
    def test_count_digit_one(self, n: int, expected: int):
        result = run_count_digit_one(Solution, n)
        assert_count_digit_one(result, expected)
