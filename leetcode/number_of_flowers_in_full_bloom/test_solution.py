import pytest

from leetcode_py import logged_test

from .helpers import assert_full_bloom_flowers, run_full_bloom_flowers
from .solution import Solution


class TestNumberOfFlowersInFullBloom:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "flowers, people, expected",
        [
            ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11], [1, 2, 2, 2]),
            ([[1, 10], [3, 3]], [3, 3, 2], [2, 2, 1]),
            ([[5, 5]], [5], [1]),
            ([[1, 3], [2, 6]], [1, 2, 3, 4, 5, 6, 7], [1, 2, 2, 1, 1, 1, 0]),
            ([[10, 20]], [1, 10, 20, 21], [0, 1, 1, 0]),
            ([[1, 1000000000]], [1, 500000000, 1000000000], [1, 1, 1]),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], [2, 3, 5, 7, 9], [1, 1, 1, 1, 0]),
            ([[1, 1], [2, 2], [3, 3]], [1, 2, 3, 4], [1, 1, 1, 0]),
            ([[1, 4], [2, 3]], [3], [2]),
            ([[2, 3], [4, 5], [6, 7]], [1, 8], [0, 0]),
            ([[1, 5], [1, 5], [1, 5]], [3], [3]),
            ([[1, 5], [2, 7], [6, 9], [3, 4]], [1, 3, 5, 7, 9, 10], [1, 3, 2, 2, 1, 0]),
            ([[3, 12]], [22, 7, 21, 10], [0, 1, 0, 1]),
            ([[8, 18], [16, 20], [5, 11]], [17, 7, 5, 3, 8], [2, 1, 1, 0, 2]),
            ([[1, 14], [4, 4], [15, 16], [7, 17]], [1, 6, 18, 6], [1, 1, 0, 1]),
            ([[12, 19], [11, 18]], [7, 6, 11, 4, 5], [0, 0, 1, 0, 0]),
            ([[3, 12]], [4, 9, 15], [1, 1, 0]),
            ([[17, 18], [2, 5], [8, 20], [17, 19], [4, 5], [16, 16]], [16], [2]),
        ],
    )
    def test_full_bloom_flowers(
        self, flowers: list[list[int]], people: list[int], expected: list[int]
    ):
        result = run_full_bloom_flowers(Solution, flowers, people)
        assert_full_bloom_flowers(result, expected)
