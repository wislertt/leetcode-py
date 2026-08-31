import pytest

from leetcode_py import logged_test

from .helpers import assert_is_ugly, run_is_ugly
from .solution import Solution


class TestUglyNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (6, True),
            (1, True),
            (14, False),
            (2, True),
            (3, True),
            (5, True),
            (4, True),
            (8, True),
            (15, True),
            (30, True),
            (60, True),
            (0, False),
            (-1, False),
            (-6, False),
            (-2147483648, False),
            (7, False),
            (49, False),
            (2147483647, False),
            (1162261467, True),
            (1220703125, True),
        ],
    )
    def test_is_ugly(self, n: int, expected: bool):
        result = run_is_ugly(Solution, n)
        assert_is_ugly(result, expected)
