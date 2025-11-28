import pytest

from leetcode_py import logged_test

from .helpers import assert_add_binary, run_add_binary
from .solution import Solution


class TestAddBinary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("a, b, expected", [])
    def test_add_binary(self, a: str, b: str, expected: str):
        result = run_add_binary(Solution, a, b)
        assert_add_binary(result, expected)
