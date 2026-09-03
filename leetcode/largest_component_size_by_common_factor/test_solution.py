import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_component_size, run_largest_component_size
from .solution import Solution


class TestLargestComponentSizeByCommonFactor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 6, 15, 35], 4),
            ([20, 50, 9, 63], 2),
            ([2, 3, 6, 7, 4, 12, 21, 39], 8),
            ([1], 1),
            ([2], 1),
            ([1, 2, 3, 4, 5, 6, 7], 4),
            ([11, 13, 17, 19], 1),
            ([6, 10, 15], 3),
            ([5, 7, 35, 11, 77], 5),
            ([2, 4, 8, 16], 4),
            ([3, 5, 7, 15, 21, 35], 6),
            ([100000, 99999], 1),
            ([99991, 100000], 1),
            ([8, 27, 125, 9, 49], 2),
            ([12, 18, 25, 49, 121, 169], 2),
            ([81, 146, 33, 165, 178], 3),
            ([111, 138, 84, 130], 4),
            ([133, 112, 107, 109, 86, 57, 154], 5),
            ([83, 184, 15, 111, 100, 191, 48, 44], 6),
            ([83, 158, 58, 60, 147, 109, 53], 4),
            ([188, 166, 34, 18, 40, 68, 129, 186, 49, 88, 97], 9),
        ],
    )
    def test_largest_component_size(self, nums: list[int], expected: int):
        result = run_largest_component_size(Solution, nums)
        assert_largest_component_size(result, expected)
