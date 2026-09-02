import pytest

from leetcode_py import logged_test

from .helpers import assert_find_mode, run_find_mode
from .solution import Solution


class TestFindModeInBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 2, 2], [2]),
            ([0], [0]),
            ([1], [1]),
            ([1, 1], [1]),
            ([1, None, 2], [1, 2]),
            ([2, 1, 2], [2]),
            ([2, 1, 3], [1, 2, 3]),
            ([3, 3, 3], [3]),
            ([2, 1, 3, None, None, None, 4], [1, 2, 3, 4]),
            ([5, 3, 5, 3, None, None, 5], [5]),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 2, 6], [2, 6]),
            ([1, None, 2, None, 3], [1, 2, 3]),
            ([0, 0, 0, 0], [0]),
            ([-1, -1, 0], [-1]),
            ([-3, -3, -2, -3], [-3]),
            ([4, 2, 6, 2, 3, 6, 7], [2, 6]),
            ([2, None, 2, None, 2], [2]),
            ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
            ([6, 3, 8, 3, 5, 8, 9, 1, None, None, 5, None, None, None, 9], [3, 5, 8, 9]),
        ],
    )
    def test_find_mode(self, root_list: list[int | None], expected: list[int]):
        result = run_find_mode(Solution, root_list)
        assert_find_mode(result, expected)
