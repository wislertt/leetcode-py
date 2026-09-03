import pytest

from leetcode_py import logged_test

from .helpers import assert_subarray_bitwise_ors, run_subarray_bitwise_ors
from .solution import Solution


class TestBitwiseOrsOfSubarrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([0], 1),
            ([1, 1, 2], 3),
            ([1, 2, 4], 6),
            ([1], 1),
            ([7], 1),
            ([0, 0, 0], 1),
            ([5, 5, 5], 1),
            ([1, 2, 4, 8], 10),
            ([1, 3, 7, 15], 4),
            ([2, 2, 2, 3], 2),
            ([1000000000, 1], 3),
            ([6, 5, 3, 12], 6),
            ([14, 7, 1, 8], 6),
            ([3, 5, 6, 7], 4),
            ([10, 11, 12, 13], 5),
            ([5, 18, 50, 41, 42, 63, 38, 24, 54], 14),
            ([283887967, 355316119, 637561638, 696862146, 85276808, 595906915], 19),
            ([1, 0, 1, 0, 1], 2),
            ([8, 4, 2, 1, 3, 5, 9], 13),
        ],
    )
    def test_subarray_bitwise_ors(self, arr: list[int], expected: int):
        result = run_subarray_bitwise_ors(Solution, arr)
        assert_subarray_bitwise_ors(result, expected)
