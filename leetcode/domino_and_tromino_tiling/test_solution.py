import pytest

from leetcode_py import logged_test

from .helpers import assert_num_tilings, run_num_tilings
from .solution import Solution


class TestDominoAndTrominoTiling:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 5),
            (4, 11),
            (5, 24),
            (6, 53),
            (7, 117),
            (8, 258),
            (9, 569),
            (10, 1255),
            (11, 2768),
            (12, 6105),
            (15, 65501),
            (20, 3418626),
            (30, 312342182),
            (50, 451995198),
            (1000, 979232805),
        ],
    )
    def test_num_tilings(self, n: int, expected: int):
        result = run_num_tilings(Solution, n)
        assert_num_tilings(result, expected)
