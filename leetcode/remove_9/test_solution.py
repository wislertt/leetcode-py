import pytest

from leetcode_py import logged_test

from .helpers import assert_new_integer, run_new_integer
from .solution import Solution


class TestRemove9:
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
            (7, 7),
            (8, 8),
            (9, 10),
            (10, 11),
            (11, 12),
            (80, 88),
            (81, 100),
            (89, 108),
            (100, 121),
            (889, 1187),
            (1000, 1331),
            (98765, 160428),
            (100000, 162151),
            (800000000, 2052305618),
        ],
    )
    def test_new_integer(self, n: int, expected: int):
        result = run_new_integer(Solution, n)
        assert_new_integer(result, expected)
