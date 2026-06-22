import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_triplets, run_merge_triplets
from .solution import Solution


class TestMergeTripletsToFormTargetTriplet:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "triplets, target, expected",
        [
            ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
            ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
            ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
            ([[1, 1, 1]], [1, 1, 1], True),
            ([[1, 1, 1]], [2, 2, 2], False),
            ([[5, 5, 5]], [1, 1, 1], False),
            ([[2, 2, 2], [3, 3, 3]], [3, 3, 3], True),
            ([[1, 2, 3], [2, 3, 1], [3, 1, 2]], [3, 3, 3], True),
            ([[2, 2, 2], [2, 2, 2]], [2, 2, 2], True),
            ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [3, 3, 3], True),
            ([[1, 2, 3]], [1, 2, 3], True),
            ([[1, 2, 3]], [3, 2, 1], False),
            ([[1, 1, 3], [1, 3, 1], [3, 1, 1]], [3, 3, 3], True),
            ([[10, 1, 1], [1, 10, 1], [1, 1, 10]], [1, 1, 1], False),
            ([[1, 5, 3], [2, 1, 4]], [2, 5, 4], True),
        ],
    )
    def test_merge_triplets(self, triplets: list[list[int]], target: list[int], expected: bool):
        result = run_merge_triplets(Solution, triplets, target)
        assert_merge_triplets(result, expected)
