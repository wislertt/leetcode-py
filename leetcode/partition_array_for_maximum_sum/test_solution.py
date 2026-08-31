import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sum_after_partitioning, run_max_sum_after_partitioning
from .solution import Solution


class TestPartitionArrayForMaximumSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, expected",
        [
            ([1, 15, 7, 9, 2, 5, 10], 3, 84),
            ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4, 83),
            ([1], 1, 1),
            ([1, 2], 2, 4),
            ([1, 2], 1, 3),
            ([9, 9, 9], 1, 27),
            ([0, 0], 2, 0),
            ([1, 2, 3, 4, 5], 2, 17),
            ([10, 1, 10, 1, 10], 2, 50),
            ([7, 2, 4], 2, 18),
            ([1, 3, 2, 4, 6, 5], 3, 29),
            ([8, 8, 1, 2, 8, 8], 3, 48),
        ],
    )
    def test_max_sum_after_partitioning(self, arr: list[int], k: int, expected: int):
        result = run_max_sum_after_partitioning(Solution, arr, k)
        assert_max_sum_after_partitioning(result, expected)
