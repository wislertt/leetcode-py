import pytest

from leetcode_py import logged_test

from .helpers import assert_four_sum, run_four_sum
from .solution import Solution


class TestTest4Sum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
            ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
            ([1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
            ([1, 2, 3, 4], 100, []),
            ([], 0, []),
            ([0], 0, []),
            ([0, 0, 0, 0], 1, []),
            ([-2, -1, 0, 1, 2, 3], 0, [[-2, -1, 0, 3], [-2, -1, 1, 2]]),
            (
                [-3, -2, -1, 0, 0, 1, 2, 3],
                0,
                [
                    [-3, -2, 2, 3],
                    [-3, -1, 1, 3],
                    [-3, 0, 0, 3],
                    [-3, 0, 1, 2],
                    [-2, -1, 0, 3],
                    [-2, -1, 1, 2],
                    [-2, 0, 0, 2],
                    [-1, 0, 0, 1],
                ],
            ),
            ([1000000000, 1000000000, 1000000000, 1000000000], -294967296, []),
            ([-1, -1, 0, 1, 1], -2, []),
        ],
    )
    def test_four_sum(self, nums: list[int], target: int, expected: list[list[int]]):
        result = run_four_sum(Solution, nums, target)
        assert_four_sum(result, expected)
