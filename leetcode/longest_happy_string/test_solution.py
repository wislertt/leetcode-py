import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_happy_string, run_longest_happy_string
from .solution import Solution


class TestLongestHappyString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, c",
        [
            (1, 1, 7),
            (7, 1, 0),
            (1, 1, 1),
            (0, 0, 7),
            (2, 2, 2),
            (0, 0, 1),
            (3, 3, 3),
            (100, 0, 0),
            (0, 5, 3),
            (1, 0, 0),
            (2, 0, 0),
            (4, 4, 0),
            (5, 5, 0),
            (10, 1, 0),
            (3, 3, 1),
            (0, 1, 1),
            (1, 2, 3),
            (0, 100, 100),
        ],
    )
    def test_longest_happy_string(self, a: int, b: int, c: int):
        result = run_longest_happy_string(Solution, a, b, c)
        assert_longest_happy_string(result, a, b, c)
