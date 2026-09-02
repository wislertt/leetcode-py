import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_largest_number, run_kth_largest_number
from .solution import Solution


class TestKthLargestNumberInArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            (["3", "6", "7", "10"], 4, "3"),
            (["2", "21", "12", "1"], 3, "2"),
            (["0", "0"], 2, "0"),
            (["1"], 1, "1"),
            (["0"], 1, "0"),
            (["9", "10", "100"], 1, "100"),
            (["100", "10", "9"], 3, "9"),
            (["11", "12", "13"], 2, "12"),
            (["5", "5", "5"], 2, "5"),
            (["10", "6", "100", "100"], 2, "100"),
            (["123456789012345678901234567890", "1"], 1, "123456789012345678901234567890"),
            (["12345678901234567890", "987654321098765432109", "5"], 2, "12345678901234567890"),
            (["7", "3", "8", "1", "9"], 1, "9"),
            (["7", "3", "8", "1", "9"], 5, "1"),
            (["0", "0", "0"], 1, "0"),
            (["100000000", "1000000000", "10000000"], 2, "100000000"),
            (["48", "49", "50", "51"], 3, "49"),
            (["99", "100", "101", "999"], 4, "99"),
        ],
    )
    def test_kth_largest_number(self, nums: list[str], k: int, expected: str):
        result = run_kth_largest_number(Solution, nums, k)
        assert_kth_largest_number(result, expected)
