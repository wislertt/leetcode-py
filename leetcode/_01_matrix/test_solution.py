from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_update_matrix, run_update_matrix
from .solution import Solution


class Test01Matrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat, expected",
        [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [1, 1, 1]])],
    )
    def test_update_matrix(self, mat: List[List[int]], expected: List[List[int]]):
        result = run_update_matrix(Solution, mat)
        assert_update_matrix(result, expected)
