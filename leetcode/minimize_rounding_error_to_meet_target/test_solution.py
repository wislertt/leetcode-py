import pytest

from leetcode_py import logged_test

from .helpers import assert_minimize_error, run_minimize_error
from .solution import Solution


class TestMinimizeRoundingErrorToMeetTarget:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prices, target, expected",
        [
            (["0.700", "2.800", "4.900"], 8, "1.000"),
            (["1.500", "2.500", "3.500"], 10, "-1"),
            (["1.500", "2.500", "3.500"], 9, "1.500"),
            (["1.500", "2.500", "3.500"], 7, "1.500"),
            (["0.700", "2.800", "4.900"], 6, "2.400"),
            (["0.700", "2.800", "4.900"], 9, "0.600"),
            (["1.000", "2.000", "3.000"], 6, "0.000"),
            (["0.001"], 1, "0.999"),
            (["0.001"], 0, "0.001"),
            (["0.500", "0.500"], 2, "1.000"),
            (["0.500", "0.500"], 0, "1.000"),
            (["2.350", "1.700", "3.200"], 8, "1.150"),
            (["10.000", "0.100", "0.200"], 11, "0.900"),
            (["1.400", "2.400", "3.400"], 7, "1.400"),
            (["0.400", "0.400"], 1, "1.000"),
        ],
    )
    def test_minimize_error(self, prices: list[str], target: int, expected: str):
        result = run_minimize_error(Solution, prices, target)
        assert_minimize_error(result, expected)
