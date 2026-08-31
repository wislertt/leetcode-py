import pytest

from leetcode_py import logged_test

from .helpers import assert_get_intersection_node, run_get_intersection_node
from .solution import Solution


class TestIntersectionOfTwoLinkedLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "list_a, list_b, skip_a, skip_b",
        [
            ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3),
            ([1, 9, 1, 2, 4], [3, 2, 4], 3, 1),
            ([2, 6, 4], [1, 5], 3, 2),
            ([1], [1], 0, 0),
            ([1], [2], 1, 1),
            ([1, 2, 3], [4, 5, 6], 3, 3),
            ([1, 3, 5, 7, 9, 11], [2, 3, 5, 7, 9, 11], 0, 0),
            ([1, 2, 3], [1, 2, 3], 3, 3),
            ([2, 2, 4, 5], [7, 8, 4, 5], 2, 2),
            ([1, 2], [3, 4, 5, 2], 1, 3),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10], 9, 0),
            ([5], [1, 2, 3, 4, 5], 0, 4),
            ([3, 7, 4, 9], [8, 1, 6, 4, 9], 2, 3),
            ([9, 8, 7], [6, 9, 8, 7], 0, 1),
            ([100000], [100000, 100000], 0, 1),
        ],
    )
    def test_get_intersection_node(
        self, list_a: list[int], list_b: list[int], skip_a: int, skip_b: int
    ):
        result, expected = run_get_intersection_node(Solution, list_a, list_b, skip_a, skip_b)
        assert_get_intersection_node(result, expected)
