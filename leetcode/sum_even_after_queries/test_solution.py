import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_even_after_queries, run_sum_even_after_queries
from .solution import Solution


class TestSumEvenAfterQueries:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, queries, expected",
        [
            ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
            ([1], [[4, 0]], [0]),
            ([1, 2, 3, 4], [[2, 0], [2, 1], [2, 2], [2, 3]], [6, 8, 8, 10]),
            ([0, 0, 0], [[1, 0], [1, 1], [1, 2]], [0, 0, 0]),
            ([5], [[-5, 0]], [0]),
            ([2, 4, 6], [[-2, 0], [-4, 1], [-6, 2]], [10, 6, 0]),
            ([1, 1, 1, 1], [[1, 0], [1, 1], [1, 2], [1, 3]], [2, 4, 6, 8]),
            ([-2, -4], [[1, 0], [3, 1]], [-4, 0]),
            ([3, 5, 7], [[-3, 0], [-5, 1], [-7, 2]], [0, 0, 0]),
            ([10, -10], [[-10, 0], [10, 1]], [-10, 0]),
            ([-4, 1, -10], [[3, 2], [-5, 1]], [-4, -8]),
            ([-6], [[-1, 0], [6, 0]], [0, 0]),
            ([-6, -8, 5, 6, -2], [[3, 0], [4, 2]], [-4, -4]),
            ([2], [[2, 0], [-5, 0], [6, 0]], [4, 0, 0]),
            ([10, 3, -10, 6], [[9, 0]], [-4]),
            ([-6], [[4, 0]], [-2]),
            ([-3], [[10, 0]], [0]),
            ([-9], [[-5, 0]], [-14]),
        ],
    )
    def test_sum_even_after_queries(
        self, nums: list[int], queries: list[list[int]], expected: list[int]
    ):
        result = run_sum_even_after_queries(Solution, nums, queries)
        assert_sum_even_after_queries(result, expected)
