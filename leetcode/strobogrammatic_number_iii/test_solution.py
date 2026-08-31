import pytest

from leetcode_py import logged_test

from .helpers import assert_strobogrammatic_in_range, run_strobogrammatic_in_range
from .solution import Solution


class TestStrobogrammaticNumberIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "low, high, expected",
        [
            ("50", "100", 3),
            ("0", "0", 1),
            ("0", "100000000000000", 124999),
            ("100", "100", 0),
            ("1", "1", 1),
            ("10", "100", 4),
            ("0", "9", 3),
            ("0", "99", 7),
            ("50", "88", 2),
            ("100", "999", 12),
            ("999", "1001", 1),
            ("0", "8", 3),
            ("69", "96", 3),
            ("1000", "9999", 20),
            ("0", "1000", 19),
            ("1000000000000", "999999999999999", 287500),
        ],
    )
    def test_strobogrammatic_in_range(self, low: str, high: str, expected: int):
        result = run_strobogrammatic_in_range(Solution, low, high)
        assert_strobogrammatic_in_range(result, expected)
