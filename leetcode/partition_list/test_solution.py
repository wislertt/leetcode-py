import pytest

from leetcode_py import logged_test

from .helpers import assert_partition, run_partition
from .solution import Solution


class TestPartitionList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, x, expected_list",
        [
            ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
            ([2, 1], 2, [1, 2]),
            ([], 3, []),
            ([1], 1, [1]),
            ([1], 2, [1]),
            ([2], 1, [2]),
            ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], 3, [2, 1, 5, 4, 3]),
            ([-100, -50, 0, 50, 100], 0, [-100, -50, 0, 50, 100]),
            ([2, 2, 2, 1, 1, 1], 2, [1, 1, 1, 2, 2, 2]),
            ([1, 1, 1], 1, [1, 1, 1]),
            ([3, 3, 3], 2, [3, 3, 3]),
            ([100, -100, 100, -100], 0, [-100, -100, 100, 100]),
            ([1, 4, 3, 2, 5, 2], 6, [1, 4, 3, 2, 5, 2]),
            ([1, 4, 3, 2, 5, 2], -200, [1, 4, 3, 2, 5, 2]),
            ([0, 0, 1, 0], 1, [0, 0, 0, 1]),
        ],
    )
    def test_partition(self, head_list: list[int], x: int, expected_list: list[int]):
        result = run_partition(Solution, head_list, x)
        assert_partition(result, expected_list)
