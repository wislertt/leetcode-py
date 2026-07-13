import pytest

from leetcode_py import logged_test

from .helpers import assert_build_matrix, run_build_matrix
from .solution import Solution


class TestTestBuildAMatrixWithConditions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "k, row_conditions, col_conditions, valid",
        [
            (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], True),
            (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], False),
            (2, [], [], True),
            (3, [[1, 2], [2, 3]], [], True),
            (3, [], [[1, 2], [2, 3]], True),
            (2, [[1, 2], [2, 1]], [], False),
            (2, [], [[1, 2], [2, 1]], False),
            (4, [[1, 2], [3, 4]], [[2, 3]], True),
            (3, [[1, 2], [2, 3], [3, 1]], [], False),
            (5, [], [], True),
            (4, [[1, 2], [2, 3], [3, 4]], [[4, 3], [3, 2], [2, 1]], True),
            (2, [[1, 2]], [[1, 2]], True),
            (3, [[1, 2], [1, 3], [2, 3]], [[3, 2]], True),
            (3, [[1, 2]], [[2, 1], [1, 2]], False),
            (4, [[1, 2], [3, 4], [2, 3]], [[4, 1]], True),
        ],
    )
    def test_build_matrix(
        self, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]], valid: bool
    ):
        result = run_build_matrix(Solution, k, row_conditions, col_conditions)
        assert_build_matrix(result, k, row_conditions, col_conditions, valid)
