import pytest

from leetcode_py import logged_test

from .helpers import assert_min_depth, run_min_depth
from .solution import Solution


class TestMinimumDepthOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], 2),
            ([2, None, 3, None, 4, None, 5, None, 6], 5),
            ([], 0),
            ([1], 1),
            ([1, 2], 2),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 2),
            ([1, None, 2, None, 3], 3),
            ([1, 2, None, 3], 3),
            ([1, 2, 3, 4, 5], 2),
            ([-100, None, 1000], 2),
            ([1, 2, 3, None, None, None, 4, 5], 2),
            ([886, 930, -353, None, 11], 2),
            ([463, None, -432, None, -226, None, -548, 651, 466, None, None, 484], 5),
            ([800], 1),
            ([921, 754, None, 111, -780, 434, None, 397, None, 574, 473], 4),
            ([-998, 946], 2),
            ([-790, 65, -183, None, -188, None, None, -565, 318, -752, None, -383], 2),
            ([837, None, 311, 740, 182], 3),
            ([687, None, 213, None, -132, -805, None, None, -192, 698], 6),
        ],
    )
    def test_min_depth(self, root_list: list[int | None], expected: int):
        result = run_min_depth(Solution, root_list)
        assert_min_depth(result, expected)
