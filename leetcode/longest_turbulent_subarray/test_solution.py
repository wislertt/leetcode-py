import pytest

from leetcode_py import logged_test

from .helpers import assert_max_turbulence_size, run_max_turbulence_size
from .solution import Solution


class TestLongestTurbulentSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
            ([4, 8, 12, 16], 2),
            ([100], 1),
            ([1, 1], 1),
            ([1, 2], 2),
            ([2, 1], 2),
            ([1, 2, 1], 3),
            ([1, 2, 1, 2], 4),
            ([1, 2, 3, 2, 1], 3),
            ([9, 9], 1),
            ([0, 1, 1, 0, 1, 0, 1, 1, 0, 0], 5),
            ([100, 100, 100], 1),
            ([1, 2, 3], 2),
            ([3, 2, 1], 2),
            ([4, 5, 4, 5, 4, 5], 6),
            ([0, 0], 1),
            ([1, 2, 3, 4, 5], 2),
            ([10, 20, 10, 20, 10, 20, 10, 20], 8),
        ],
    )
    def test_max_turbulence_size(self, arr: list[int], expected: int):
        result = run_max_turbulence_size(Solution, arr)
        assert_max_turbulence_size(result, expected)
