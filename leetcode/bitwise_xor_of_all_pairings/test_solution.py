import pytest

from leetcode_py import logged_test

from .helpers import assert_xor_all_nums, run_xor_all_nums
from .solution import Solution


class TestBitwiseXorOfAllPairings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([2, 1, 3], [10, 2, 5, 0], 13),
            ([1, 2], [3, 4], 0),
            ([1], [2], 3),
            ([0], [0], 0),
            ([5], [5], 0),
            ([1], [1, 2, 3], 1),
            ([1, 2, 3], [1], 1),
            ([1, 2], [3, 4, 5], 3),
            ([7], [7], 0),
            ([0, 0, 0], [0, 0], 0),
            ([1, 1, 1, 1], [2, 2], 0),
            ([1000000000, 0], [1000000000, 1000000000], 0),
            ([1000000000, 999999999], [123456789], 1023),
            ([536870911, 536870912], [1], 1073741823),
            ([1], [1000000000, 999999999], 1023),
            ([962, 286, 783], [317, 19, 170], 87),
            ([607, 344, 456, 268], [408, 973, 623, 492, 937], 963),
            ([259, 921], [587, 446, 858, 10], 0),
            ([497, 960, 590, 758, 4], [967, 933, 849], 446),
            ([145, 527, 489], [125, 599], 554),
            ([686, 751, 318, 164, 843, 606], [732, 273, 104, 729, 560, 980], 0),
        ],
    )
    def test_xor_all_nums(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_xor_all_nums(Solution, nums1, nums2)
        assert_xor_all_nums(result, expected)
