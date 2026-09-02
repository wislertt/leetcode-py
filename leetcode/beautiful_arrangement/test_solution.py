import pytest

from leetcode_py import logged_test

from .helpers import assert_count_arrangement, run_count_arrangement
from .solution import Solution


class TestBeautifulArrangement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 8),
            (5, 10),
            (6, 36),
            (7, 41),
            (8, 132),
            (9, 250),
            (10, 700),
            (11, 750),
            (12, 4010),
            (13, 4237),
            (14, 10680),
            (15, 24679),
        ],
    )
    def test_count_arrangement(self, n: int, expected: int):
        result = run_count_arrangement(Solution, n)
        assert_count_arrangement(result, expected)
