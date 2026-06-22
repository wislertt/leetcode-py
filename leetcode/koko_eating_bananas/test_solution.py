import pytest

from leetcode_py import logged_test

from .helpers import assert_min_eating_speed, run_min_eating_speed
from .solution import Solution


class TestKokoEatingBananas:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "piles, h, expected",
        [
            ([3, 6, 7, 11], 8, 4),
            ([30, 11, 23, 4, 20], 5, 30),
            ([30, 11, 23, 4, 20], 6, 23),
            ([1], 1, 1),
            ([5], 5, 1),
            ([1000000000], 2, 500000000),
            ([1, 1, 1, 1], 4, 1),
            ([10], 3, 4),
            ([2, 2, 2], 3, 2),
            ([3, 6, 7, 11], 1000000000, 1),
            ([100], 1, 100),
            ([1, 2, 3, 4, 5], 5, 5),
            ([8, 8, 8, 8], 8, 4),
        ],
    )
    def test_min_eating_speed(self, piles: list[int], h: int, expected: int):
        result = run_min_eating_speed(Solution, piles, h)
        assert_min_eating_speed(result, expected)
