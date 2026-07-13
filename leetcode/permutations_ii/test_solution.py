import pytest

from leetcode_py import logged_test

from .helpers import assert_permute_unique, run_permute_unique
from .solution import Solution


class TestTestPermutationsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([1], [[1]]),
            ([1, 1], [[1, 1]]),
            ([1, 1, 1], [[1, 1, 1]]),
            ([1, 2], [[1, 2], [2, 1]]),
            ([1, 1, 1, 1], [[1, 1, 1, 1]]),
            (
                [2, 2, 1, 1],
                [
                    [1, 1, 2, 2],
                    [1, 2, 1, 2],
                    [1, 2, 2, 1],
                    [2, 1, 1, 2],
                    [2, 1, 2, 1],
                    [2, 2, 1, 1],
                ],
            ),
            ([-1, -1, 0], [[-1, -1, 0], [-1, 0, -1], [0, -1, -1]]),
            ([1, 2, 2], [[1, 2, 2], [2, 1, 2], [2, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([3, 3, 3, 3], [[3, 3, 3, 3]]),
        ],
    )
    def test_permute_unique(self, nums: list[int], expected: list[list[int]]):
        result = run_permute_unique(Solution, nums)
        assert_permute_unique(result, expected)
