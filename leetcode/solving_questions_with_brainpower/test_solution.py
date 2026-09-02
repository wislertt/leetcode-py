import pytest

from leetcode_py import logged_test

from .helpers import assert_most_points, run_most_points
from .solution import Solution


class TestSolvingQuestionsWithBrainpower:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "questions, expected",
        [
            ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
            ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
            ([[3, 1]], 3),
            ([[10, 100]], 10),
            ([[1, 1], [1, 1]], 1),
            ([[100, 1], [1, 100]], 100),
            ([[1, 1], [100, 1]], 100),
            ([[5, 5], [5, 5], [5, 5], [5, 5]], 5),
            ([[2, 1], [3, 1], [4, 1]], 6),
            ([[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]], 79),
            ([[21, 5], [92, 3], [74, 2], [39, 23], [22, 7], [100, 2]], 192),
            ([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]], 12),
            ([[48, 3], [45, 3], [92, 1], [55, 3], [2, 1], [22, 2], [12, 2], [27, 3], [78, 1]], 192),
            ([[91, 4], [85, 2], [58, 1]], 91),
            ([[50, 2], [65, 1], [81, 4], [7, 2], [93, 1]], 158),
            ([[55, 1]], 55),
        ],
    )
    def test_most_points(self, questions: list[list[int]], expected: int):
        result = run_most_points(Solution, questions)
        assert_most_points(result, expected)
