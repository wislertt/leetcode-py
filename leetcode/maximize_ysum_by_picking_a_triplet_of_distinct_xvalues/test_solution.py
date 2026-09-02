import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sum_distinct_triplet, run_max_sum_distinct_triplet
from .solution import Solution


class TestMaximizeYSumByPickingATripletOfDistinctXValues:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            ([1, 2, 1, 3, 2], [5, 3, 4, 6, 2], 14),
            ([1, 2, 1, 2], [4, 5, 6, 7], -1),
            ([1, 2, 3], [1, 2, 3], 6),
            ([1, 1, 1], [5, 5, 5], -1),
            ([1, 2, 1], [10, 20, 30], -1),
            ([3, 1, 2, 3], [4, 5, 6, 1], 15),
            ([1, 1, 2, 2, 3, 3], [1, 9, 2, 8, 3, 7], 24),
            ([5, 5, 4, 4, 3, 3], [1, 2, 3, 4, 5, 6], 12),
            ([2, 2, 1, 1, 3, 3], [7, 6, 5, 4, 3, 2], 15),
            ([1, 3, 2, 1, 3, 2], [10, 1, 1, 1, 10, 1], 21),
            ([4, 1, 3, 2, 4, 3, 4, 3], [8, 3, 6, 3, 8, 6, 2, 10], 21),
            ([1, 1, 1, 3, 4, 3], [2, 8, 8, 9, 7, 8], 24),
            ([2, 1, 3, 2, 3, 3, 1], [10, 3, 10, 7, 2, 9, 6], 26),
            ([4, 1, 2, 1, 4], [10, 4, 2, 4, 6], 16),
            ([1, 4, 2], [7, 2, 5], 14),
            ([2, 1, 4, 1, 3, 3, 4, 1], [5, 7, 7, 5, 4, 5, 4, 1], 19),
            ([4, 2, 3, 2, 1, 3], [7, 6, 5, 3, 7, 1], 20),
            ([1, 4, 3, 1, 3, 3], [5, 6, 10, 2, 3, 1], 21),
            ([1, 2, 4], [6, 9, 9], 24),
            ([1, 4, 4, 4, 3], [3, 8, 7, 5, 3], 14),
            ([1000000, 999999, 999998], [1000000, 1000000, 1000000], 3000000),
            ([1, 1, 1, 2, 2, 3], [1000000, 999999, 1, 2, 3, 4], 1000007),
        ],
    )
    def test_max_sum_distinct_triplet(self, x: list[int], y: list[int], expected: int):
        result = run_max_sum_distinct_triplet(Solution, x, y)
        assert_max_sum_distinct_triplet(result, expected)
