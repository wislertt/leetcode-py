import pytest

from leetcode_py import logged_test

from .helpers import assert_is_ideal_permutation, run_is_ideal_permutation
from .solution import Solution


class TestGlobalAndLocalInversions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 0, 2], True),
            ([1, 2, 0], False),
            ([0], True),
            ([0, 1], True),
            ([1, 0], True),
            ([0, 1, 2], True),
            ([0, 2, 1], True),
            ([2, 0, 1], False),
            ([2, 1, 0], False),
            ([0, 1, 2, 3], True),
            ([1, 0, 3, 2], True),
            ([0, 3, 2, 1], False),
            ([0, 1, 2, 3, 4], True),
            ([0, 2, 1, 4, 3], True),
            ([3, 1, 4, 0, 2], False),
            ([0, 1, 2, 3, 4, 5], True),
            ([0, 2, 1, 4, 3, 5], True),
            ([5, 4, 0, 1, 3, 2], False),
            ([0, 1, 2, 3, 4, 5, 6], True),
            ([1, 0, 3, 2, 5, 4, 6], True),
            ([6, 3, 5, 0, 4, 1, 2], False),
            ([0, 1, 2, 3, 4, 5, 6, 7], True),
            ([0, 2, 1, 3, 4, 6, 5, 7], True),
            ([7, 3, 6, 0, 5, 4, 2, 1], False),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8], True),
            ([1, 0, 2, 4, 3, 6, 5, 7, 8], True),
            ([5, 0, 8, 1, 4, 7, 2, 3, 6], False),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True),
            ([1, 0, 3, 2, 4, 5, 6, 7, 9, 8], True),
            ([7, 1, 8, 2, 5, 3, 6, 0, 4, 9], False),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
            ([1, 0, 2, 3, 4, 5, 6, 8, 7, 10, 9], True),
            ([2, 10, 1, 3, 7, 9, 4, 6, 5, 8, 0], False),
        ],
    )
    def test_is_ideal_permutation(self, nums: list[int], expected: bool):
        result = run_is_ideal_permutation(Solution, nums)
        assert_is_ideal_permutation(result, expected)
