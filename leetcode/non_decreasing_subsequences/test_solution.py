import pytest

from leetcode_py import logged_test

from .helpers import assert_find_subsequences, run_find_subsequences
from .solution import Solution


class TestNonDecreasingSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            (
                [4, 6, 7, 7],
                [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]],
            ),
            ([4, 4, 3, 2, 1], [[4, 4]]),
            ([1, 2, 3], [[1, 2], [1, 2, 3], [1, 3], [2, 3]]),
            ([1], []),
            ([2, 2], [[2, 2]]),
            ([1, 1, 1], [[1, 1], [1, 1, 1]]),
            ([3, 2, 1], []),
            ([1, 3, 2, 4], [[1, 2], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2, 4], [3, 4]]),
            ([-1, 0, -2, 3], [[-2, 3], [-1, 0], [-1, 0, 3], [-1, 3], [0, 3]]),
            ([7, 7], [[7, 7]]),
            ([100, -100], []),
            ([5, 5, 5, 5], [[5, 5], [5, 5, 5], [5, 5, 5, 5]]),
            ([1, 2, 1, 1, 1], [[1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 2]]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], []),
            ([-100, 100], [[-100, 100]]),
        ],
    )
    def test_find_subsequences(self, nums: list[int], expected: list[list[int]]):
        result = run_find_subsequences(Solution, nums)
        assert_find_subsequences(result, expected)
