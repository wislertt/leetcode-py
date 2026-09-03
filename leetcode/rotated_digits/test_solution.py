import pytest

from leetcode_py import logged_test

from .helpers import assert_rotated_digits, run_rotated_digits
from .solution import Solution


class TestRotatedDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 2),
            (6, 3),
            (7, 3),
            (8, 3),
            (9, 4),
            (10, 4),
            (11, 4),
            (15, 6),
            (20, 9),
            (25, 12),
            (30, 15),
            (50, 16),
            (68, 28),
            (99, 40),
            (100, 40),
            (251, 103),
            (857, 247),
            (1000, 316),
            (2345, 779),
            (6789, 1563),
            (9999, 2320),
            (10000, 2320),
        ],
    )
    def test_rotated_digits(self, n: int, expected: int):
        result = run_rotated_digits(Solution, n)
        assert_rotated_digits(result, expected)
