import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_read_binary_watch,
    assert_read_binary_watch_count,
    run_read_binary_watch,
)
from .solution import Solution


class TestBinaryWatch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "turned_on, expected",
        [
            (0, ["0:00"]),
            (1, ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]),
            (8, ["7:31", "7:47", "7:55", "7:59", "11:31", "11:47", "11:55", "11:59"]),
            (9, []),
            (10, []),
        ],
    )
    def test_read_binary_watch(self, turned_on: int, expected: list[str]):
        result = run_read_binary_watch(Solution, turned_on)
        assert_read_binary_watch(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "turned_on, expected_count",
        [
            (0, 1),
            (1, 10),
            (2, 44),
            (3, 112),
            (4, 181),
            (5, 190),
            (6, 126),
            (7, 48),
            (8, 8),
            (9, 0),
            (10, 0),
        ],
    )
    def test_read_binary_watch_count(self, turned_on: int, expected_count: int):
        result = run_read_binary_watch(Solution, turned_on)
        assert_read_binary_watch_count(result, turned_on, expected_count)
