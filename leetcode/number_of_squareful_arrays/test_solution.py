import pytest

from leetcode_py import logged_test

from .helpers import assert_num_squareful_perms, run_num_squareful_perms
from .solution import Solution


class TestNumberOfSquarefulArrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 17, 8], 2),
            ([2, 2, 2], 1),
            ([1], 1),
            ([0], 1),
            ([0, 0], 1),
            ([1, 1], 0),
            ([1, 3], 2),
            ([2, 2, 7], 3),
            ([0, 1, 3], 2),
            ([1, 3, 6], 2),
            ([4, 5, 11], 2),
            ([1, 3, 8], 2),
            ([1, 8, 17, 0], 2),
            ([0, 0, 1, 3], 2),
            ([1000000000, 13129], 0),
            ([999950884, 0], 2),
            ([999950884, 0, 1], 2),
            ([2, 2, 2, 2], 1),
            ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1),
        ],
    )
    def test_num_squareful_perms(self, nums: list[int], expected: int):
        result = run_num_squareful_perms(Solution, nums)
        assert_num_squareful_perms(result, expected)
