import pytest

from leetcode_py import logged_test

from .helpers import assert_count_triplets, run_count_triplets
from .solution import Solution


class TestCountTripletsThatCanFormTwoArraysOfEqualXor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 3, 1, 6, 7], 4),
            ([1, 1, 1, 1, 1], 10),
            ([1], 0),
            ([2, 2], 1),
            ([1, 1], 1),
            ([1, 2, 3], 2),
            ([4, 4, 4], 2),
            ([1, 2, 1], 0),
            ([2, 3, 1, 6, 7, 7], 5),
            ([6, 6, 6, 6], 6),
            ([1, 100000000, 100000000, 1], 4),
            ([3, 5, 3, 5, 3, 5], 9),
            ([1, 1, 2, 2, 1], 8),
            ([1, 9, 11, 5, 2, 4, 4, 11], 6),
            ([2, 8, 10, 1, 11, 3], 4),
            ([8, 10, 4, 8, 10, 9], 0),
            ([2, 5, 9, 5, 5, 12, 4, 4], 12),
        ],
    )
    def test_count_triplets(self, arr: list[int], expected: int):
        result = run_count_triplets(Solution, arr)
        assert_count_triplets(result, expected)
