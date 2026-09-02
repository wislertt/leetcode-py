import pytest

from leetcode_py import logged_test

from .helpers import assert_count_bad_pairs, run_count_bad_pairs
from .solution import Solution


class TestCountNumberOfBadPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 1, 3, 3], 5),
            ([1, 2, 3, 4, 5], 0),
            ([1], 0),
            ([1, 2], 0),
            ([1, 3], 1),
            ([3, 3, 3], 3),
            ([1, 2, 3, 4], 0),
            ([5, 4, 3, 2, 1], 10),
            ([2, 2, 2], 3),
            ([1000000000, 1], 1),
            ([1, 1, 2, 2, 3, 3], 13),
            ([7, 1, 7, 1, 7], 10),
            ([10, 20, 10, 20, 10, 20], 15),
            ([9, 8, 10, 7, 11, 6], 14),
            ([1, 100, 2, 99, 3, 98, 4], 21),
            ([390065284, 284712645, 463168409, 13835088], 6),
            ([785816186, 237091423, 855758531, 653610779, 966123013, 399555075], 15),
            ([488132343, 593784099], 1),
        ],
    )
    def test_count_bad_pairs(self, nums: list[int], expected: int):
        result = run_count_bad_pairs(Solution, nums)
        assert_count_bad_pairs(result, expected)
