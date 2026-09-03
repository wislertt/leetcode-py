import pytest

from leetcode_py import logged_test

from .helpers import assert_can_visit_all_rooms, run_can_visit_all_rooms
from .solution import Solution


class TestKeysAndRooms:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rooms, expected",
        [
            ([[1], [2], [3], []], True),
            ([[1, 3], [3, 0, 1], [2], [0]], False),
            ([[1], [0], [1], [2]], False),
            ([[1, 2, 3], [], [], []], True),
            ([[1], [0, 2], []], True),
            ([[2], [3], [0], [1]], False),
            ([[1], [1], [1], [3]], False),
            ([[1, 2], [0], [0]], True),
            ([[1], [2], [3], [0]], True),
            ([[1], [0, 3], [3], [2]], True),
            ([[2], [2], [1], []], False),
            ([[1, 2], [2], [1], []], False),
            ([[1], [0]], True),
            ([[1], [2], [0]], True),
            ([[1], [1], [2]], False),
            ([[1, 4, 5], [5, 3, 4], [5, 4], [], [3, 1, 5], [2, 0]], True),
            ([[0], []], False),
            ([[], [1, 5, 3], [2, 3, 5], [], [], [3]], False),
            ([[3, 2], [], [3, 2, 0], []], False),
            ([[2, 4, 3], [5], [], [0, 3, 5], [1, 4], []], True),
            ([[2, 4], [1], [3, 1, 4], [1, 4], [1]], True),
            ([[3, 0, 2], [], [2], []], False),
            ([[4, 0], [], [], [], [4], [3, 2, 5]], False),
        ],
    )
    def test_can_visit_all_rooms(self, rooms: list[list[int]], expected: bool):
        result = run_can_visit_all_rooms(Solution, rooms)
        assert_can_visit_all_rooms(result, expected)
