import pytest

from leetcode_py import logged_test

from .helpers import assert_magical_string, run_magical_string
from .solution import Solution


class TestMagicalString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 3),
            (6, 3),
            (7, 4),
            (8, 4),
            (9, 4),
            (10, 5),
            (11, 5),
            (12, 5),
            (13, 6),
            (14, 7),
            (15, 7),
            (16, 8),
            (17, 9),
            (18, 9),
            (19, 9),
            (20, 10),
            (21, 10),
            (22, 11),
            (23, 12),
            (24, 12),
            (30, 15),
            (50, 25),
            (100, 49),
            (499, 248),
            (1000, 502),
            (4999, 2500),
            (10000, 4996),
            (99999, 49972),
            (100000, 49972),
        ],
    )
    def test_magical_string(self, n: int, expected: int):
        result = run_magical_string(Solution, n)
        assert_magical_string(result, expected)
