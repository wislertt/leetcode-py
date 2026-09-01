import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_good_integer, run_largest_good_integer
from .solution import Solution


class TestLargest3SameDigitNumberInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            ("6777133339", "777"),
            ("2300019", "000"),
            ("42352338", ""),
            ("999", "999"),
            ("000", "000"),
            ("111222", "222"),
            ("222111", "222"),
            ("123456", ""),
            ("112233", ""),
            ("777123777", "777"),
            ("8888", "888"),
            ("1000", "000"),
            ("909999", "999"),
            ("121212", ""),
            ("555333444", "555"),
            ("999000", "999"),
            ("7777", "777"),
            ("0011002", ""),
            ("77777777777777777777777777777777777777777", "777"),
            ("123456789012345678901234567890999", "999"),
        ],
    )
    def test_largest_good_integer(self, num: str, expected: str):
        result = run_largest_good_integer(Solution, num)
        assert_largest_good_integer(result, expected)
