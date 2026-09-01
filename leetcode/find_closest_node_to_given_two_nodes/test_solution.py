import pytest

from leetcode_py import logged_test

from .helpers import assert_closest_meeting_node, run_closest_meeting_node
from .solution import Solution


class TestFindClosestNodeToGivenTwoNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges, node1, node2, expected",
        [
            ([2, 2, 3, -1], 0, 1, 2),
            ([1, 2, -1], 0, 2, 2),
            ([4, 4, 8, -1, 9, -1, -1, -1, -1, -1], 0, 1, 4),
            ([1, 2, -1], 0, 0, 0),
            ([1, -1], 0, 1, 1),
            ([-1, 0], 0, 1, 0),
            ([1, 2, 0], 0, 1, 1),
            ([-1, 3, -1, -1], 0, 1, -1),
            ([1, 2, 3, 1], 0, 2, 1),
            ([1, -1], 1, 0, 1),
            ([2, 2, -1, -1], 0, 2, 2),
            ([-1, -1], 0, 1, -1),
            ([4, 4, 8, -1, 9, -1, -1, -1, -1, -1], 1, 1, 1),
            ([-1, -1, 0, 4, 5, 1], 3, 1, 1),
            ([5, 4, -1, 4, 0, 4], 0, 0, 0),
            ([-1, 0], 1, 1, 1),
            ([1, 0], 0, 1, 0),
            ([2, 0, -1], 0, 0, 0),
        ],
    )
    def test_closest_meeting_node(self, edges: list[int], node1: int, node2: int, expected: int):
        result = run_closest_meeting_node(Solution, edges, node1, node2)
        assert_closest_meeting_node(result, expected)
