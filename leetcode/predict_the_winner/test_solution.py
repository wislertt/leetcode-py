import pytest

from leetcode_py import logged_test

from .helpers import assert_predict_the_winner, run_predict_the_winner
from .solution import Solution


class TestPredictTheWinner:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 5, 2], False),
            ([1, 5, 233, 7], True),
            ([0], True),
            ([7], True),
            ([1, 1], True),
            ([0, 0], True),
            ([1, 2], True),
            ([2, 1], True),
            ([1, 5, 2, 6], True),
            ([1, 3, 1], False),
            ([2, 4, 6], True),
            ([5, 5, 5, 5], True),
            ([1, 100, 2, 99], True),
            ([20, 1, 20, 1, 20], False),
            ([10000000], True),
            ([10000000, 0, 0, 10000000], True),
            ([3, 7, 2, 9, 4], False),
            ([8, 15, 3, 7], True),
            ([7, 7, 29, 29, 17, 22, 0], False),
            ([2, 10, 25, 21, 22, 30, 18, 14, 1], False),
            ([19, 10, 20, 1, 7, 3, 21], False),
            ([14, 10, 16, 11, 3, 25, 2, 2, 29], False),
            ([12, 21, 27, 2, 5, 5, 13, 2, 8], False),
            ([20, 3246762, 24, 27], True),
        ],
    )
    def test_predict_the_winner(self, nums: list[int], expected: bool):
        result = run_predict_the_winner(Solution, nums)
        assert_predict_the_winner(result, expected)
