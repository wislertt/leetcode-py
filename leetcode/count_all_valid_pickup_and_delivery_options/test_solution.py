import pytest

from leetcode_py import logged_test

from .helpers import assert_count_orders, run_count_orders
from .solution import Solution


class TestCountAllValidPickupAndDeliveryOptions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 6),
            (3, 90),
            (4, 2520),
            (5, 113400),
            (6, 7484400),
            (7, 681080400),
            (8, 729647433),
            (9, 636056472),
            (10, 850728840),
            (25, 586091532),
            (100, 14159051),
            (500, 764678010),
        ],
    )
    def test_count_orders(self, n: int, expected: int):
        result = run_count_orders(Solution, n)
        assert_count_orders(result, expected)
