import pytest

from leetcode_py import logged_test

from .helpers import assert_beautiful_array, run_beautiful_array
from .solution import Solution


class TestBeautifulArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (15, 15),
            (20, 20),
            (25, 25),
            (33, 33),
            (40, 40),
        ],
    )
    def test_beautiful_array(self, n: int, expected: int):
        result = run_beautiful_array(Solution, n)
        assert_beautiful_array(result, expected)
