import pytest

from leetcode_py import logged_test

from .helpers import assert_two_sum, run_two_sum
from .solution import Solution


class TestTwoSumIIInputArrayIsSorted:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "numbers, target, expected",
        [
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
            ([1, 2, 3, 4, 5], 9, [4, 5]),
            ([1, 2, 3, 4, 5], 3, [1, 2]),
            ([0, 0, 3, 4], 0, [1, 2]),
            ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),
            ([5, 25, 75], 100, [2, 3]),
            ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
            ([1, 2], 3, [1, 2]),
            ([-5, -3, -1, 0, 2, 4], -4, [2, 3]),
            ([-1000, 0, 1, 1000], 0, [1, 4]),
            ([2, 7, 11, 15], 26, [3, 4]),
            ([1, 4, 6, 8, 10, 14], 10, [2, 3]),
        ],
    )
    def test_two_sum(self, numbers: list[int], target: int, expected: list[int]):
        result = run_two_sum(Solution, numbers, target)
        assert_two_sum(result, expected)
