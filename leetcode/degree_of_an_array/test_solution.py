import pytest

from leetcode_py import logged_test

from .helpers import assert_find_shortest_sub_array, run_find_shortest_sub_array
from .solution import Solution


class TestDegreeOfAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2, 3, 1], 2),
            ([1, 2, 2, 3, 1, 4, 2], 6),
            ([1], 1),
            ([0], 1),
            ([5, 5, 5, 5], 4),
            ([1, 2, 3, 4, 5], 1),
            ([1, 1, 2, 2], 2),
            ([2, 1, 2, 1, 2], 5),
            ([3, 3, 3, 1, 1, 2], 3),
            ([1, 2, 1, 2, 1, 2], 5),
            ([4, 4, 4, 4, 4, 4], 6),
            ([7, 8, 7, 8, 7], 5),
            ([9, 1, 9, 1, 9, 1, 9], 7),
            ([0, 0, 1, 1, 2, 2], 2),
            ([6, 5, 4, 5, 6], 3),
            ([4, 0, 2], 1),
            ([2, 3], 1),
            ([5, 1, 0, 2, 4], 1),
            ([0, 3, 1, 5, 0, 2, 2, 1, 0], 9),
            ([5, 1, 2, 3, 0, 5, 1], 6),
            ([5, 2, 5], 3),
            ([5, 3, 2, 2, 0, 4, 1, 5], 2),
            ([2, 1], 1),
            ([3, 1, 5, 0, 2, 2, 3, 3, 1], 8),
            ([3, 5, 1, 3, 3, 4], 5),
            ([5, 2, 0, 3, 1, 1, 4, 4], 2),
            ([0, 3, 2, 0, 3, 3, 2, 0, 1], 5),
            ([3, 5, 3, 2, 3, 3, 2, 1], 6),
            ([4, 0, 3, 5], 1),
            ([3, 2, 5, 1], 1),
            ([1, 3, 0, 3, 3, 3, 4], 5),
            ([4, 2, 3, 5, 4], 5),
            ([4, 1, 0, 4, 2], 4),
            ([1, 3], 1),
            ([0, 0, 2, 5, 1], 2),
            ([3, 2, 0, 5, 1, 3, 5], 4),
            ([4, 4, 4, 3, 5, 2, 5, 3], 3),
            ([0, 4, 0, 0, 1], 4),
            ([2, 0], 1),
            ([2, 3, 4, 2, 0, 5, 3, 4], 4),
        ],
    )
    def test_find_shortest_sub_array(self, nums: list[int], expected: int):
        result = run_find_shortest_sub_array(Solution, nums)
        assert_find_shortest_sub_array(result, expected)
