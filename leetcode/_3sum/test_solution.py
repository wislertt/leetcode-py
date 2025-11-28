from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum, run_three_sum
from .solution import Solution


class Test3sum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("nums, expected", [])
    def test_three_sum(self, nums: List[int], expected: List[List[int]]):
        result = run_three_sum(Solution, nums)
        assert_three_sum(result, expected)
