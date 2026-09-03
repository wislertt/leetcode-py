import pytest

from leetcode_py import logged_test

from .helpers import assert_is_cousins, run_is_cousins
from .solution import Solution


class TestCousinsInBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, x, y, expected",
        [
            ([1, 2, 3, 4], 4, 3, False),
            ([1, 2, 3, None, 4, None, 5], 5, 4, True),
            ([1, 2, 3, None, 4], 2, 3, False),
            ([1, 2, 3], 2, 3, False),
            ([1, 2], 1, 2, False),
            ([1, 2, 3, 4, 5], 4, 5, False),
            ([1, 2, 3, None, 4, None, 5], 4, 5, True),
            ([1, 2, 3, 4, 5, 6, 7], 4, 6, True),
            ([1, 2, 3, 4, 5, 6, 7], 4, 7, True),
            ([1, 2, None, 3, None, 4], 3, 4, False),
            ([1, None, 2, None, 3], 1, 3, False),
            ([10, 1, 2, 3, 4, 5, 6, 7], 7, 4, False),
            ([11, 19], 11, 19, False),
            ([34, 40, 80, 54, 31, None, 39, 5, 6], 34, 80, False),
            ([92, 7, None, 98, 85, None, 37], 7, 37, False),
            ([15, None, 17, 61], 61, 17, False),
        ],
    )
    def test_is_cousins(self, root_list: list[int | None], x: int, y: int, expected: bool):
        result = run_is_cousins(Solution, root_list, x, y)
        assert_is_cousins(result, expected)
