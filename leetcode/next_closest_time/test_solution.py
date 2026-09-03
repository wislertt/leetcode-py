import pytest

from leetcode_py import logged_test

from .helpers import assert_next_closest_time, run_next_closest_time
from .solution import Solution


class TestNextClosestTime:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "time, expected",
        [
            ("19:34", "19:39"),
            ("23:59", "22:22"),
            ("00:00", "00:00"),
            ("11:11", "11:11"),
            ("13:55", "15:11"),
            ("09:59", "00:00"),
            ("10:00", "10:01"),
            ("15:47", "15:51"),
            ("20:38", "22:00"),
            ("06:06", "00:00"),
            ("12:34", "12:41"),
            ("17:59", "19:11"),
            ("21:11", "21:12"),
            ("23:53", "23:55"),
            ("05:05", "05:50"),
            ("18:42", "18:44"),
            ("08:15", "08:18"),
            ("14:02", "14:04"),
        ],
    )
    def test_next_closest_time(self, time: str, expected: str):
        result = run_next_closest_time(Solution, time)
        assert_next_closest_time(result, expected)
