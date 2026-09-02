import pytest

from leetcode_py import logged_test

from .helpers import assert_summary_ranges, run_summary_ranges
from .solution import Solution


class TestSummaryRanges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
            ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
            ([], []),
            ([0], ["0"]),
            ([-1], ["-1"]),
            ([1, 2], ["1->2"]),
            ([1, 3], ["1", "3"]),
            ([-1, 0], ["-1->0"]),
            ([-2, -1, 1, 2], ["-2->-1", "1->2"]),
            ([-3, -2, -1], ["-3->-1"]),
            ([-2147483648, 2147483647], ["-2147483648", "2147483647"]),
            ([1, 2, 3, 4, 5], ["1->5"]),
            ([7, 8, 9, 10], ["7->10"]),
            ([-12, 19, 33], ["-12", "19", "33"]),
            ([-31, -24, -22, -1, 12, 34, 36], ["-31", "-24", "-22", "-1", "12", "34", "36"]),
            ([-15, 11, 32, 36, 40], ["-15", "11", "32", "36", "40"]),
            ([32], ["32"]),
            ([-31, -9, -8, 3, 12, 15, 23, 37], ["-31", "-9->-8", "3", "12", "15", "23", "37"]),
            ([-32, -14, -6, 2, 3, 17], ["-32", "-14", "-6", "2->3", "17"]),
            ([-4], ["-4"]),
            ([-23, -2, 7, 27], ["-23", "-2", "7", "27"]),
        ],
    )
    def test_summary_ranges(self, nums: list[int], expected: list[str]):
        result = run_summary_ranges(Solution, nums)
        assert_summary_ranges(result, expected)
