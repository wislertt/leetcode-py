import pytest

from leetcode_py import logged_test

from .helpers import assert_xor_game, run_xor_game
from .solution import Solution


class TestChalkboardXorGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2], False),
            ([0, 1], True),
            ([1, 2, 3], True),
            ([0], True),
            ([1], False),
            ([7], False),
            ([1, 1], True),
            ([5, 5], True),
            ([1, 2], True),
            ([2], False),
            ([1, 1, 1], False),
            ([2, 2, 2], False),
            ([0, 0, 0], True),
            ([1, 2, 3, 4], True),
            ([0, 1, 2, 3], True),
            ([1, 1, 2, 2, 3], False),
            ([3, 3, 3, 3, 3], False),
            ([0, 1, 2, 3, 4, 5], True),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8], False),
            ([1, 1, 1, 2, 2, 2, 3], True),
            ([4, 4, 8, 8, 15, 15, 15], False),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], False),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], True),
            ([3, 2, 3, 2, 3, 2], True),
            ([1, 0, 1, 3, 0, 3, 3], False),
            ([1, 0], True),
            ([2, 0, 1, 3, 2], False),
            ([2, 0, 3, 1, 1], False),
            ([2, 0, 2, 1, 0, 2, 2], False),
            ([2, 2, 3, 3, 2], False),
            ([3, 2, 0], False),
        ],
    )
    def test_xor_game(self, nums: list[int], expected: bool):
        result = run_xor_game(Solution, nums)
        assert_xor_game(result, expected)
