import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_largest_level_sum, run_kth_largest_level_sum
from .solution import Solution


class TestKthLargestSumInABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, k, expected",
        [
            ([5, 8, 9, 2, 1, 3, 7, 4, 6], 2, 13),
            ([1, 2, None, 3], 1, 3),
            ([5, 8, 9, 2, 1, 3, 7, 4, 6], 4, 5),
            ([5, 8, 9, 2, 1, 3, 7, 4, 6], 5, -1),
            ([1, 2], 1, 2),
            ([1, 2], 2, 1),
            ([1, 2, 3], 3, -1),
            ([10, 20, 30, 40, 50, 60, 70], 2, 50),
            ([1, None, 2, None, 3], 3, 1),
            ([999999, 1000000, 999998], 1, 1999998),
            ([7, 7, 7, 7], 2, 7),
            ([3, 1, 4, None, 2, None, 5], 1, 7),
            ([57, 47, 81, 89, 62, 78, 56], 2, 128),
            ([80, 100, 70, None, 42, 14, 91, 49, 86, None, 47, 47, 90, 10], 5, 10),
            ([24, 97], 2, 24),
            ([68, 78, 83, 85, 92, None, 49, None, 86, 40, 49, None, 75], 4, 68),
            ([3, 74, None, 40, 68, 82, 100], 2, 108),
            ([65, 36, 61, 36, 14, 80, 32], 1, 162),
        ],
    )
    def test_kth_largest_level_sum(self, root_list: list[int | None], k: int, expected: int):
        result = run_kth_largest_level_sum(Solution, root_list, k)
        assert_kth_largest_level_sum(result, expected)
