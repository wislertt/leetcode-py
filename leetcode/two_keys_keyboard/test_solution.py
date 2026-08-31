import pytest

from leetcode_py import logged_test

from .helpers import assert_min_steps, run_min_steps
from .solution import Solution


class TestTwoKeysKeyboard:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (3, 3),
            (1, 0),
            (2, 2),
            (4, 4),
            (6, 5),
            (12, 7),
            (30, 10),
            (100, 14),
            (128, 14),
            (729, 18),
            (999, 46),
            (1000, 21),
            (971, 971),
            (5, 5),
        ],
    )
    def test_min_steps(self, n: int, expected: int):
        result = run_min_steps(Solution, n)
        assert_min_steps(result, expected)
