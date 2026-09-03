import pytest

from leetcode_py import logged_test

from .helpers import assert_is_rectangle_overlap, run_is_rectangle_overlap
from .solution import Solution


class TestRectangleOverlap:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rec1, rec2, expected",
        [
            ([0, 0, 2, 2], [1, 1, 3, 3], True),
            ([0, 0, 1, 1], [1, 0, 2, 1], False),
            ([0, 0, 1, 1], [2, 2, 3, 3], False),
            ([0, 0, 1, 1], [1, 1, 2, 2], False),
            ([0, 0, 1, 1], [-1, -1, 0, 0], False),
            ([0, 0, 1, 1], [0, 1, 1, 2], False),
            ([0, 0, 2, 3], [1, -1, 3, 0], False),
            ([0, 0, 1, 1], [0, 2, 1, 3], False),
            ([0, 0, 1, 1], [5, 0, 6, 1], False),
            ([0, 0, 5, 5], [1, 1, 2, 2], True),
            ([0, 0, 3, 3], [0, 0, 3, 3], True),
            ([0, 0, 10, 10], [0, 0, 5, 5], True),
            ([-5, -5, -1, -1], [-2, -2, 1, 1], True),
            ([-3, -3, 0, 0], [-1, -1, 2, 2], True),
            ([0, 0, 4, 1], [-1, -1, 1, 3], True),
            ([1, 1, 3, 3], [2, 2, 4, 4], True),
            ([0, 0, 100000000, 100000000], [-100000000, 0, 0, 1], False),
            ([-100000000, -100000000, 100000000, 100000000], [-1, -1, 0, 0], True),
        ],
    )
    def test_is_rectangle_overlap(self, rec1: list[int], rec2: list[int], expected: bool):
        result = run_is_rectangle_overlap(Solution, rec1, rec2)
        assert_is_rectangle_overlap(result, expected)
