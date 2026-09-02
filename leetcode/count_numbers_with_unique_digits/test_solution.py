import pytest

from leetcode_py import logged_test

from .helpers import assert_count_numbers_with_unique_digits, run_count_numbers_with_unique_digits
from .solution import Solution


class TestCountNumbersWithUniqueDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 1),
            (1, 10),
            (2, 91),
            (3, 739),
            (4, 5275),
            (5, 32491),
            (6, 168571),
            (7, 712891),
            (8, 2345851),
            (8, 2345851),
            (0, 1),
            (3, 739),
        ],
    )
    def test_count_numbers_with_unique_digits(self, n: int, expected: int):
        result = run_count_numbers_with_unique_digits(Solution, n)
        assert_count_numbers_with_unique_digits(result, expected)
