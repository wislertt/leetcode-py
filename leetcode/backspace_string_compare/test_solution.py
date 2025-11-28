import pytest

from leetcode_py import logged_test

from .helpers import assert_backspace_compare, run_backspace_compare
from .solution import Solution


class TestBackspaceStringCompare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("s, t, expected", [])
    def test_backspace_compare(self, s: str, t: str, expected: bool):
        result = run_backspace_compare(Solution, s, t)
        assert_backspace_compare(result, expected)
