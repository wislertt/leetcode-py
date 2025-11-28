from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_add_to_array_form, run_add_to_array_form
from .solution import Solution


class TestAddToArrayFormOfInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("num, k, expected", [])
    def test_add_to_array_form(self, num: List[int], k: int, expected: List[int]):
        result = run_add_to_array_form(Solution, num, k)
        assert_add_to_array_form(result, expected)
