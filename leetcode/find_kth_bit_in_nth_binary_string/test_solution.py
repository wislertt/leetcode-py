import pytest

from leetcode_py import logged_test

from .helpers import assert_find_kth_bit, run_find_kth_bit
from .solution import Solution


class TestFindKthBitInNthBinaryString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (3, 1, "0"),
            (4, 11, "1"),
            (1, 1, "0"),
            (2, 1, "0"),
            (2, 3, "1"),
            (3, 3, "1"),
            (3, 7, "1"),
            (4, 1, "0"),
            (4, 8, "1"),
            (4, 15, "1"),
            (5, 16, "1"),
            (10, 1, "0"),
            (10, 513, "0"),
            (10, 1023, "1"),
            (20, 1048575, "1"),
            (20, 1, "0"),
            (7, 44, "0"),
            (8, 40, "1"),
        ],
    )
    def test_find_kth_bit(self, n: int, k: int, expected: str):
        result = run_find_kth_bit(Solution, n, k)
        assert_find_kth_bit(result, expected)
