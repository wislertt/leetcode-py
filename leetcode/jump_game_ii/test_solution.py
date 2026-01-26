import pytest

from leetcode_py import logged_test

from .helpers import assert_jump, run_jump
from .solution import Solution


class TestJumpGameIi:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 1, 1, 4], 2),
            ([2, 3, 0, 1, 4], 2),
            ([1, 2], 1),
            ([1, 1, 1, 1], 3),
            ([2, 1], 1),
            ([1, 2, 3], 2),
            ([2, 2, 0, 1], 2),
            ([1, 2, 1, 1, 1], 3),
            ([3, 2, 1], 1),
            ([1, 3, 2], 2),
            ([4, 1, 1, 3, 1, 1, 1], 2),
            ([1, 1, 1, 1, 1], 4),
            ([2, 3, 1], 1),
            ([2, 1, 1, 1, 4], 3),
            ([3, 1, 1, 1, 1], 2),
            ([1], 0),
            ([1, 2, 0, 1], 2),
            ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
            ([2, 1, 2, 1, 4], 2),
            ([1, 1, 2, 1, 1], 3),
        ],
    )
    def test_jump(self, nums: list[int], expected: int):
        result = run_jump(Solution, nums)
        assert_jump(result, expected)
