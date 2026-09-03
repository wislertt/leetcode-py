import pytest

from leetcode_py import logged_test

from .helpers import assert_count_triplets, run_count_triplets
from .solution import Solution


class TestTriplesWithBitwiseAndEqualToZero:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 1, 3], 12),
            ([0, 0, 0], 27),
            ([0], 1),
            ([1], 0),
            ([65535], 0),
            ([1, 2], 6),
            ([0, 1], 7),
            ([65535, 65535, 65535], 0),
            ([3, 5], 0),
            ([1, 1, 1], 0),
            ([2, 2, 2], 0),
            ([1, 2, 4], 24),
            ([7, 7, 0], 19),
            ([1, 3, 7, 0], 37),
            ([5, 10, 20, 40], 48),
            ([15, 0, 15], 19),
            ([81, 371, 553, 265, 864], 18),
            ([529, 831, 305, 1012, 669, 183, 571, 117, 375], 0),
            ([148, 550, 34, 181, 533, 171], 72),
            ([455, 136, 541, 249, 929, 23, 694], 60),
            ([855, 548, 264, 88, 488, 224, 330], 138),
            ([103, 370, 413, 638, 624], 12),
        ],
    )
    def test_count_triplets(self, nums: list[int], expected: int):
        result = run_count_triplets(Solution, nums)
        assert_count_triplets(result, expected)
