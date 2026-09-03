import pytest

from leetcode_py import logged_test

from .helpers import assert_str_without3a3b, run_str_without3a3b
from .solution import Solution


class TestStringWithoutAAAOrBBB:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (4, 1, 5),
            (1, 1, 2),
            (0, 1, 1),
            (1, 0, 1),
            (0, 0, 0),
            (2, 2, 4),
            (3, 3, 6),
            (5, 3, 8),
            (7, 4, 11),
            (0, 2, 2),
            (2, 0, 2),
            (100, 100, 200),
            (100, 50, 150),
            (100, 51, 151),
            (99, 49, 148),
        ],
    )
    def test_str_without3a3b(self, a: int, b: int, expected: int):
        result = run_str_without3a3b(Solution, a, b)
        assert_str_without3a3b(result, expected)
