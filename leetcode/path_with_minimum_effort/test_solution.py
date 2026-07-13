import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_effort_path, run_minimum_effort_path
from .solution import Solution


class TestTestPathWithMinimumEffort:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
            ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
            (
                [
                    [1, 2, 1, 1, 1],
                    [1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1],
                    [1, 1, 1, 2, 1],
                ],
                0,
            ),
            ([[1]], 0),
            ([[5]], 0),
            ([[1, 2, 3]], 1),
            ([[1], [2], [3]], 1),
            ([[1, 10], [2, 3]], 1),
            ([[1, 2, 3], [4, 5, 6]], 3),
            ([[10, 8, 10], [8, 0, 8]], 2),
            ([[1, 100], [2, 3]], 1),
            ([[1, 2], [4, 3]], 1),
            ([[1, 2, 2], [3, 8, 2]], 1),
            ([[1, 2, 1], [6, 1, 1], [1, 1, 1]], 1),
            ([[1, 1, 1], [10, 10, 1]], 0),
        ],
    )
    def test_minimum_effort_path(self, heights: list[list[int]], expected: int):
        result = run_minimum_effort_path(Solution, heights)
        assert_minimum_effort_path(result, expected)
