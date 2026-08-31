import pytest

from leetcode_py import logged_test

from .helpers import assert_is_strobogrammatic, run_is_strobogrammatic
from .solution import Solution


class TestStrobogrammaticNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            ("69", True),
            ("88", True),
            ("962", False),
            ("0", True),
            ("1", True),
            ("8", True),
            ("2", False),
            ("5", False),
            ("6", False),
            ("9", False),
            ("11", True),
            ("96", True),
            ("619", True),
            ("689", True),
            ("1001", True),
            ("25", False),
            ("818", True),
            ("9006", True),
        ],
    )
    def test_is_strobogrammatic(self, num: str, expected: bool):
        result = run_is_strobogrammatic(Solution, num)
        assert_is_strobogrammatic(result, expected)
