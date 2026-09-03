import pytest

from leetcode_py import logged_test

from .helpers import assert_find_kth_number, run_find_kth_number
from .solution import Solution


class TestKthSmallestNumberInMultiplicationTable:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, k, expected",
        [
            (3, 3, 5, 3),
            (2, 3, 6, 6),
            (1, 1, 1, 1),
            (1, 10, 5, 5),
            (10, 1, 7, 7),
            (2, 2, 1, 1),
            (2, 2, 4, 4),
            (3, 3, 1, 1),
            (3, 3, 9, 9),
            (5, 5, 13, 8),
            (4, 6, 10, 6),
            (6, 4, 18, 12),
            (12, 17, 100, 44),
            (20, 20, 400, 400),
            (20, 1, 20, 20),
            (7, 11, 42, 21),
            (13, 19, 247, 247),
            (9, 3, 27, 27),
            (16, 14, 1, 1),
            (18, 15, 269, 255),
            (15, 4, 2, 2),
            (14, 6, 5, 3),
            (6, 18, 4, 3),
            (20, 5, 92, 72),
            (14, 12, 40, 15),
            (14, 5, 61, 44),
            (4, 18, 27, 14),
            (17, 20, 239, 126),
            (15, 14, 32, 12),
            (17, 13, 160, 88),
        ],
    )
    def test_find_kth_number(self, m: int, n: int, k: int, expected: int):
        result = run_find_kth_number(Solution, m, n, k)
        assert_find_kth_number(result, expected)
