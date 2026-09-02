import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_nodes, run_merge_nodes
from .solution import Solution


class TestMergeNodesInBetweenZeros:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, expected_vals",
        [
            ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
            ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]),
            ([0, 5, 0], [5]),
            ([0, 1, 2, 3, 4, 0], [10]),
            ([0, 1000, 0, 1000, 0], [1000, 1000]),
            ([0, 10, 20, 30, 0, 40, 50, 60, 0], [60, 150]),
            ([0, 1, 1, 1, 1, 0], [4]),
            ([0, 7, 0, 8, 0, 9, 0], [7, 8, 9]),
            ([0, 2, 0, 1, 0, 3, 0, 4, 0, 5, 0], [2, 1, 3, 4, 5]),
            ([0, 999, 0, 1000, 0], [999, 1000]),
            ([0, 4, 3, 2, 1, 0, 1, 2, 3, 4, 0], [10, 10]),
            ([0, 12, 0, 34, 0, 56, 0], [12, 34, 56]),
            ([0, 100, 0, 200, 0, 300, 0, 400, 0], [100, 200, 300, 400]),
            ([0, 1, 0, 2, 3, 0], [1, 5]),
            ([0, 1000, 999, 0, 1, 0], [1999, 1]),
            ([0, 98, 76, 4, 9, 0, 20, 61, 2, 0], [187, 83]),
            ([0, 53, 75, 54, 0, 21, 35, 0, 10, 76, 33, 1, 0], [182, 56, 120]),
            ([0, 78, 11, 44, 0], [133]),
            ([0, 60, 87, 0], [147]),
            ([0, 16, 41, 69, 0, 79, 70, 0, 100, 0, 35, 0], [126, 149, 100, 35]),
        ],
    )
    def test_merge_nodes(self, head_vals: list[int], expected_vals: list[int]):
        result = run_merge_nodes(Solution, head_vals)
        assert_merge_nodes(result, expected_vals)
