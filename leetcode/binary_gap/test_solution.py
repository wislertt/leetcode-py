import pytest

from leetcode_py import logged_test

from .helpers import assert_binary_gap, run_binary_gap
from .solution import Solution


class TestBinaryGap:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (22, 2),
            (8, 0),
            (5, 2),
            (1, 0),
            (2, 0),
            (3, 1),
            (6, 1),
            (9, 3),
            (10, 2),
            (15, 1),
            (17, 4),
            (21, 2),
            (33, 5),
            (511, 1),
            (512, 0),
            (1000000000, 3),
            (999999999, 3),
            (431306783, 7),
            (157882799, 4),
            (353249164, 5),
        ],
    )
    def test_binary_gap(self, n: int, expected: int):
        result = run_binary_gap(Solution, n)
        assert_binary_gap(result, expected)
