import pytest

from leetcode_py import logged_test

from .helpers import assert_find_root, run_find_root
from .solution import Solution


class TestFindRootOfNAryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list",
        [
            ([1, None, 3, 2, 4, None, 5, 6]),
            (
                [
                    1,
                    None,
                    2,
                    3,
                    4,
                    5,
                    None,
                    None,
                    6,
                    7,
                    None,
                    8,
                    None,
                    9,
                    10,
                    None,
                    None,
                    11,
                    None,
                    12,
                    None,
                    13,
                    None,
                    None,
                    14,
                ]
            ),
            ([1]),
            ([10]),
            ([999]),
            ([1, None, 2]),
            ([3, None, 7]),
            ([1, None, 2, None, 3, None, 4, None, 5, None, 6]),
            ([2, None, 1, None, 3, None, 4, None, 5]),
            ([5, None, 9, None, 1, None, 8]),
            ([1, None, 2, 3, 4, 5, 6]),
            ([100, None, 200, 300, None, 400, 500, 600]),
            ([7, None, 3, 9, 1, None, None, 4, None, 2]),
            ([9, None, 8, 7, 6, 5, 4, 3, 2, 1]),
            ([10, None, 1, 2, 3, None, None, 4, 5, None, 6, 7, 8, 9]),
            ([4, None, 2, 6, None, None, 1, 5, 7]),
            ([50, None, 25, None, 75, None, 12, None, 88]),
            ([492, None, 592, 833, 958]),
            (
                [
                    822,
                    None,
                    381,
                    525,
                    None,
                    634,
                    48,
                    None,
                    None,
                    723,
                    414,
                    32,
                    346,
                    None,
                    382,
                    None,
                    None,
                    None,
                    None,
                    None,
                    883,
                ]
            ),
            ([192, None, 902, None, 406, 122, None, 420, 752, None, 262, 39]),
            ([621, None, 838]),
            (
                [
                    208,
                    None,
                    63,
                    145,
                    147,
                    470,
                    None,
                    223,
                    250,
                    773,
                    None,
                    598,
                    None,
                    929,
                    None,
                    21,
                    None,
                    367,
                    16,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    576,
                ]
            ),
            ([807, None, 591, 444, None, 994, None, 743, None, 997, 990, 434, None, 430]),
            ([644, None, 398, 671, 676, None, 613, None, 982, 110]),
            (
                [
                    252,
                    None,
                    732,
                    672,
                    147,
                    475,
                    None,
                    None,
                    703,
                    None,
                    None,
                    None,
                    476,
                    451,
                    None,
                    None,
                    894,
                ]
            ),
            ([265, None, 106, None, 226, 448, None, 902, 592, 414]),
            ([860, None, 700, 644, None, 833, 608]),
            ([795, None, 997, None, 512]),
            ([514, None, 125, None, 563, 661]),
        ],
    )
    def test_find_root(self, root_list: list[int | None]):
        result = run_find_root(Solution, root_list)
        assert_find_root(result, root_list)
