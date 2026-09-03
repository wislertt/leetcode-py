import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum_multiplicity, run_three_sum_multiplicity
from .solution import Solution


class TestThreeSumMultiplicity:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, target, expected",
        [
            ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
            ([1, 1, 2, 2, 2, 2], 5, 12),
            ([2, 1, 3], 6, 1),
            ([0, 0, 0], 0, 1),
            ([0, 0, 0, 0], 0, 4),
            ([1, 1, 1], 3, 1),
            ([1, 1, 1, 1], 3, 4),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 120),
            ([1, 2, 3], 7, 0),
            ([0, 1, 2], 3, 1),
            ([5, 5, 5, 5, 5], 15, 10),
            ([0, 0, 1, 1, 2, 2], 3, 8),
            ([100, 100, 100], 300, 1),
            ([0, 0, 0], 300, 0),
            ([1, 1, 2, 2, 2], 5, 6),
            ([1, 2, 3, 4, 5], 9, 2),
            ([3, 3, 3, 6, 6], 12, 6),
            ([0, 100, 50], 150, 1),
            ([3, 1, 4, 2, 4, 5, 6, 4, 6], 10, 9),
            ([5, 3, 0], 1, 0),
            ([5, 6, 6, 3, 3, 6, 1, 3, 5], 3, 0),
            ([6, 4, 0, 3, 5, 3, 3, 3, 0], 8, 8),
        ],
    )
    def test_three_sum_multiplicity(self, arr: list[int], target: int, expected: int):
        result = run_three_sum_multiplicity(Solution, arr, target)
        assert_three_sum_multiplicity(result, expected)
