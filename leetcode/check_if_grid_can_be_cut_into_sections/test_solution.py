import pytest

from leetcode_py import logged_test

from .helpers import assert_check_valid_cuts, run_check_valid_cuts
from .solution import Solution


class TestCheckIfGridCanBeCutIntoSections:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, rectangles, expected",
        [
            (5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]], True),
            (4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]], True),
            (4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]], False),
            (3, [[0, 0, 1, 1], [1, 0, 2, 1], [0, 1, 1, 2]], False),
            (6, [[0, 0, 2, 6], [2, 0, 4, 6], [4, 0, 6, 6]], True),
            (7, [[0, 0, 7, 2], [1, 2, 6, 5], [0, 5, 7, 7], [0, 2, 1, 5], [6, 2, 7, 5]], True),
            (3, [[0, 0, 3, 1], [0, 1, 3, 2], [0, 2, 3, 3]], True),
            (5, [[0, 0, 5, 1], [0, 1, 2, 4], [2, 1, 5, 4], [0, 4, 5, 5]], True),
            (5, [[2, 0, 4, 1], [0, 0, 1, 1], [4, 0, 5, 1], [0, 1, 5, 5], [1, 0, 2, 1]], False),
            (5, [[4, 0, 5, 5], [0, 0, 3, 4], [0, 4, 3, 5], [3, 0, 4, 1], [3, 1, 4, 5]], True),
            (3, [[0, 2, 1, 3], [0, 1, 1, 2], [0, 0, 1, 1], [1, 0, 3, 3]], False),
            (3, [[0, 1, 1, 3], [0, 0, 3, 1], [1, 1, 3, 3]], False),
            (6, [[0, 0, 3, 5], [3, 0, 6, 6], [0, 5, 3, 6]], False),
            (8, [[1, 0, 8, 8], [0, 4, 1, 6], [0, 0, 1, 4], [0, 6, 1, 8]], False),
            (3, [[1, 1, 3, 3], [1, 0, 3, 1], [0, 0, 1, 3]], False),
            (7, [[2, 6, 7, 7], [2, 0, 7, 6], [0, 0, 2, 7]], False),
            (9, [[0, 0, 3, 1], [3, 0, 4, 1], [8, 0, 9, 1], [4, 0, 8, 1], [0, 1, 9, 9]], False),
            (5, [[4, 4, 5, 5], [4, 0, 5, 4], [0, 0, 4, 5]], False),
        ],
    )
    def test_check_valid_cuts(self, n: int, rectangles: list[list[int]], expected: bool):
        result = run_check_valid_cuts(Solution, n, rectangles)
        assert_check_valid_cuts(result, expected)
