import pytest

from leetcode_py import logged_test

from .helpers import assert_subsets_with_dup, run_subsets_with_dup
from .solution import Solution


class TestSubsetsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
            ([0], [[], [0]]),
            ([1], [[], [1]]),
            ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
            ([2, 2], [[], [2], [2, 2]]),
            ([1, 1], [[], [1], [1, 1]]),
            ([1, 1, 1], [[], [1], [1, 1], [1, 1, 1]]),
            ([4, 4, 4, 4], [[], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]),
            ([1, 2], [[], [1], [1, 2], [2]]),
            ([4, 1, 0], [[], [0], [0, 1], [0, 1, 4], [0, 4], [1], [1, 4], [4]]),
            ([-1, 0, 1], [[], [-1], [-1, 0], [-1, 0, 1], [-1, 1], [0], [0, 1], [1]]),
            (
                [3, 3, 3, 1, 1],
                [
                    [],
                    [1],
                    [1, 1],
                    [1, 1, 3],
                    [1, 1, 3, 3],
                    [1, 1, 3, 3, 3],
                    [1, 3],
                    [1, 3, 3],
                    [1, 3, 3, 3],
                    [3],
                    [3, 3],
                    [3, 3, 3],
                ],
            ),
            (
                [1, 2, 2, 3],
                [
                    [],
                    [1],
                    [1, 2],
                    [1, 2, 2],
                    [1, 2, 2, 3],
                    [1, 2, 3],
                    [1, 3],
                    [2],
                    [2, 2],
                    [2, 2, 3],
                    [2, 3],
                    [3],
                ],
            ),
        ],
    )
    def test_subsets_with_dup(self, nums: list[int], expected: list[list[int]]):
        result = run_subsets_with_dup(Solution, nums)
        assert_subsets_with_dup(result, expected)
