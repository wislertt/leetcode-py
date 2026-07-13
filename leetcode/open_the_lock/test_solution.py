import pytest

from leetcode_py import logged_test

from .helpers import assert_open_lock, run_open_lock
from .solution import Solution


class TestOpenTheLock:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "deadends, target, expected",
        [
            (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
            (["8888"], "0009", 1),
            (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1),
            (["0000"], "8888", -1),
            ([], "0000", 0),
            ([], "0001", 1),
            ([], "0009", 1),
            ([], "0019", 2),
            (["0001", "0009", "0010", "0090", "0100", "0900", "1000", "9000"], "1111", -1),
            ([], "9999", 4),
            ([], "0202", 4),
            (["1000", "0100", "0010", "0001"], "2000", 4),
            (["1234", "5678"], "4321", 10),
            ([], "1111", 4),
        ],
    )
    def test_open_lock(self, deadends: list[str], target: str, expected: int):
        result = run_open_lock(Solution, deadends, target)
        assert_open_lock(result, expected)
