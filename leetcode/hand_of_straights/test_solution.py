import pytest

from leetcode_py import logged_test

from .helpers import assert_is_n_straight_hand, run_is_n_straight_hand
from .solution import Solution


class TestHandOfStraights:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "hand, group_size, expected",
        [
            ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
            ([1, 2, 3, 4, 5], 4, False),
            ([1], 1, True),
            ([1, 2, 3], 1, True),
            ([1, 2, 3, 4], 2, True),
            ([1, 2, 3, 4], 4, True),
            ([1, 2, 4], 3, False),
            ([1, 1, 2, 2, 3, 3], 3, True),
            ([1, 2, 3, 4, 5, 6], 3, True),
            ([1, 2, 3, 4, 5], 1, True),
            ([8, 8, 9, 7, 7, 9], 3, True),
            ([1, 2, 3, 4, 6, 7, 8], 3, False),
            ([1, 2, 3, 5], 4, False),
        ],
    )
    def test_is_n_straight_hand(self, hand: list[int], group_size: int, expected: bool):
        result = run_is_n_straight_hand(Solution, hand, group_size)
        assert_is_n_straight_hand(result, expected)
