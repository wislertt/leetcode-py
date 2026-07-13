import pytest

from leetcode_py import logged_test

from .helpers import assert_rob, run_rob
from .solution import Solution


class TestHouseRobberIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 2, 3, None, 3, None, 1], 7),
            ([3, 4, 5, 1, 3, None, 1], 9),
            ([1], 1),
            ([2, 1, 3, None, 4], 7),
            ([1, 2, 3], 5),
            ([1, 2], 2),
            ([2, None, 3], 3),
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 35),
            ([3], 3),
            ([0], 0),
            ([2, 1, 3, None, 4, None, None], 7),
            ([10, 5, 15, None, None, 11, 20], 41),
            ([1, 2, 3, 4], 7),
            ([1, 2, 3, 4, 5], 12),
        ],
    )
    def test_rob(self, root_list: list[int | None], expected: int):
        result = run_rob(Solution, root_list)
        assert_rob(result, expected)
