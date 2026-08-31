import pytest

from leetcode_py import logged_test

from .helpers import assert_nth_ugly_number, run_nth_ugly_number
from .solution import Solution


class TestUglyNumberII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 8),
            (8, 9),
            (9, 10),
            (10, 12),
            (11, 15),
            (15, 24),
            (20, 36),
            (50, 243),
            (100, 1536),
            (235, 30720),
            (500, 937500),
            (666, 4423680),
            (1000, 51200000),
            (1690, 2123366400),
        ],
    )
    def test_nth_ugly_number(self, n: int, expected: int):
        result = run_nth_ugly_number(Solution, n)
        assert_nth_ugly_number(result, expected)
