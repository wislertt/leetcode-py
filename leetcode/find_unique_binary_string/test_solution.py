import pytest

from leetcode_py import logged_test

from .helpers import assert_find_unique_binary_string, run_find_unique_binary_string
from .solution import Solution


class TestFindUniqueBinaryString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            (["01", "10"], "11"),
            (["00", "01"], "11"),
            (["111", "011", "001"], "101"),
            (["0"], "1"),
            (["1"], "0"),
            (["00", "11"], "01"),
            (["010", "110", "001"], "100"),
            (["0000", "1111", "0101", "1010"], "1011"),
            (["00000", "00001", "00010", "00100", "01000"], "11111"),
            (["111111", "000000", "010101", "101010", "011001", "100110"], "011111"),
            (["11011", "00100", "01000", "11010", "00111"], "01100"),
            (["00000", "10000", "10001", "00101", "00001"], "11110"),
            (["10010", "10000", "01011", "11111", "11100"], "01101"),
            (["01101", "00111", "01011", "00101", "11100"], "11111"),
            (["1010", "1001", "0100", "1100"], "0111"),
            (["00101", "11100", "01001", "00010", "01111"], "10100"),
            (["11000", "11100", "00001", "10011", "00000"], "00101"),
            (["0011", "0111", "1001", "0101"], "1010"),
            (["1001", "1000", "0000", "1100"], "0111"),
            (["0110", "0001", "0000", "0111"], "1110"),
        ],
    )
    def test_find_unique_binary_string(self, nums: list[str], expected: str):
        result = run_find_unique_binary_string(Solution, nums)
        assert_find_unique_binary_string(result, expected)
        assert result not in nums
