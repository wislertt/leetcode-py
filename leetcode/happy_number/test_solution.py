import pytest

from leetcode_py import logged_test

from .helpers import assert_is_happy, run_is_happy
from .solution import Solution


class TestHappyNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (19, True),
            (2, False),
            (1, True),
            (7, True),
            (10, True),
            (13, True),
            (4, False),
            (3, False),
            (20, False),
            (100, True),
            (82, True),
            (68, True),
            (5, False),
            (1111111, True),
        ],
    )
    def test_is_happy(self, n: int, expected: bool):
        result = run_is_happy(Solution, n)
        assert_is_happy(result, expected)
