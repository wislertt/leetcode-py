import pytest

from leetcode_py import logged_test

from .helpers import assert_rearrange_array, run_rearrange_array
from .solution import Solution


class TestArrayWithElementsNotEqualToAverageOfNeighbors:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([6, 2, 0, 9, 7], [6, 2, 0, 9, 7]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [3, 2, 1]),
            ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
            ([0, 100000, 50000], [0, 100000, 50000]),
            ([1, 3, 2, 4], [1, 3, 2, 4]),
            ([2, 4, 6, 8, 10, 12], [2, 4, 6, 8, 10, 12]),
            ([7, 1, 5, 3, 9], [7, 1, 5, 3, 9]),
            ([10, 20, 30], [10, 20, 30]),
            ([4, 1, 3, 2, 5, 0], [4, 1, 3, 2, 5, 0]),
            ([100, 200, 300, 400, 500, 600, 700], [100, 200, 300, 400, 500, 600, 700]),
            ([1, 16, 13, 3], [1, 16, 13, 3]),
            ([4, 8, 10, 2], [4, 8, 10, 2]),
            ([1, 10, 9, 20], [1, 10, 9, 20]),
            ([20, 9, 0, 1, 18, 19], [20, 9, 0, 1, 18, 19]),
        ],
    )
    def test_rearrange_array(self, nums: list[int], expected: list[int]):
        result = run_rearrange_array(Solution, nums)
        assert_rearrange_array(result, expected)
