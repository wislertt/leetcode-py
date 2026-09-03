import pytest

from leetcode_py import logged_test

from .helpers import assert_find_target, run_find_target
from .solution import Solution


class TestTwoSumIVInputIsABST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, k, expected",
        [
            ([5, 3, 6, 2, 4, None, 7], 9, True),
            ([5, 3, 6, 2, 4, None, 7], 28, False),
            ([1], 2, False),
            ([1], 1, False),
            ([1], 100000, False),
            ([1], -100000, False),
            ([-5, -10, 3, None, None, -2, 4], -15, True),
            ([-5, -10, 3, None, None, -2, 4], -12, True),
            ([-5, -10, 3, None, None, -2, 4], 100, False),
            ([2, 1, 3], 4, True),
            ([2, 1, 3], 3, True),
            ([2, 1, 3], 2, False),
            ([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7], 13, True),
            ([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7], 1, False),
            ([0, -1, None, -2, None, -3, None, -4], -7, True),
            ([0, -1, None, -2, None, -3, None, -4], 0, False),
            ([34, -19, None, None, 23, -5, None, None, 16, 8, 18], 52, True),
            ([17, -25, 24, None, -10, None, 26], 16, True),
            ([-28, None, 24, -14, None, -26, 9], 34, False),
            ([31, -6, None, -28, None, -32, -7, -38], 90, False),
            ([31, -17, None, None, -12, None, 20, None, 28], 48, True),
            ([-25, None, -11, None, 7, -2, 10], 6, False),
            ([27, 24, None, -23, 26], 0, False),
            ([-23, -38, 21, None, None, 19, 32, 16, None, None, None, 1], -7, True),
            ([-24, -30, -13, None, None, -21, 36], 12, True),
            ([9000, -10000, 10000, None, -5000, 9500], -15000, True),
            ([9000, -10000, 10000, None, -5000, 9500], 19000, True),
            ([9000, -10000, 10000, None, -5000, 9500], 0, True),
        ],
    )
    def test_find_target(self, root_list: list[int | None], k: int, expected: bool):
        result = run_find_target(Solution, root_list, k)
        assert_find_target(result, expected)
