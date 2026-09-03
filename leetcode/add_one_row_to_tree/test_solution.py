import pytest

from leetcode_py import logged_test

from .helpers import assert_add_one_row, run_add_one_row
from .solution import Solution


class TestAddOneRowToTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, val, depth, expected_list",
        [
            ([4, 2, 6, 3, 1, 5], 1, 2, [4, 1, 1, 2, None, None, 6, 3, 1, 5]),
            ([4, 2, None, 3, 1], 1, 3, [4, 2, None, 1, 1, 3, None, None, 1]),
            ([1], 1, 1, [1, 1]),
            ([4, 2, 6, 3, 1, 5], 1, 1, [1, 4, None, 2, 6, 3, 1, 5]),
            ([-1, -2, -3], 0, 1, [0, -1, None, -2, -3]),
            ([1], 5, 2, [1, 5, 5]),
            ([1], -5, 2, [1, -5, -5]),
            ([4, 2, 6, 3, 1, 5], 9, 3, [4, 2, 6, 9, 9, 9, 9, 3, None, None, 1, 5]),
            ([4, 2, 6, 3, 1, 5], 9, 4, [4, 2, 6, 3, 1, 5, None, 9, 9, 9, 9, 9, 9]),
            ([4, 2, None, 3, 1], 1, 4, [4, 2, None, 3, 1, 1, 1, 1, 1]),
            ([1, 2, 3, 4, 5], 6, 3, [1, 2, 3, 6, 6, 6, 6, 4, None, None, 5]),
            ([3, 1, 5, None, 2], 7, 3, [3, 1, 5, 7, 7, 7, 7, None, None, None, 2]),
            ([1, 2, None, 3, None, 4], 10, 4, [1, 2, None, 3, None, 10, 10, 4]),
            ([1, None, 2, None, 3], -10, 4, [1, None, 2, None, 3, -10, -10]),
            ([100, -100, 100], 50, 2, [100, 50, 50, -100, None, None, 100]),
            ([10, -100, -50], -100, 3, [10, -100, -50, -100, -100, -100, -100]),
            ([0], 100000, 2, [0, 100000, 100000]),
            ([-4, -84, None, -90], 69, 1, [69, -4, None, -84, None, -90]),
            ([-22], -25, 1, [-25, -22]),
            ([-85, None, -1, 72, 40], -73, 3, [-85, None, -1, -73, -73, 72, None, None, 40]),
            (
                [44, -82, 79, -31, 8, None, -90],
                -34,
                2,
                [44, -34, -34, -82, None, None, 79, -31, 8, None, -90],
            ),
        ],
    )
    def test_add_one_row(
        self, root_list: list[int | None], val: int, depth: int, expected_list: list[int | None]
    ):
        result = run_add_one_row(Solution, root_list, val, depth)
        assert_add_one_row(result, expected_list)
