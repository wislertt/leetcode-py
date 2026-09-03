import pytest

from leetcode_py import logged_test

from .helpers import assert_has_alternating_bits, run_has_alternating_bits
from .solution import Solution


class TestBinaryNumberWithAlternatingBits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (5, True),
            (1, True),
            (2, True),
            (10, True),
            (42, True),
            (85, True),
            (170, True),
            (1431655765, True),
            (715827882, True),
            (2147483647, False),
            (7, False),
            (11, False),
            (3, False),
            (4, False),
            (6, False),
            (12, False),
            (2147483645, False),
            (2147483646, False),
        ],
    )
    def test_has_alternating_bits(self, n: int, expected: bool):
        result = run_has_alternating_bits(Solution, n)
        assert_has_alternating_bits(result, expected)
