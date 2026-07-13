import pytest

from leetcode_py import logged_test

from .helpers import assert_candy, run_candy
from .solution import Solution


class TestTestCandy:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, ratings, expected",
        [
            (Solution, [1, 0, 2], 5),
            (Solution, [1, 2, 2], 4),
            (Solution, [1], 1),
            (Solution, [0], 1),
            (Solution, [1, 2], 3),
            (Solution, [2, 1], 3),
            (Solution, [1, 2, 3], 6),
            (Solution, [3, 2, 1], 6),
            (Solution, [1, 3, 2, 1], 7),
            (Solution, [1, 2, 3, 4, 5], 15),
            (Solution, [5, 4, 3, 2, 1], 15),
            (Solution, [1, 2, 1, 2, 1], 7),
            (Solution, [2, 2, 2, 2], 4),
            (Solution, [1, 0, 1, 0, 1], 8),
            (Solution, [5, 5, 5], 3),
            (Solution, [1, 2, 2, 1], 6),
            (Solution, [3, 2, 3], 5),
            (Solution, [1, 3, 4, 5, 2], 11),
        ],
    )
    def test_candy(self, solution_class, ratings: list[int], expected: int):
        result = run_candy(solution_class, ratings)
        assert_candy(result, expected)
