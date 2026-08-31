import pytest

from leetcode_py import logged_test

from .helpers import assert_connect, run_connect
from .solution import Solution


class TestPopulatingNextRightPointersInEachNode:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([1, 2, 3, 4, 5, 6, 7], [1, None, 2, 3, None, 4, 5, 6, 7, None]),
            ([], []),
            ([1], [1, None]),
            ([7], [7, None]),
            ([1, 2, 3], [1, None, 2, 3, None]),
            ([-1, -2, -3], [-1, None, -2, -3, None]),
            ([5, 4, 6], [5, None, 4, 6, None]),
            ([9, 8, 7], [9, None, 8, 7, None]),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [1, None, 2, 3, None, 4, 5, 6, 7, None, 8, 9, 10, 11, 12, 13, 14, 15, None],
            ),
            (
                [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                [15, None, 14, 13, None, 12, 11, 10, 9, None, 8, 7, 6, 5, 4, 3, 2, 1, None],
            ),
            ([0, 0, 0, 0, 0, 0, 0], [0, None, 0, 0, None, 0, 0, 0, 0, None]),
            ([3, 3, 3, 3, 3, 3, 3], [3, None, 3, 3, None, 3, 3, 3, 3, None]),
            ([10, 5, 15, 3, 7, 12, 18], [10, None, 5, 15, None, 3, 7, 12, 18, None]),
            ([100, 50, 200, 25, 75, 150, 250], [100, None, 50, 200, None, 25, 75, 150, 250, None]),
            (
                [-1000, 1000, -1000, 1000, -1000, 1000, -1000],
                [-1000, None, 1000, -1000, None, 1000, -1000, 1000, -1000, None],
            ),
            ([-3, -6, -9, -12, -24, -36, -48], [-3, None, -6, -9, None, -12, -24, -36, -48, None]),
        ],
    )
    def test_connect(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_connect(Solution, root_list)
        assert_connect(result, expected_list)
