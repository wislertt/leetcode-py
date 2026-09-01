import pytest

from leetcode_py import logged_test

from .helpers import assert_nodes_between_critical_points, run_nodes_between_critical_points
from .solution import Solution


class TestFindTheMinimumAndMaximumNumberOfNodesBetweenCriticalPoints:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([3, 1], [-1, -1]),
            ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
            ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
            ([1, 2], [-1, -1]),
            ([2, 1], [-1, -1]),
            ([1, 2, 1], [-1, -1]),
            ([2, 1, 2], [-1, -1]),
            ([1, 3, 2], [-1, -1]),
            ([5, 5, 5], [-1, -1]),
            ([1, 2, 3, 4, 5], [-1, -1]),
            ([5, 4, 3, 2, 1], [-1, -1]),
            ([1, 2, 2, 1], [-1, -1]),
            ([1, 2, 1, 2, 1, 2, 1], [1, 4]),
            ([1, 5, 1, 5, 1, 5, 1, 5, 1], [1, 6]),
            ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 8]),
            ([2, 2, 2, 3, 3, 3, 2, 2, 2], [-1, -1]),
            ([4, 2, 6, 1, 7, 3, 8, 2, 9, 1], [1, 7]),
            ([1, 1, 4, 2], [-1, -1]),
            ([2, 2, 5, 4, 3, 5, 4], [1, 3]),
            ([2, 4, 1, 5, 3, 1, 4, 3, 1], [1, 5]),
            ([2, 5, 3, 1, 2, 4, 5], [2, 2]),
            ([4, 3, 3, 2, 4, 1, 2, 3, 1, 3, 4], [1, 5]),
        ],
    )
    def test_nodes_between_critical_points(self, head_list: list[int], expected: list[int]):
        result = run_nodes_between_critical_points(Solution, head_list)
        assert_nodes_between_critical_points(result, expected)
