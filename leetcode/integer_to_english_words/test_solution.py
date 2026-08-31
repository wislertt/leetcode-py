import pytest

from leetcode_py import logged_test

from .helpers import assert_number_to_words, run_number_to_words
from .solution import Solution


class TestIntegerToEnglishWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (0, "Zero"),
            (1, "One"),
            (10, "Ten"),
            (11, "Eleven"),
            (13, "Thirteen"),
            (20, "Twenty"),
            (21, "Twenty One"),
            (38, "Thirty Eight"),
            (85, "Eighty Five"),
            (99, "Ninety Nine"),
            (100, "One Hundred"),
            (105, "One Hundred Five"),
            (115, "One Hundred Fifteen"),
            (123, "One Hundred Twenty Three"),
            (678, "Six Hundred Seventy Eight"),
            (999, "Nine Hundred Ninety Nine"),
            (1000, "One Thousand"),
            (1001, "One Thousand One"),
            (1010, "One Thousand Ten"),
            (1100, "One Thousand One Hundred"),
            (1234, "One Thousand Two Hundred Thirty Four"),
            (2345, "Two Thousand Three Hundred Forty Five"),
            (10000, "Ten Thousand"),
            (10001, "Ten Thousand One"),
            (12345, "Twelve Thousand Three Hundred Forty Five"),
            (1000000, "One Million"),
            (1000001, "One Million One"),
            (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
            (100000000, "One Hundred Million"),
            (1000000000, "One Billion"),
            (1000000001, "One Billion One"),
            (1000010000, "One Billion Ten Thousand"),
        ],
    )
    def test_number_to_words(self, num: int, expected: str):
        result = run_number_to_words(Solution, num)
        assert_number_to_words(result, expected)
