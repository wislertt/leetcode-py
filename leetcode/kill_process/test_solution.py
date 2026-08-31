import pytest

from leetcode_py import logged_test

from .helpers import assert_kill_process, run_kill_process
from .solution import Solution


class TestKillProcess:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pid, ppid, kill, expected",
        [
            ([1, 3, 10, 5], [3, 0, 5, 3], 5, [5, 10]),
            ([1], [0], 1, [1]),
            ([1, 2, 3], [0, 1, 1], 1, [1, 2, 3]),
            ([1, 2, 3], [0, 1, 1], 2, [2]),
            ([1, 2, 3, 4, 5, 6], [0, 1, 1, 2, 2, 3], 1, [1, 2, 3, 4, 5, 6]),
            ([1, 2, 3, 4, 5, 6], [0, 1, 1, 2, 2, 3], 3, [3, 6]),
            ([2, 4, 6, 8], [0, 2, 2, 6], 6, [6, 8]),
            ([5, 23, 39, 47, 19, 6, 33, 48, 26], [0, 5, 5, 5, 5, 47, 6, 23, 6], 23, [23, 48]),
            ([28, 27, 44, 37], [0, 28, 27, 27], 44, [44]),
            (
                [10, 20, 48, 38, 42, 31, 26, 40, 7],
                [0, 10, 10, 20, 20, 48, 10, 42, 26],
                48,
                [31, 48],
            ),
            ([1, 49, 2, 26, 27], [0, 1, 49, 1, 2], 1, [1, 2, 26, 27, 49]),
            ([1, 41], [0, 1], 1, [1, 41]),
        ],
    )
    def test_kill_process(self, pid: list[int], ppid: list[int], kill: int, expected: list[int]):
        result = run_kill_process(Solution, pid, ppid, kill)
        assert_kill_process(result, expected)
