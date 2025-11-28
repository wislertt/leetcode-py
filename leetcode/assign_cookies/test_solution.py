from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_find_content_children, run_find_content_children
from .solution import Solution


class TestAssignCookies:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("g, s, expected", [])
    def test_find_content_children(self, g: List[int], s: List[int], expected: int):
        result = run_find_content_children(Solution, g, s)
        assert_find_content_children(result, expected)
