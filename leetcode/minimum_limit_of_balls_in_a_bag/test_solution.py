import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_size, run_minimum_size
from .solution import Solution


class TestMinimumLimitOfBallsInABag:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, max_operations, expected",
        [
            ([9], 2, 3),
            ([2, 4, 8, 2], 4, 2),
            ([1], 1, 1),
            ([1000000000], 1000000000, 1),
            ([1000000000], 1, 500000000),
            ([3], 1, 2),
            ([7], 2, 3),
            ([2, 2], 1, 2),
            ([4, 4, 4], 3, 2),
            ([1, 1000000000], 1000000000, 1),
            ([5, 9, 13], 4, 5),
            ([6, 7, 8, 9], 6, 4),
            ([11], 5, 2),
            ([100000], 3, 25000),
            ([999999999, 999999998], 2, 500000000),
            ([28, 18, 25, 6, 1], 8, 7),
            ([18, 5], 7, 3),
            ([24], 11, 2),
            ([14, 13, 30, 9], 3, 13),
            ([28, 7, 29, 2], 2, 15),
            ([6], 7, 1),
            ([13, 27], 11, 4),
        ],
    )
    def test_minimum_size(self, nums: list[int], max_operations: int, expected: int):
        result = run_minimum_size(Solution, nums, max_operations)
        assert_minimum_size(result, expected)
