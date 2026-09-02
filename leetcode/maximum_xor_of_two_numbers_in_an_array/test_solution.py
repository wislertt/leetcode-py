import pytest

from leetcode_py import logged_test

from .helpers import assert_find_maximum_xor, run_find_maximum_xor
from .solution import Solution


class TestMaximumXorOfTwoNumbersInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 10, 5, 25, 2, 8], 28),
            ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),
            ([1], 0),
            ([0], 0),
            ([0, 0], 0),
            ([2, 4], 6),
            ([8, 10, 2], 10),
            ([1, 2, 3, 4], 7),
            ([5, 5, 5, 5], 0),
            ([1, 1, 1], 0),
            ([2147483647, 0], 2147483647),
            ([2147483647, 2147483646], 1),
            ([4, 6, 7, 11, 25, 66, 70, 81, 88, 92], 95),
            ([12, 3, 19, 7, 14, 8], 31),
            ([1000000000, 999999999, 1], 1000000001),
            ([65536, 65535, 131071, 1], 131071),
            ([63, 8, 14, 7, 3, 0], 63),
            ([80, 15, 14, 38, 0, 6, 4], 118),
            ([5, 46, 15], 43),
            ([14, 41, 2, 9, 6, 3, 5], 47),
        ],
    )
    def test_find_maximum_xor(self, nums: list[int], expected: int):
        result = run_find_maximum_xor(Solution, nums)
        assert_find_maximum_xor(result, expected)
