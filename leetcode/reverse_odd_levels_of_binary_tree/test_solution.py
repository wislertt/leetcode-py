import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_odd_levels, run_reverse_odd_levels
from .solution import Solution


class TestReverseOddLevelsOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([2], [2]),
            ([7], [7]),
            ([0], [0]),
            ([2, 3, 5], [2, 5, 3]),
            ([7, 13, 11], [7, 11, 13]),
            ([4, 2, 7], [4, 7, 2]),
            ([0, 1, 2], [0, 2, 1]),
            ([5, 4, 8], [5, 8, 4]),
            ([2, 3, 5, 8, 13, 21, 34], [2, 5, 3, 8, 13, 21, 34]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7]),
            ([9, 8, 7, 6, 5, 4, 3], [9, 7, 8, 6, 5, 4, 3]),
            ([100, 50, 150, 25, 75, 125, 175], [100, 150, 50, 25, 75, 125, 175]),
            ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]),
            ([0, 10, 20, 30, 40, 50, 60], [0, 20, 10, 30, 40, 50, 60]),
            ([64, 18, 18, 12, 48, 10, 46], [64, 18, 18, 12, 48, 10, 46]),
            ([50, 2, 90], [50, 90, 2]),
            ([1, 52, 47], [1, 47, 52]),
        ],
    )
    def test_reverse_odd_levels(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_reverse_odd_levels(Solution, root_list)
        assert_reverse_odd_levels(result, expected_list)
