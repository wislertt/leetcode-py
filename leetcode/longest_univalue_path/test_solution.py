import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_univalue_path, run_longest_univalue_path
from .solution import Solution


class TestLongestUnivaluePath:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([5, 4, 5, 1, 1, None, 5], 2),
            ([1, 4, 5, 4, 4, None, 5], 2),
            ([], 0),
            ([1], 0),
            ([1, 1, 1], 2),
            ([1, 1, 2], 1),
            ([2, 2, 2, 2, 2], 3),
            ([1, 2, 2, 2, 2], 2),
            ([5, 4, 5, 1, 1, 5], 2),
            ([1, 1, None, 1, 1], 2),
            ([4, -7, -3, -9, -3], 0),
            ([1, 1, 1, 1, None, None, 1, 1], 5),
            ([1000, 1000, -1000, 1000], 2),
            ([0, 0, 0, None, 0, None, 0], 4),
            ([1, 1, 1, None, 1, 1, 0], 4),
            ([-2, 2, -2, None, 2, -2], 2),
            ([1, 1], 1),
            ([-1, 0, -1, -2, 0, 1, -1], 2),
        ],
    )
    def test_longest_univalue_path(self, root_list: list[int | None], expected: int):
        result = run_longest_univalue_path(Solution, root_list)
        assert_longest_univalue_path(result, expected)
