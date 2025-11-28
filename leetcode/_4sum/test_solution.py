from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_four_sum, run_four_sum
from .solution import Solution


class Test4sum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("nums, target, expected", [])
    def test_four_sum(self, nums: List[int], target: int, expected: List[List[int]]):
        result = run_four_sum(Solution, nums, target)
        assert_four_sum(result, expected)
