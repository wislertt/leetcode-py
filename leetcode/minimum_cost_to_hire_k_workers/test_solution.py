import pytest

from leetcode_py import logged_test

from .helpers import assert_mincost_to_hire_workers, run_mincost_to_hire_workers
from .solution import Solution


class TestMinimumCostToHireKWorkers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "quality, wage, k, expected",
        [
            ([10, 20, 5], [70, 50, 30], 2, 105.0),
            ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3, 30.66667),
            ([10, 20, 5], [70, 50, 30], 1, 30.0),
            ([4, 5], [8, 14], 2, 25.2),
            ([1], [10], 1, 10.0),
            ([2, 3, 4], [10, 10, 10], 2, 23.33333),
            ([14, 56, 32, 85, 11], [140, 560, 320, 850, 110], 3, 570.0),
            ([4, 1, 9, 8, 8, 5, 4, 18], [6, 38, 28, 3, 2, 6, 14, 15], 1, 2.0),
            ([7, 18, 14, 8, 15, 19, 9], [1, 49, 11, 45, 28, 22, 18], 2, 16.5),
            ([11, 4, 3, 13], [7, 23, 23, 39], 3, 138.0),
            ([2, 15, 18, 4, 13, 3, 18, 10, 20], [24, 37, 13, 46, 5, 3, 43, 15, 50], 5, 145.53333),
            ([8, 4, 13], [18, 30, 41], 2, 66.23077),
            ([12, 12, 7, 9], [45, 44, 42, 5], 2, 77.0),
            ([8, 6, 15, 13, 9, 18, 8], [44, 21, 50, 50, 4, 15, 3], 7, 423.5),
            ([13, 9, 3, 7, 19], [46, 21, 14, 42, 32], 4, 192.0),
        ],
    )
    def test_mincost_to_hire_workers(
        self, quality: list[int], wage: list[int], k: int, expected: float
    ):
        result = run_mincost_to_hire_workers(Solution, quality, wage, k)
        assert_mincost_to_hire_workers(result, expected)
