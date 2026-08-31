import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min_difference, run_find_min_difference
from .solution import Solution


class TestMinimumTimeDifference:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "time_points, expected",
        [
            (["23:59", "00:00"], 1),
            (["00:00", "23:59", "00:00"], 0),
            (["00:00", "00:00"], 0),
            (["12:00", "12:01"], 1),
            (["06:00", "18:00"], 720),
            (["00:00", "12:00"], 720),
            (["05:31", "22:08", "00:35"], 147),
            (["23:58", "00:02"], 4),
            (["01:00", "23:00"], 120),
            (["10:59", "11:00", "11:01"], 1),
            (["00:01", "23:59"], 2),
            (["13:26", "04:24", "20:46", "09:52"], 214),
            (["22:29", "23:52", "01:15"], 83),
            (["07:30", "08:00", "07:45"], 15),
            (["18:00", "06:00", "12:00"], 360),
        ],
    )
    def test_find_min_difference(self, time_points: list[str], expected: int):
        result = run_find_min_difference(Solution, time_points)
        assert_find_min_difference(result, expected)
