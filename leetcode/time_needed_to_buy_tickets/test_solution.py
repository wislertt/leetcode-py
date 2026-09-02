import pytest

from leetcode_py import logged_test

from .helpers import assert_time_required_to_buy, run_time_required_to_buy
from .solution import Solution


class TestTimeNeededToBuyTickets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tickets, k, expected",
        [
            ([2, 3, 2], 2, 6),
            ([5, 1, 1, 1], 0, 8),
            ([1], 0, 1),
            ([100], 0, 100),
            ([1, 2], 0, 1),
            ([1, 2], 1, 3),
            ([2, 3, 2], 0, 4),
            ([2, 3, 2], 1, 7),
            ([5, 1, 1, 1], 3, 4),
            ([84, 49, 5, 24, 70, 77, 43, 19], 6, 263),
            ([1, 1, 1, 1, 1], 4, 5),
            ([3, 3, 3, 3], 2, 11),
            ([100, 1, 100, 1], 0, 201),
            ([1, 100, 1], 1, 102),
            ([7, 7, 7, 7, 7, 7], 5, 42),
            ([2, 1, 3, 4, 1, 2, 5, 1], 7, 8),
            ([10, 9, 11, 1], 0, 29),
            ([4, 2], 1, 4),
        ],
    )
    def test_time_required_to_buy(self, tickets: list[int], k: int, expected: int):
        result = run_time_required_to_buy(Solution, tickets, k)
        assert_time_required_to_buy(result, expected)
