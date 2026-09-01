import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_odd_number, run_largest_odd_number
from .solution import Solution


class TestLargestOddNumberInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            ("52", "5"),
            ("4206", ""),
            ("35427", "35427"),
            ("7", "7"),
            ("8", ""),
            ("2468", ""),
            ("13579", "13579"),
            ("101", "101"),
            ("234", "23"),
            ("999", "999"),
            ("1000", "1"),
            ("0", ""),
            ("1234567890", "123456789"),
            ("987654321", "987654321"),
            ("20", ""),
            ("354270000000000000000000000000", "35427"),
        ],
    )
    def test_largest_odd_number(self, num: str, expected: str):
        result = run_largest_odd_number(Solution, num)
        assert_largest_odd_number(result, expected)
