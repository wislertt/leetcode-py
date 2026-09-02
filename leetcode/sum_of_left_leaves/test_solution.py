import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_of_left_leaves, run_sum_of_left_leaves
from .solution import Solution


class TestSumOfLeftLeaves:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], 24),
            ([1], 0),
            ([1, 2], 2),
            ([1, None, 2], 0),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4, 5], 4),
            ([1, 2, 3, None, 4, None, 5], 0),
            ([4, 9, 5, None, 7], 0),
            ([10, 5, 15, 3, 7, None, 20], 3),
            ([-2, -3, 4], -3),
            ([0, 0, 0, 0], 0),
            ([100, -100, 200, 50], 50),
            ([-50, 37, -48, -8, 35, -39], -47),
            ([-28, 45, -34, -26, 45], -26),
            ([19, -41, 47, -30, -1], -30),
            ([39, -9, -18, 3], 3),
            ([-23, 5, -32, -25, 8, 11], -14),
            ([-36, 25, -45, 36], 36),
        ],
    )
    def test_sum_of_left_leaves(self, root_list: list[int | None], expected: int):
        result = run_sum_of_left_leaves(Solution, root_list)
        assert_sum_of_left_leaves(result, expected)
