import pytest

from leetcode_py import logged_test

from .helpers import assert_max_depth, run_max_depth
from .solution import Solution


class TestMaximumDepthOfNAryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1], 1),
            ([], 0),
            ([1, None, 3, 2, 4, None, 5, 6], 3),
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
                ],
                5,
            ),
            ([1, None, 2], 2),
            ([1, None, 2, 3], 2),
            ([1, None, 2, None, 3], 3),
            ([1, None, 2, None, 3, None, 4], 4),
            ([1, None, 2, None, 3, None, 4, None, 5], 5),
            ([1, None, 2, None, 3, None, 4, None, 5, None, 6], 6),
            ([5, None, 4, None, 2, None, 3, 1], 4),
            ([1, None, 10, 2, None, 20, 30, 40], 3),
            ([1, None, 2, 3, 4, 5], 2),
            ([20, None], 1),
            ([11, None, 17, 3, None, 5, None, None, 15, 14, None, 5, 1, None, None, None, 17], 6),
            ([17, None], 1),
            (
                [12, None, 4, 20, None, 5, 19, None, None, 7, 2, None, None, 13, 10, None, None, 7],
                6,
            ),
            ([11, None, 11], 2),
            ([2, None], 1),
            ([12, None, 8, None, 14, 5], 3),
        ],
    )
    def test_max_depth(self, root_list: list[int | None], expected: int):
        result = run_max_depth(Solution, root_list)
        assert_max_depth(result, expected)
