import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_k_digits, run_remove_k_digits
from .solution import Solution


class TestRemoveKDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, k, expected",
        [
            ("1432219", 3, "1219"),
            ("10200", 1, "200"),
            ("10", 2, "0"),
            ("112", 1, "11"),
            ("9", 1, "0"),
            ("10", 1, "0"),
            ("12345", 2, "123"),
            ("54321", 2, "321"),
            ("100", 1, "0"),
            ("10001", 1, "1"),
            ("935", 2, "3"),
            ("112255", 3, "112"),
            ("1234567890", 9, "0"),
            ("99999", 2, "999"),
            ("10234", 1, "234"),
            ("5337", 2, "33"),
            ("1432219", 1, "132219"),
            ("1123581321", 4, "111321"),
            ("100", 2, "0"),
            ("0", 1, "0"),
            ("12", 2, "0"),
            ("1111111", 3, "1111"),
        ],
    )
    def test_remove_k_digits(self, num: str, k: int, expected: str):
        result = run_remove_k_digits(Solution, num, k)
        assert_remove_k_digits(result, expected)
