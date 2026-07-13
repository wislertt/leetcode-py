import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_number, run_largest_number
from .solution import Solution


class TestLargestNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([10, 2], "210"),
            ([3, 30, 34, 5, 9], "9534330"),
            ([0, 0], "0"),
            ([0], "0"),
            ([1], "1"),
            ([1, 2, 3], "321"),
            ([20, 1], "201"),
            ([121, 12], "12121"),
            ([12, 121], "12121"),
            ([9, 90, 9], "9990"),
            ([0, 0, 0, 0], "0"),
            ([1, 0, 0], "100"),
            ([3, 30, 3], "3330"),
            ([999999991, 9], "9999999991"),
            ([432, 43243], "43243432"),
            ([818, 81], "81881"),
        ],
    )
    def test_largest_number(self, nums: list[int], expected: str):
        result = run_largest_number(Solution, nums)
        assert_largest_number(result, expected)
