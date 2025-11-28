from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum_closest, run_three_sum_closest
from .solution import Solution


class Test3sumClosest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("nums, target, expected", [])
    def test_three_sum_closest(self, nums: List[int], target: int, expected: int):
        result = run_three_sum_closest(Solution, nums, target)
        assert_three_sum_closest(result, expected)
