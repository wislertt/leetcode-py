import pytest

from leetcode_py import logged_test

from .helpers import assert_distance_k, run_distance_k
from .solution import Solution


class TestAllNodesDistanceKInBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target, k, expected",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2, [7, 4, 1]),
            ([1], 1, 3, []),
            ([1], 1, 0, [1]),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 0, [5]),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 3, 1, [5, 1]),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 3, 2, [6, 2, 0, 8]),
            ([1, 2, 3, 4, 5], 2, 2, [3]),
            ([1, 2, 3, 4, 5], 4, 1, [2]),
            ([1, 2, 3, 4, 5], 4, 2, [1, 5]),
            ([1, 2], 1, 1, [2]),
            ([1, 2], 2, 1, [1]),
            ([1, 2, 3], 2, 2, [3]),
            ([1, None, 2, None, 3], 1, 1, [2]),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 3, [3, 6]),
            ([1, 2, 3, 4, 5, 6, 7], 3, 3, [4, 5]),
        ],
    )
    def test_distance_k(
        self, root_list: list[int | None], target: int, k: int, expected: list[int]
    ):
        result = run_distance_k(Solution, root_list, target, k)
        assert_distance_k(result, expected)
