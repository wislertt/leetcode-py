import pytest

from leetcode_py import logged_test

from .helpers import assert_connect, run_connect
from .solution import Solution


class TestPopulatingNextRightPointersInEachNodeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([1, 2, 3, 4, 5, None, 7], [1, None, 2, 3, None, 4, 5, 7, None]),
            ([], []),
            ([1], [1, None]),
            ([1, 2, 3], [1, None, 2, 3, None]),
            ([1, None, 2], [1, None, 2, None]),
            ([1, 2, None], [1, None, 2, None]),
            ([1, 2, 3, 4, None, None, 5], [1, None, 2, 3, None, 4, 5, None]),
            ([1, 2, 3, None, 4, 5, None], [1, None, 2, 3, None, 4, 5, None]),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, 10, None, None, 11],
                [1, None, 2, 3, None, 4, 5, 6, 7, None, 8, 9, 10, 11, None],
            ),
            ([1, 2, 3, 4, None, None, None, 5], [1, None, 2, 3, None, 4, None, 5, None]),
            ([3, 9, 20, None, None, 15, 7], [3, None, 9, 20, None, 15, 7, None]),
            ([-100, 100, -100, 100, -100], [-100, None, 100, -100, None, 100, -100, None]),
            ([0, -1, 1, -2, 2, -3, 3], [0, None, -1, 1, None, -2, 2, -3, 3, None]),
            ([-54, 2, None, 79, 34], [-54, None, 2, None, 79, 34, None]),
            ([-11, 67, -5, -59, 64, -99, 8], [-11, None, 67, -5, None, -59, 64, -99, 8, None]),
            ([51, -64, 40, -1], [51, None, -64, 40, None, -1, None]),
            ([-56, 51, None, -95, -15], [-56, None, 51, None, -95, -15, None]),
            ([4, -17, 42, -38, -6, -27, -89], [4, None, -17, 42, None, -38, -6, -27, -89, None]),
            ([-17, 13, None, None, 93, None, None, None, None], [-17, None, 13, None, 93, None]),
        ],
    )
    def test_connect(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_connect(Solution, root_list)
        assert_connect(result, expected_list)
