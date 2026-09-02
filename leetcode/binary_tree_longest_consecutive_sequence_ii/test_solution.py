import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_consecutive, run_longest_consecutive
from .solution import Solution


class TestBinaryTreeLongestConsecutiveSequenceII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3], 2),
            ([2, 1, 3], 3),
            ([1], 1),
            ([3, 2, None, 1], 3),
            ([5, 3, 6, 2, 4, None, None, 1], 4),
            ([1, None, 2, None, 3, None, 4], 4),
            ([1, 2, 3, 4, 5], 2),
            ([0, 3, -2], 1),
            ([-1, -3, -3, -3, 4], 1),
            ([-3, -2, -5, -1], 3),
            ([-4, -1, 0], 1),
            ([2, None, -5], 1),
        ],
    )
    def test_longest_consecutive(self, root_list: list[int | None], expected: int):
        result = run_longest_consecutive(Solution, root_list)
        assert_longest_consecutive(result, expected)
