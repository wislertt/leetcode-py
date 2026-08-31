import pytest

from leetcode_py import logged_test

from .helpers import assert_find_derangement, run_find_derangement
from .solution import Solution


class TestFindTheDerangementOfAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 9),
            (5, 44),
            (6, 265),
            (7, 1854),
            (8, 14833),
            (9, 133496),
            (10, 1334961),
            (100, 944828409),
            (1000000, 102701088),
        ],
    )
    def test_find_derangement(self, n: int, expected: int):
        result = run_find_derangement(Solution, n)
        assert_find_derangement(result, expected)
