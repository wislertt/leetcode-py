import pytest

from leetcode_py import logged_test

from .helpers import assert_num_components, run_num_components
from .solution import Solution


class TestLinkedListComponents:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, nums, expected",
        [
            ([0, 1, 2, 3], [0, 1, 3], 2),
            ([0, 1, 2, 3, 4], [0, 3, 1, 4], 2),
            ([0], [0], 1),
            ([0, 1], [0], 1),
            ([0, 1], [1], 1),
            ([0, 1], [0, 1], 1),
            ([0, 1, 2, 3], [1, 3], 2),
            ([3, 0, 1, 2], [0, 1, 2], 1),
            ([1, 0, 2], [0], 1),
            ([4, 2, 0, 1, 3], [4, 1], 2),
            ([2, 1, 0, 3], [0, 3, 1], 1),
            ([0, 1, 4, 2, 3], [3, 4, 0, 1], 2),
            ([7, 1, 0, 3, 5, 6, 4, 2], [0, 6, 7, 5, 4], 3),
            ([3, 1, 0, 2], [2], 1),
            ([0, 2, 1, 8, 3, 7, 6, 5, 4], [8, 5, 6, 0, 7, 2, 3, 4], 2),
            ([1, 0, 2], [1, 2, 0], 1),
        ],
    )
    def test_num_components(self, head_vals: list[int], nums: list[int], expected: int):
        result = run_num_components(Solution, head_vals, nums)
        assert_num_components(result, expected)
