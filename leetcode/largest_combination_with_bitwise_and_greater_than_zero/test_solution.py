import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_combination, run_largest_combination
from .solution import Solution


class TestLargestCombinationWithBitwiseAndGreaterThanZero:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "candidates, expected",
        [
            ([16, 17, 71, 62, 12, 24, 14], 4),
            ([8, 8], 2),
            ([1], 1),
            ([7], 1),
            ([2, 3], 2),
            ([2, 2], 2),
            ([1, 2, 4, 8], 1),
            ([3, 3, 3], 3),
            ([5, 6, 7, 8, 9], 3),
            ([16, 16, 16, 1], 3),
            ([1048576, 1048576, 1048577], 3),
            ([10000000], 1),
            ([10000000, 10000000, 9999999], 3),
            ([67, 66, 65, 64, 3], 4),
            ([12, 12, 1, 1], 2),
            ([1000000, 999999, 999998, 1000000], 4),
            ([48, 2, 1, 5398006, 3], 3),
            ([1, 3, 2960204, 2, 33], 3),
            ([1, 3, 5753392, 2, 1, 1], 4),
            ([8952585, 3, 1], 3),
            ([2, 67, 3, 1710510], 4),
            ([7852437, 68, 4282524], 3),
            ([3, 1356083, 8391756, 1, 1], 4),
            ([8550141, 1, 69, 1, 1833520, 2], 4),
        ],
    )
    def test_largest_combination(self, candidates: list[int], expected: int):
        result = run_largest_combination(Solution, candidates)
        assert_largest_combination(result, expected)
