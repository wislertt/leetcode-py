import pytest

from leetcode_py import logged_test

from .helpers import assert_assign_bikes, run_assign_bikes
from .solution import Solution


class TestCampusBikes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "workers, bikes, expected",
        [
            ([[0, 0], [2, 1]], [[1, 2], [3, 3]], [1, 0]),
            ([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]], [0, 2, 1]),
            ([[0, 0]], [[0, 1]], [0]),
            ([[0, 0], [0, 2]], [[0, 1], [1, 0]], [0, 1]),
            ([[1, 3], [3, 1]], [[1, 1], [3, 3]], [0, 1]),
            ([[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 1], [1, 1], [2, 1], [3, 1]], [0, 1, 2, 3]),
            (
                [[240, 446], [725, 504], [503, 318], [415, 224], [818, 477]],
                [
                    [146, 785],
                    [185, 244],
                    [592, 834],
                    [252, 698],
                    [318, 647],
                    [166, 905],
                    [573, 506],
                    [118, 801],
                    [858, 542],
                    [698, 733],
                ],
                [3, 6, 4, 1, 8],
            ),
            ([[0, 0], [1, 1]], [[0, 1], [1, 0]], [0, 1]),
            ([[5, 5]], [[6, 6], [4, 4], [7, 3]], [0]),
            (
                [[0, 0], [999, 999], [500, 500]],
                [[0, 1], [998, 998], [501, 500], [250, 250]],
                [0, 1, 2],
            ),
            ([[0, 0], [3, 3], [1, 1]], [[1, 1], [4, 4], [0, 1]], [2, 1, 0]),
        ],
    )
    def test_assign_bikes(
        self, workers: list[list[int]], bikes: list[list[int]], expected: list[int]
    ):
        result = run_assign_bikes(Solution, workers, bikes)
        assert_assign_bikes(result, expected)
