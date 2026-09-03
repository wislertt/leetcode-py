import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_subseq_widths, run_sum_subseq_widths
from .solution import Solution


class TestSumOfSubseqWidths:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 1, 3], 6),
            ([2], 0),
            ([1, 2], 1),
            ([2, 1], 1),
            ([5, 5, 5], 0),
            ([1, 2, 3], 6),
            ([3, 2, 1], 6),
            ([1, 3, 2], 6),
            ([1, 1, 2], 3),
            ([2, 2, 1], 3),
            ([1, 100000], 99999),
            ([100000, 1], 99999),
            ([1, 2, 4, 8, 16], 261),
            ([100000, 99999, 99999, 99999, 100000, 99999, 100000, 100000, 100000], 465),
            ([9, 10, 7, 10, 9, 6, 8, 6], 820),
            ([7, 2, 4, 1], 46),
            ([4, 4, 1, 1, 4], 63),
            ([6, 3, 2, 7, 2, 6, 5], 471),
            ([100000, 100000, 100000, 99999, 99999], 21),
            ([1, 1, 5, 5, 7], 114),
        ],
    )
    def test_sum_subseq_widths(self, nums: list[int], expected: int):
        result = run_sum_subseq_widths(Solution, nums)
        assert_sum_subseq_widths(result, expected)
