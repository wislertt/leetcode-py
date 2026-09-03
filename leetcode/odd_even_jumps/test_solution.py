import pytest

from leetcode_py import logged_test

from .helpers import assert_odd_even_jumps, run_odd_even_jumps
from .solution import Solution


class TestOddEvenJump:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([10, 13, 12, 14, 15], 2),
            ([2, 3, 1, 1, 4], 3),
            ([5, 1, 3, 4, 2], 3),
            ([7], 1),
            ([1, 2], 2),
            ([2, 1], 1),
            ([5, 5, 5, 5], 4),
            ([1, 2, 3, 4, 5], 2),
            ([5, 4, 3, 2, 1], 1),
            ([3, 3, 3, 3, 3], 5),
            ([10, 10, 11, 11, 12], 3),
            ([9, 1, 8, 2, 7, 3], 2),
            ([1, 5, 2, 4, 3, 5, 1], 6),
            ([14, 3, 19, 3, 17, 20], 3),
            ([2, 2, 2, 1, 1, 1], 4),
            ([0, 9, 8, 0, 4, 1], 2),
        ],
    )
    def test_odd_even_jumps(self, arr: list[int], expected: int):
        result = run_odd_even_jumps(Solution, arr)
        assert_odd_even_jumps(result, expected)
