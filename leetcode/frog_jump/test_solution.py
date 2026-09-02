import pytest

from leetcode_py import logged_test

from .helpers import assert_can_cross, run_can_cross
from .solution import Solution


class TestFrogJump:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stones, expected",
        [
            ([0, 1, 3, 5, 6, 8, 12, 17], True),
            ([0, 1], True),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
            ([0, 1, 3, 5, 6], True),
            ([0, 1, 2, 4, 7], True),
            ([0, 1, 3, 6, 9, 13, 18], True),
            ([0, 1, 2, 4, 5, 7], True),
            ([0, 1, 2, 4, 7, 11], True),
            ([0, 1, 2, 3, 4, 8, 9, 11], False),
            ([0, 2], False),
            ([0, 1, 3, 6, 10, 16], False),
            ([0, 1, 2, 3, 7, 8, 12], False),
            ([0, 5, 9, 14], False),
            ([0, 1, 3, 7, 12, 18, 25, 31], False),
            ([0, 2147483646, 2147483647], False),
            ([0, 1, 3, 2147483647], False),
            ([0, 1, 2, 4, 7, 11, 16, 17], False),
        ],
    )
    def test_can_cross(self, stones: list[int], expected: bool):
        result = run_can_cross(Solution, stones)
        assert_can_cross(result, expected)
