import pytest

from leetcode_py import logged_test

from .helpers import assert_missing_rolls, run_missing_rolls
from .solution import Solution


class TestFindMissingObservations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rolls, mean, n, expected",
        [
            ([3, 2, 4, 3], 4, 2, [6, 6]),
            ([1, 5, 6], 3, 4, [3, 2, 2, 2]),
            ([1, 2, 3, 4], 6, 4, []),
            ([1], 3, 1, [5]),
            ([6, 6, 6], 1, 2, []),
            ([1], 6, 5, []),
            ([2, 3, 4], 3, 3, [3, 3, 3]),
            ([5, 5, 5, 5], 5, 1, [5]),
            ([1, 2], 6, 3, []),
            ([4, 4], 4, 4, [4, 4, 4, 4]),
            ([6], 1, 1, []),
            ([1, 1, 1, 1, 1], 6, 6, []),
            ([3, 3], 3, 2, [3, 3]),
            ([2, 2, 2, 2, 2, 2], 4, 2, []),
            ([1, 6], 3, 2, [3, 2]),
            ([5], 5, 2, [5, 5]),
            ([1, 2, 3], 2, 3, [2, 2, 2]),
            ([6, 6], 6, 3, [6, 6, 6]),
            ([2, 4, 6], 5, 3, [6, 6, 6]),
            ([1, 1], 3, 4, [4, 4, 4, 4]),
        ],
    )
    def test_missing_rolls(self, rolls: list[int], mean: int, n: int, expected: list[int]):
        result = run_missing_rolls(Solution, rolls, mean, n)
        assert_missing_rolls(result, expected)
