import pytest

from leetcode_py import logged_test

from .helpers import assert_cal_points, run_cal_points
from .solution import Solution


class TestBaseballGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "operations, expected",
        [
            (["5", "2", "C", "D", "+"], 30),
            (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
            (["1", "C"], 0),
            (["5"], 5),
            (["1", "2", "3"], 6),
            (["1", "2", "+", "+"], 11),
            (["1", "D", "D"], 7),
            (["-1", "D", "+"], -6),
            (["10", "20", "C", "C", "5"], 5),
            (["1", "2", "3", "C", "C", "C"], 0),
            (["100", "D", "+", "C"], 300),
            (["0", "0", "0", "+"], 0),
            (["-5", "D"], -15),
            (["1", "2", "D", "+", "C"], 7),
        ],
    )
    def test_cal_points(self, operations: list[str], expected: int):
        result = run_cal_points(Solution, operations)
        assert_cal_points(result, expected)
