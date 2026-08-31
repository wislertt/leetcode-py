import pytest

from leetcode_py import logged_test

from .helpers import assert_find_kth_number, run_find_kth_number
from .solution import Solution


class TestKThSmallestInLexicographicalOrder:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (13, 2, 10),
            (1, 1, 1),
            (13, 1, 1),
            (13, 5, 13),
            (13, 13, 9),
            (13, 10, 6),
            (10, 3, 2),
            (100, 10, 17),
            (100, 3, 100),
            (100, 100, 99),
            (99, 50, 54),
            (25, 20, 4),
            (2, 1, 1),
            (2, 2, 2),
            (9, 9, 9),
            (19, 19, 9),
            (1000, 1000, 999),
            (1000, 999, 998),
            (100000, 1, 1),
            (100000, 100000, 99999),
            (99999, 44444, 49999),
            (50000, 12345, 21107),
            (8, 8, 8),
            (77, 70, 72),
            (1000000000, 1, 1),
            (1000000000, 1000000000, 999999999),
        ],
    )
    def test_find_kth_number(self, n: int, k: int, expected: int):
        result = run_find_kth_number(Solution, n, k)
        assert_find_kth_number(result, expected)
