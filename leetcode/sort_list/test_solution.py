import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_list, run_sort_list
from .solution import Solution


class TestSortList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([4, 2, 1, 3], [1, 2, 3, 4]),
            ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2], [1, 2]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([3, -1, 0, 4, 2], [-1, 0, 2, 3, 4]),
            ([-10, 5, -3, 8, 0], [-10, -3, 0, 5, 8]),
            ([1, 1, 1], [1, 1, 1]),
            ([3, 3, 1, 2, 2], [1, 2, 2, 3, 3]),
            ([100], [100]),
            ([-5], [-5]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ],
    )
    def test_sort_list(self, head_list: list[int], expected: list[int]):
        result = run_sort_list(Solution, head_list)
        assert_sort_list(result, expected)
