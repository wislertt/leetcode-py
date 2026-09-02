import pytest

from leetcode_py import logged_test

from .helpers import assert_is_majority_element, run_is_majority_element
from .solution import Solution


class TestCheckIfANumberIsMajorityElementInASortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([2, 4, 5, 5, 5, 5, 5, 6, 6], 5, True),
            ([10, 100, 101, 101], 101, False),
            ([1], 1, True),
            ([1], 2, False),
            ([5, 5, 5, 5], 5, True),
            ([1, 2, 3, 4], 3, False),
            ([2, 2], 2, True),
            ([1, 1, 2, 2], 1, False),
            ([1, 2, 2, 2, 3], 2, True),
            ([1, 2, 3, 4, 4, 4, 4, 4], 4, True),
            ([7, 7, 7], 7, True),
            ([1, 1, 1, 1, 1, 1, 1, 2], 1, True),
            ([3, 3, 3, 3, 9, 9], 3, True),
            ([5, 5, 5, 8, 9], 5, True),
            ([999999999], 999999999, True),
            ([1, 1, 1, 1, 1], 5, False),
            ([2, 4, 5, 5, 5, 5, 5, 6, 6], 6, False),
            ([1, 1, 2, 2, 3, 3, 4, 4], 4, False),
            ([4, 8, 14], 1, False),
            ([1, 2, 15, 16], 9, False),
            ([1, 10, 12, 15], 15, False),
            ([5, 5, 9, 11, 13, 14, 15], 6, False),
            ([1, 2, 5, 6, 6, 10, 11, 12, 13, 14], 12, False),
            ([2, 3, 10, 10, 11, 13, 15], 2, False),
            ([1, 3, 4, 5, 7, 9, 10, 15, 15, 16], 15, False),
            ([2, 3, 4, 7, 11, 12, 12, 15, 16], 4, False),
        ],
    )
    def test_is_majority_element(self, nums: list[int], target: int, expected: bool):
        result = run_is_majority_element(Solution, nums, target)
        assert_is_majority_element(result, expected)
