import pytest

from leetcode_py import logged_test

from .helpers import assert_count_days, run_count_days
from .solution import Solution


class TestCountDaysWithoutMeetings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "days, meetings, expected",
        [
            (10, [[5, 7], [1, 3], [9, 10]], 2),
            (5, [[2, 4], [1, 3]], 1),
            (6, [[1, 6]], 0),
            (1, [[1, 1]], 0),
            (2, [[1, 1]], 1),
            (10, [[1, 10]], 0),
            (1000000000, [[1, 1]], 999999999),
            (8, [[2, 3], [6, 8]], 3),
            (4, [[1, 2], [3, 4]], 0),
            (7, [[4, 5]], 5),
            (9, [[1, 2], [8, 9]], 5),
            (3, [[1, 3], [1, 3], [1, 3]], 0),
            (10, [[3, 3]], 9),
            (5, [[1, 1], [3, 3], [5, 5]], 2),
            (2, [[2, 2], [1, 1]], 0),
            (1000000000, [[999999999, 1000000000]], 999999998),
            (18, [[3, 3], [18, 18], [9, 16], [7, 12]], 6),
            (11, [[4, 9], [3, 3]], 4),
            (8, [[5, 8], [3, 8], [1, 8]], 0),
            (7, [[3, 5], [7, 7], [2, 7]], 1),
            (11, [[11, 11]], 10),
            (12, [[1, 6]], 6),
        ],
    )
    def test_count_days(self, days: int, meetings: list[list[int]], expected: int):
        result = run_count_days(Solution, days, meetings)
        assert_count_days(result, expected)
