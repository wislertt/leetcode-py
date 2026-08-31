import pytest

from leetcode_py import logged_test

from .helpers import assert_find_bottom_left_value, run_find_bottom_left_value
from .solution import Solution


class TestFindBottomLeftTreeValue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 1, 3], 1),
            ([1, 2, 3, 4, None, 5, 6, None, None, 7], 7),
            ([1], 1),
            ([1, 2, 3], 2),
            ([1, 2, None, 3], 3),
            ([1, None, 2], 2),
            ([1, 2, 3, 4, 5], 4),
            ([1, 2, 3, None, 4, None, 5], 4),
            ([0, -1, 1, None, None, -2, 2], -2),
            ([1, 2, 2, 3, 3, None, None, 4], 4),
            ([7], 7),
            ([3, 1, 5, 0, 2, 4, 6], 0),
            ([1, 2, 3, 4, None, None, 5, 6], 6),
            ([10, 5, 15, 3, None, None, 20], 3),
            ([1, None, 2, None, 3], 3),
        ],
    )
    def test_find_bottom_left_value(self, root_list: list[int | None], expected: int):
        result = run_find_bottom_left_value(Solution, root_list)
        assert_find_bottom_left_value(result, expected)
