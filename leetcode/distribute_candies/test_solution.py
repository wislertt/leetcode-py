import pytest

from leetcode_py import logged_test

from .helpers import assert_distribute_candies, run_distribute_candies
from .solution import Solution


class TestDistributeCandies:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "candy_type, expected",
        [
            ([1, 1, 2, 2, 3, 3], 3),
            ([1, 1, 2, 3], 2),
            ([6, 6, 6, 6], 1),
            ([1, 1], 1),
            ([1, 2], 1),
            ([1, 1, 1, 1], 1),
            ([1, 2, 3, 4], 2),
            ([1, 1, 1, 2, 2, 2], 2),
            ([1, 2, 2, 2, 3, 3], 3),
            ([0, 0, 0, 0, 0, 0, 0, 0], 1),
            ([-1, -1, -2, -2], 2),
            ([100000, -100000], 1),
            ([5, 5, 5, 5, 9, 9, 9, 9], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6),
            ([4, 4, -6, -8, -6, 4], 3),
            ([3, -1, -1, -1], 2),
        ],
    )
    def test_distribute_candies(self, candy_type: list[int], expected: int):
        result = run_distribute_candies(Solution, candy_type)
        assert_distribute_candies(result, expected)
