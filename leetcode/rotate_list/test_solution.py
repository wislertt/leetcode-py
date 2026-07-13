import pytest

from leetcode_py import logged_test

from .helpers import assert_rotate_right, run_rotate_right
from .solution import Solution


class TestRotateList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, k, expected",
        [
            ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
            ([0, 1, 2], 4, [2, 0, 1]),
            ([], 0, []),
            ([], 5, []),
            ([1], 0, [1]),
            ([1], 3, [1]),
            ([1, 2], 1, [2, 1]),
            ([1, 2], 2, [1, 2]),
            ([1, 2, 3], 1, [3, 1, 2]),
            ([1, 2, 3], 2, [2, 3, 1]),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
            ([1, 2, 3], 1000000000, [3, 1, 2]),
        ],
    )
    def test_rotate_right(self, head_list: list[int], k: int, expected: list[int]):
        result = run_rotate_right(Solution, head_list, k)
        assert_rotate_right(result, expected)
