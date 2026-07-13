import pytest

from leetcode_py import logged_test

from .helpers import assert_majority_element, run_majority_element
from .solution import Solution


class TestMajorityElementII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 2, 3], [3]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 1, 1, 2, 2, 3], [1]),
            ([1, 2, 3], []),
            ([2, 2, 2, 2], [2]),
            ([1, 1, 2, 2, 3, 3], []),
            ([1, 1, 2], [1]),
            ([1, 2, 1, 2, 1], [1, 2]),
            ([0, 0, 0], [0]),
            ([1, 2, 3, 4], []),
            ([5, 5, 5, 5, 5], [5]),
            ([1, 2, 3, 1, 2, 3, 1, 2, 3, 1], [1]),
            ([1, 1, 2, 2], [1, 2]),
            ([4], [4]),
        ],
    )
    def test_majority_element(self, nums: list[int], expected: list[int]):
        result = run_majority_element(Solution, nums)
        assert_majority_element(result, expected)
