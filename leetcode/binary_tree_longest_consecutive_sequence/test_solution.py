import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_consecutive, run_longest_consecutive
from .solution import Solution


class TestBinaryTreeLongestConsecutiveSequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 3, 2, 4, None, None, None, 5], 3),
            ([2, None, 3, 2, None, 1], 2),
            ([1], 1),
            ([1, 2, 3], 2),
            ([1, None, 2, None, 3, None, 4], 4),
            ([3, 4, None, 5, None, 6, None], 4),
            ([5, 4, 3, 2, 1], 1),
            ([1, 2, None, 3, None, 4, None, 5], 5),
            ([2, 1, 3], 2),
            ([1, 3, 2, 4, None, None, 5], 2),
            ([7, 8, 6, None, 9], 3),
            ([-3, -2, None, -1], 3),
            ([10, 11, None, 12, None, 13], 4),
            ([1, 2, 2, 3, 1], 3),
            ([100, 50, 101], 2),
        ],
    )
    def test_longest_consecutive(self, root_list: list[int | None], expected: int):
        result = run_longest_consecutive(Solution, root_list)
        assert_longest_consecutive(result, expected)
