import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_average_subtree, run_maximum_average_subtree
from .solution import Solution


class TestMaximumAverageSubtree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([5, 6, 1], 6.00000),
            ([0, None, 1], 1.00000),
            ([1], 1.00000),
            ([2, 1, 3], 3.00000),
            ([12, 8, 15, 1, None, 7, None, None, None, 3], 8.33333),
            ([4, 2, 6, 1, 3, 5, 7], 7.00000),
            ([9, 5, 20, 15, 7], 20.00000),
            ([1, None, 2, None, 3, None, 4], 4.00000),
            ([0], 0.00000),
            ([100, 50, 200, 25, 75, 150, 250], 250.00000),
            ([3, 0, 4, 0, 0, 0, 0], 1.33333),
            ([6, 3, 9, None, None, None, 0], 4.50000),
        ],
    )
    def test_maximum_average_subtree(self, root_list: list[int | None], expected: float):
        result = run_maximum_average_subtree(Solution, root_list)
        assert_maximum_average_subtree(result, expected)
