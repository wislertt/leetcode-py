import pytest

from leetcode_py import logged_test

from .helpers import assert_exclusive_time, run_exclusive_time
from .solution import Solution


class TestExclusiveTimeOfFunctions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, logs, expected",
        [
            (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
            (1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"], [8]),
            (2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"], [7, 1]),
            (1, ["0:start:0", "0:end:1"], [2]),
            (2, ["0:start:0", "0:end:0", "1:start:1", "1:end:1"], [1, 1]),
            (
                3,
                ["0:start:0", "1:start:3", "1:end:3", "2:start:5", "2:end:6", "0:end:8"],
                [6, 1, 2],
            ),
            (2, ["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"], [6, 0]),
            (2, ["0:start:0", "1:start:1", "0:start:2", "0:end:2", "1:end:4", "0:end:5"], [3, 3]),
            (1, ["0:start:0", "0:start:1", "0:end:1", "0:end:2", "0:start:3", "0:end:3"], [4]),
            (4, ["3:start:0", "3:end:0", "0:start:2", "0:end:4"], [3, 0, 0, 1]),
            (
                3,
                ["2:start:999999995", "2:end:999999998", "0:start:1000000000", "0:end:1000000000"],
                [1, 0, 4],
            ),
            (
                2,
                ["1:start:2", "1:start:4", "1:start:11", "1:end:12", "1:end:13", "1:end:20"],
                [0, 19],
            ),
            (8, ["5:start:2", "5:end:4"], [0, 0, 0, 0, 0, 3, 0, 0]),
            (2, ["1:start:1", "0:start:2", "0:end:3", "1:end:6"], [2, 4]),
            (8, ["6:start:6", "6:end:7"], [0, 0, 0, 0, 0, 0, 2, 0]),
            (2, ["1:start:101", "1:end:108"], [0, 8]),
        ],
    )
    def test_exclusive_time(self, n: int, logs: list[str], expected: list[int]):
        result = run_exclusive_time(Solution, n, logs)
        assert_exclusive_time(result, expected)
