from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_generate, run_generate
from .solution import Solution


class TestPascalsTriangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("numRows, expected", [(5, 1)])
    def test_generate(self, numRows: int, expected: List[List[int]]):
        result = run_generate(Solution, numRows)
        assert_generate(result, expected)
