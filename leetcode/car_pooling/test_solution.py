import pytest

from leetcode_py import logged_test

from .helpers import assert_car_pooling, run_car_pooling
from .solution import Solution


class TestCarPooling:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "trips, capacity, expected",
        [
            ([[2, 1, 5], [3, 3, 7]], 4, False),
            ([[2, 1, 5], [3, 3, 7]], 5, True),
            ([[2, 1, 5], [3, 5, 7]], 3, True),
            ([[2, 1, 5], [3, 5, 7]], 2, False),
            ([[7, 5, 6], [6, 4, 7], [5, 3, 4]], 16, True),
            ([[7, 5, 6], [6, 4, 7], [5, 3, 4]], 12, False),
            ([[4, 1, 5], [4, 2, 6]], 8, True),
            ([[4, 1, 5], [4, 2, 6]], 7, False),
            ([[1, 1, 2]], 1, True),
            ([[2, 1, 2], [2, 2, 3], [2, 3, 4]], 2, True),
            ([[3, 1, 3], [3, 2, 4]], 6, True),
            ([[3, 1, 3], [3, 2, 4]], 5, False),
            ([[10, 0, 5], [5, 1, 3]], 15, True),
            ([[10, 0, 5], [5, 1, 3]], 14, False),
            ([[100, 0, 1000]], 100, True),
            ([[100, 0, 1000]], 99, False),
        ],
    )
    def test_car_pooling(self, trips: list[list[int]], capacity: int, expected: bool):
        result = run_car_pooling(Solution, trips, capacity)
        assert_car_pooling(result, expected)
