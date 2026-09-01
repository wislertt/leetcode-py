import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_number, run_smallest_number
from .solution import Solution


class TestConstructSmallestNumberFromDiString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pattern, expected",
        [
            ("D", "21"),
            ("I", "12"),
            ("DD", "321"),
            ("DI", "213"),
            ("ID", "132"),
            ("II", "123"),
            ("DDD", "4321"),
            ("DID", "2143"),
            ("IDI", "1324"),
            ("DDDD", "54321"),
            ("IDID", "13254"),
            ("IIID", "12354"),
            ("IIII", "12345"),
            ("IDDII", "143256"),
            ("IIDDD", "126543"),
            ("DDDIID", "4321576"),
            ("IIDDID", "1254376"),
            ("IIIDIDDD", "123549876"),
        ],
    )
    def test_smallest_number(self, pattern: str, expected: str):
        result = run_smallest_number(Solution, pattern)
        assert_smallest_number(result, expected)
