import pytest

from leetcode_py import logged_test

from .helpers import assert_best_closing_time, run_best_closing_time
from .solution import Solution


class TestMinimumPenaltyForAShop:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "customers, expected",
        [
            ("YYNY", 2),
            ("NNNNN", 0),
            ("YYYY", 4),
            ("Y", 1),
            ("N", 0),
            ("NY", 0),
            ("YN", 1),
            ("NN", 0),
            ("YY", 2),
            ("NYNY", 0),
            ("YNNY", 1),
            ("NNYY", 0),
            ("YYNN", 2),
            ("NYYN", 3),
            ("NYY", 3),
            ("YYNYNYNN", 2),
            ("NYYNYN", 3),
            ("YNYYN", 4),
            ("YYNYYN", 5),
            ("YNNYYNNN", 1),
        ],
    )
    def test_best_closing_time(self, customers: str, expected: int):
        result = run_best_closing_time(Solution, customers)
        assert_best_closing_time(result, expected)
