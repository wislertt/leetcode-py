import pytest

from leetcode_py import logged_test

from .helpers import assert_merge, run_merge
from .solution import Solution


class TestTestMergeSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, nums1, m, nums2, n, expected",
        [
            (Solution, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            (Solution, [1], 1, [], 0, [1]),
            (Solution, [0], 0, [1], 1, [1]),
            (Solution, [2, 0], 1, [1], 1, [1, 2]),
            (Solution, [1, 0], 1, [2], 1, [1, 2]),
            (Solution, [4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
            (Solution, [1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
            (Solution, [1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
            (Solution, [0, 0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),
            (Solution, [1, 2, 3, 4, 5, 6], 6, [], 0, [1, 2, 3, 4, 5, 6]),
            (Solution, [-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
            (Solution, [-10, -5, 0, 0, 0, 0], 2, [-3, -1, 7, 9], 4, [-10, -5, -3, -1, 7, 9]),
            (Solution, [5, 6, 7, 0, 0, 0], 3, [1, 2, 8], 3, [1, 2, 5, 6, 7, 8]),
            (Solution, [2, 2, 2, 0, 0, 0], 3, [2, 2, 2], 3, [2, 2, 2, 2, 2, 2]),
            (Solution, [1, 5, 9, 0, 0, 0, 0, 0], 3, [2, 3, 6, 7, 8], 5, [1, 2, 3, 5, 6, 7, 8, 9]),
            (Solution, [1, 0], 1, [0], 1, [0, 1]),
            (Solution, [-1, -1, 0, 0, 0], 2, [-1, -1, 0], 3, [-1, -1, -1, -1, 0]),
            (Solution, [1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]),
        ],
    )
    def test_merge(
        self,
        solution_class,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int,
        expected: list[int],
    ):
        result = run_merge(solution_class, nums1, m, nums2, n)
        assert_merge(result, expected)
