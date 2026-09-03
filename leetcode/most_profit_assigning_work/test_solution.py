import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit_assignment, run_max_profit_assignment
from .solution import Solution


class TestMostProfitAssigningWork:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "difficulty, profit, worker, expected",
        [
            ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
            ([85, 47, 57], [24, 66, 99], [40, 25, 25], 0),
            ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [10, 10, 10, 10], 200),
            ([5], [10], [5], 10),
            ([5], [10], [4], 0),
            ([1], [1], [1, 1, 1, 1], 4),
            ([3, 1, 2], [5, 4, 3], [3, 2, 1], 13),
            ([10, 10, 10], [1, 2, 3], [10], 3),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 25),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], 25),
            ([7, 7, 7], [1, 5, 3], [7, 7], 10),
            ([4, 4, 4], [9, 1, 5], [3, 4, 5], 18),
            ([68, 35, 52, 47, 82], [67, 27, 63, 18, 90], [40, 25, 52, 82], 180),
            ([13, 37, 58], [24, 66, 99], [40, 25, 25], 114),
            ([1, 1, 1], [1, 2, 3], [1], 3),
            ([23, 44, 66, 12], [30, 60, 90, 10], [25, 45, 67, 13, 100], 280),
            ([9, 16, 12, 5, 7], [20, 1, 29, 23, 19], [8, 9], 46),
            ([8, 5, 5], [21, 17, 12], [11, 17, 6], 59),
            ([3, 15, 7], [21, 5, 18], [9, 16, 8, 6], 84),
            ([15, 16, 17, 20, 17], [25, 10, 13, 14, 9], [23], 25),
        ],
    )
    def test_max_profit_assignment(
        self, difficulty: list[int], profit: list[int], worker: list[int], expected: int
    ):
        result = run_max_profit_assignment(Solution, difficulty, profit, worker)
        assert_max_profit_assignment(result, expected)
