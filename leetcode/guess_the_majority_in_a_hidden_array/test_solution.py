import pytest

from leetcode_py import logged_test

from .helpers import assert_guess_majority, run_guess_majority
from .solution import Solution


class TestGuessTheMajorityInAHiddenArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 0, 1, 0, 1, 1, 1, 1], 2),
            ([0, 0, 1, 1, 0], 0),
            ([1, 0, 1, 0, 1, 0, 1, 0], -1),
            ([1, 1, 1, 1, 1], 0),
            ([0, 0, 0, 0, 0], 0),
            ([0, 0, 0, 0, 1], 0),
            ([1, 0, 0, 0, 0], 1),
            ([1, 1, 1, 0, 1, 1], 0),
            ([0, 1, 1, 0, 0], 0),
            ([1, 1, 0, 0, 1, 1], 0),
            ([0, 0, 1, 0, 0], 0),
            ([1, 0, 0, 1, 0, 0, 1], 1),
            ([0, 1, 1, 1, 1, 0, 1], 1),
            ([0, 1, 0, 1, 0, 1], -1),
            ([1, 1, 0, 0, 0, 0, 1, 1], -1),
            ([1, 0, 1, 1, 0, 1, 1, 0, 1], 0),
            ([0, 0, 0, 1, 0, 0, 0, 0, 0], 0),
            ([1, 0, 1, 0, 1, 1], 0),
            ([0, 1, 1, 0, 1, 0], -1),
            ([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 0),
            ([0, 1, 1, 0, 0, 1, 1, 0], -1),
            ([1, 0, 0, 1, 1, 0, 1], 0),
            ([0, 0, 0, 0, 1, 0, 0, 1, 1], 0),
            ([0, 0, 1, 1, 1], 2),
            ([1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], 2),
            ([0, 0, 1, 0, 1, 0, 0], 0),
            ([0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1], -1),
            ([0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 0),
        ],
    )
    def test_guess_majority(self, nums: list[int], expected: int):
        result = run_guess_majority(Solution, nums)
        assert_guess_majority(result, expected, nums)
