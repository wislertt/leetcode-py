import pytest

from leetcode_py import logged_test

from .helpers import assert_find_longest_chain, run_find_longest_chain
from .solution import Solution


class TestMaximumLengthOfPairChain:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pairs, expected",
        [
            ([[1, 2], [2, 3], [3, 4]], 2),
            ([[1, 2], [7, 8], [4, 5]], 3),
            ([[1, 2]], 1),
            ([[3, 4], [1, 2]], 2),
            ([[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [0, 5], [3, 9], [-5, 10]], 3),
            ([[1, 3], [2, 4], [5, 6]], 2),
            ([[1, 2], [2, 3], [3, 4], [5, 6], [7, 8]], 4),
            ([[-1000, 1000]], 1),
            ([[1, 2], [1, 2], [1, 2]], 1),
            ([[5, 7], [1, 3], [9, 10], [4, 6]], 3),
            ([[1, 10], [2, 3], [4, 5], [6, 7]], 3),
        ],
    )
    def test_find_longest_chain(self, pairs: list[list[int]], expected: int):
        result = run_find_longest_chain(Solution, pairs)
        assert_find_longest_chain(result, expected)
