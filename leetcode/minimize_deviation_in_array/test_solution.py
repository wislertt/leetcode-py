import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_deviation, run_minimum_deviation
from .solution import Solution


class TestMinimizeDeviationInArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], 1),
            ([4, 1, 5, 20, 3], 3),
            ([2, 10, 8], 3),
            ([1, 2], 0),
            ([2, 1], 0),
            ([3, 5], 1),
            ([4, 8], 0),
            ([1, 1000000000], 1953123),
            ([1, 100000000], 390623),
            ([2, 3], 1),
            ([6, 3], 0),
            ([7, 7, 7], 0),
            ([14, 28, 56], 0),
            ([3, 6, 12], 0),
            ([5, 10, 20, 40], 0),
            ([10, 6], 1),
            ([9, 4, 1, 7], 7),
            ([28, 8, 16, 1], 5),
            ([50, 50, 51], 1),
            ([9, 41, 35, 45], 27),
            ([39, 25, 50, 20], 19),
            ([9, 26, 54, 38, 29], 11),
            ([32, 57, 52, 9, 12], 45),
            ([36, 36, 24, 26], 4),
            ([48, 31, 8, 57], 49),
            ([20, 37], 17),
            ([24, 8, 44, 36], 4),
            ([15, 12, 42, 27], 15),
            ([45, 52, 45, 47], 7),
            ([22, 44], 0),
            ([34, 57, 39, 4, 21], 53),
            ([56, 49, 56, 22, 25], 27),
            ([44, 58, 17], 12),
            ([9, 35, 20, 4], 31),
            ([1, 42, 6, 15, 2], 19),
            ([4, 37], 33),
            ([24, 30], 3),
            ([19, 30, 42, 17], 6),
            ([58, 7, 1], 27),
            ([58, 46, 41, 22], 19),
            ([8, 53], 45),
            ([21, 16, 25, 54], 11),
            ([1000000000, 999999999], 1),
            ([536870912, 1], 0),
            ([3, 1000000000, 2], 1953123),
        ],
    )
    def test_minimum_deviation(self, nums: list[int], expected: int):
        result = run_minimum_deviation(Solution, nums)
        assert_minimum_deviation(result, expected)
