import pytest

from leetcode_py import logged_test

from .helpers import assert_has_path_sum, run_has_path_sum
from .solution import Solution


class TestPathSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target_sum, expected",
        [
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
            ([1, 2, 3], 5, False),
            ([], 0, False),
            ([], 1, False),
            ([1], 1, True),
            ([1], 2, False),
            ([1, 2], 1, False),
            ([1, 2], 3, True),
            ([1, 2, 3], 3, True),
            ([1, 2, 3], 4, True),
            ([1, -2, -3], -1, True),
            ([1, -2, -3], -2, True),
            ([2, 1, 3], 5, True),
            ([2, 1, 3], 4, False),
            ([1, 2, None, 3], 6, True),
            ([1, None, 2, None, 3], 3, False),
            ([1, None, 2, None, 3], 6, True),
            ([0, 0, 0], 0, True),
            ([-1, -2, None, None, -3], -6, True),
            ([-1, -2, None, None, -3], -3, False),
        ],
    )
    def test_has_path_sum(self, root_list: list[int | None], target_sum: int, expected: bool):
        result = run_has_path_sum(Solution, root_list, target_sum)
        assert_has_path_sum(result, expected)
