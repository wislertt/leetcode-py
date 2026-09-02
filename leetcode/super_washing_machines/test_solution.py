import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min_moves, run_find_min_moves
from .solution import Solution


class TestSuperWashingMachines:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "machines, expected",
        [
            ([1, 0, 5], 3),
            ([0, 3, 0], 2),
            ([0, 2, 0], -1),
            ([0, 0, 0], 0),
            ([1], 0),
            ([0, 0, 11, 5], 8),
            ([4, 0, 0, 4], 2),
            ([0, 5, 0, 0, 0], 4),
            ([100000, 0, 0, 0], 75000),
            ([0, 0, 100000, 0, 0], 80000),
            ([9, 1, 8, 2], 4),
            ([4, 1, 1, 2], 2),
            ([4, 1, 2, 1], 2),
            ([1, 1, 3], -1),
            ([2, 4, 4, 2], 1),
            ([4, 1, 2], -1),
            ([4, 3, 0, 2], -1),
        ],
    )
    def test_find_min_moves(self, machines: list[int], expected: int):
        result = run_find_min_moves(Solution, machines)
        assert_find_min_moves(result, expected)
