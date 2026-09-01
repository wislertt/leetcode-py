import pytest

from leetcode_py import logged_test

from .helpers import assert_pair_sum, run_pair_sum
from .solution import Solution


class TestMaximumTwinSumOfALinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([5, 4, 2, 1], 6),
            ([4, 2, 2, 3], 7),
            ([1, 100000], 100001),
            ([1, 2], 3),
            ([2, 2], 4),
            ([3, 8], 11),
            ([1, 1, 1, 1], 2),
            ([10, 1, 1, 10], 20),
            ([1, 5, 5, 1], 10),
            ([7, 3, 9, 4], 12),
            ([100, 200, 300, 400], 500),
            ([1, 2, 3, 4, 5, 6, 7, 8], 9),
            ([5, 5, 5, 1, 1, 5], 10),
            ([9, 1, 2, 8, 7, 3], 12),
            ([100000, 100000, 1, 1], 100001),
            ([10, 1, 14, 20], 30),
            ([12, 1, 10, 12, 20, 5, 7, 9], 32),
            ([14, 19], 33),
        ],
    )
    def test_pair_sum(self, head_list: list[int], expected: int):
        result = run_pair_sum(Solution, head_list)
        assert_pair_sum(result, expected)
