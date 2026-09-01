import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_chair, run_smallest_chair
from .solution import Solution


class TestSmallestUnoccupiedChair:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "times, target_friend, expected",
        [
            ([[1, 4], [2, 3], [4, 6]], 1, 1),
            ([[3, 10], [1, 5], [2, 6]], 0, 2),
            ([[1, 4], [2, 3], [4, 6]], 0, 0),
            ([[1, 4], [2, 3], [4, 6]], 2, 0),
            ([[3, 10], [1, 5], [2, 6]], 1, 0),
            ([[3, 10], [1, 5], [2, 6]], 2, 1),
            ([[1, 2], [3, 4]], 0, 0),
            ([[1, 2], [3, 4]], 1, 0),
            ([[1, 5], [2, 6], [3, 7]], 2, 2),
            ([[1, 3], [2, 5], [3, 4], [4, 6]], 3, 0),
            ([[1, 100], [2, 3], [3, 4], [4, 5]], 0, 0),
            ([[1, 100], [2, 3], [3, 4], [4, 5]], 3, 1),
            ([[5, 6], [1, 2], [2, 3], [3, 4]], 0, 0),
            ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], 0, 0),
            ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], 4, 0),
            ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], 4, 1),
            ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], 1, 1),
            ([[1, 12], [3, 6], [14, 25], [28, 29]], 1, 1),
            ([[2, 13], [9, 20], [12, 14], [15, 19], [21, 26], [24, 27], [25, 27]], 3, 0),
            ([[12, 16], [19, 21], [22, 24], [29, 40]], 0, 0),
        ],
    )
    def test_smallest_chair(self, times: list[list[int]], target_friend: int, expected: int):
        result = run_smallest_chair(Solution, times, target_friend)
        assert_smallest_chair(result, expected)
