import pytest

from leetcode_py import logged_test

from .helpers import assert_find_judge, run_find_judge
from .solution import Solution


class TestFindTheTownJudge:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, trust, expected",
        [
            (2, [[1, 2]], 2),
            (3, [[1, 3], [2, 3]], 3),
            (3, [[1, 3], [2, 3], [3, 1]], -1),
            (1, [], 1),
            (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
            (3, [[1, 2], [2, 3]], -1),
            (4, [[1, 2], [1, 3], [2, 3], [4, 3]], 3),
            (3, [], -1),
            (4, [[1, 2], [2, 3], [3, 4], [4, 1]], -1),
            (2, [], -1),
            (5, [[1, 4], [2, 4], [3, 4], [5, 4]], 4),
            (2, [[1, 2], [2, 1]], -1),
            (4, [[1, 3], [2, 3], [4, 3], [3, 2]], -1),
            (3, [[1, 2], [1, 3]], -1),
            (6, [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5]], 5),
            (3, [[1, 3], [2, 3], [1, 2]], 3),
            (4, [[1, 2], [3, 2], [4, 2], [2, 1]], -1),
            (2, [[2, 1]], 1),
        ],
    )
    def test_find_judge(self, n: int, trust: list[list[int]], expected: int):
        result = run_find_judge(Solution, n, trust)
        assert_find_judge(result, expected)
