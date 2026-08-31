import pytest

from leetcode_py import logged_test

from .helpers import assert_num_ways, run_num_ways
from .solution import Solution


class TestNumberOfWaysToStayInTheSamePlaceAfterSomeSteps:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "steps, arr_len, expected",
        [
            (3, 2, 4),
            (2, 4, 2),
            (4, 2, 8),
            (1, 1, 1),
            (1, 2, 1),
            (1, 1000000, 1),
            (2, 1, 1),
            (3, 3, 4),
            (10, 3, 1682),
            (5, 6, 21),
            (27, 7, 127784505),
            (430, 92939, 525833932),
            (47, 200, 318671228),
            (50, 50, 852867642),
            (100, 1000000, 345787718),
            (500, 500, 374847123),
        ],
    )
    def test_num_ways(self, steps: int, arr_len: int, expected: int):
        result = run_num_ways(Solution, steps, arr_len)
        assert_num_ways(result, expected)
