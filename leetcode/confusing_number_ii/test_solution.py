import pytest

from leetcode_py import logged_test

from .helpers import assert_confusing_number_ii, run_confusing_number_ii
from .solution import Solution


class TestConfusingNumberII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (5, 0),
            (6, 1),
            (9, 2),
            (10, 3),
            (11, 3),
            (15, 3),
            (19, 6),
            (20, 6),
            (25, 6),
            (50, 6),
            (59, 6),
            (60, 7),
            (65, 8),
            (85, 12),
            (89, 14),
            (99, 18),
            (100, 19),
            (101, 19),
            (116, 24),
            (150, 26),
            (200, 40),
            (500, 40),
            (689, 57),
            (1000, 107),
            (2000, 226),
            (5000, 226),
            (10000, 587),
            (15000, 830),
            (20000, 1196),
        ],
    )
    def test_confusing_number_ii(self, n: int, expected: int):
        result = run_confusing_number_ii(Solution, n)
        assert_confusing_number_ii(result, expected)
