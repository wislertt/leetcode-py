import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_ones, run_longest_ones
from .solution import Solution


class TestMaxConsecutiveOnesIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
            ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
            ([1, 1, 1], 0, 3),
            ([0, 0, 0], 0, 0),
            ([0, 0, 0], 3, 3),
            ([1, 0, 1, 0, 1], 1, 3),
            ([1], 0, 1),
            ([0], 1, 1),
            ([0], 0, 0),
            ([1, 1, 0, 1, 1, 0], 1, 5),
            ([0, 1, 0, 1, 0], 2, 4),
            ([1, 0, 0, 0, 1, 1, 1, 0, 1], 2, 6),
        ],
    )
    def test_longest_ones(self, nums: list[int], k: int, expected: int):
        result = run_longest_ones(Solution, nums, k)
        assert_longest_ones(result, expected)
