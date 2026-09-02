import pytest

from leetcode_py import logged_test

from .helpers import assert_construct_rectangle, run_construct_rectangle
from .solution import Solution


class TestConstructRectangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "area, expected",
        [
            (4, [2, 2]),
            (37, [37, 1]),
            (122122, [427, 286]),
            (1, [1, 1]),
            (2, [2, 1]),
            (3, [3, 1]),
            (5, [5, 1]),
            (6, [3, 2]),
            (12, [4, 3]),
            (100, [10, 10]),
            (999, [37, 27]),
            (999983, [999983, 1]),
            (720720, [858, 840]),
            (1000000, [1000, 1000]),
            (10000000, [3200, 3125]),
            (9999999, [4649, 2151]),
        ],
    )
    def test_construct_rectangle(self, area: int, expected: list[int]):
        result = run_construct_rectangle(Solution, area)
        assert_construct_rectangle(result, expected)
