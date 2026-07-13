import pytest

from leetcode_py import logged_test

from .helpers import assert_most_booked, run_most_booked
from .solution import Solution


class TestTestMeetingRoomsIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, meetings, expected",
        [
            (2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0),
            (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1),
            (1, [[0, 5], [5, 10]], 0),
            (1, [[0, 5], [3, 10]], 0),
            (2, [[0, 5], [1, 2], [3, 4]], 1),
            (4, [[0, 3], [1, 2], [2, 3], [3, 4]], 0),
            (2, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]], 0),
            (3, [[1, 2], [2, 3], [3, 4], [4, 5]], 0),
            (2, [[0, 1], [2, 3], [4, 5], [6, 7]], 0),
            (3, [[1, 5], [2, 3], [4, 6]], 1),
            (1, [[0, 1]], 0),
            (2, [[0, 5], [5, 10]], 0),
            (3, [[0, 10], [1, 11], [2, 12], [3, 13]], 0),
            (2, [[1, 10], [2, 3], [4, 5], [6, 7]], 1),
        ],
    )
    def test_most_booked(self, n: int, meetings: list[list[int]], expected: int):
        result = run_most_booked(Solution, n, meetings)
        assert_most_booked(result, expected)
