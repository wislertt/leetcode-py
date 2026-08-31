import pytest

from leetcode_py import logged_test

from .helpers import assert_convert_bst, run_convert_bst
from .solution import Solution


class TestConvertBstToGreaterTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            (
                [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
                [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8],
            ),
            ([0, None, 1], [1, None, 1]),
            ([], []),
            ([1], [1]),
            ([2, 1, 3], [5, 6, 3]),
            ([1, None, 2], [3, None, 2]),
            ([3, 2, 4, 1], [7, 9, 4, 10]),
            ([1, 2], [1, 3]),
            ([0, -1], [0, -1]),
            ([5, 3, 7, 2, 4, 6, 8], [26, 33, 15, 35, 30, 21, 8]),
            ([10, 5, 15], [25, 30, 15]),
            ([-3, -5, -1], [-4, -9, -1]),
            ([100, 50, 150, 25, 75], [250, 375, 150, 400, 325]),
            ([4, 2, 6, 1, 3, 5, 7], [22, 27, 13, 28, 25, 18, 7]),
            ([2, 1], [2, 3]),
        ],
    )
    def test_convert_bst(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_convert_bst(Solution, root_list)
        assert_convert_bst(result, expected_list)
