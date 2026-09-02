import pytest

from leetcode_py import logged_test

from .helpers import assert_lexicographically_smallest_array, run_lexicographically_smallest_array
from .solution import Solution


class TestMakeLexicographicallySmallestArrayBySwappingElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, limit, expected",
        [
            ([1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]),
            ([1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]),
            ([1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]),
            ([1], 5, [1]),
            ([5, 5, 5, 5], 1, [5, 5, 5, 5]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], 1, [1, 2, 3, 4, 5]),
            ([10, 1, 2, 3], 1, [10, 1, 2, 3]),
            ([1, 100, 2, 101, 3], 1, [1, 100, 2, 101, 3]),
            ([1000000000, 1, 999999999], 1, [999999999, 1, 1000000000]),
            ([9, 3, 7, 1], 1000000000, [1, 3, 7, 9]),
            ([4, 3, 2, 1, 8, 7], 2, [1, 2, 3, 4, 7, 8]),
            ([2, 4, 6, 8], 3, [2, 4, 6, 8]),
            ([1, 1000000000, 2], 1, [1, 1000000000, 2]),
            ([7, 1, 11, 3, 5], 2, [1, 3, 11, 5, 7]),
            ([20, 21, 22, 40, 41], 1, [20, 21, 22, 40, 41]),
            ([6, 2, 10, 3, 100, 9], 1, [6, 2, 9, 3, 100, 10]),
            ([3, 8, 7, 6, 12, 4], 2, [3, 4, 6, 7, 12, 8]),
        ],
    )
    def test_lexicographically_smallest_array(
        self, nums: list[int], limit: int, expected: list[int]
    ):
        result = run_lexicographically_smallest_array(Solution, nums, limit)
        assert_lexicographically_smallest_array(result, expected)
